#!/usr/bin/env python3
"""Validate the GOV-006 routing matrix and response-template contract."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required by the routing validator") from exc


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_tokens(path: str, tokens: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    missing = [token for token in tokens if token not in text]
    require(not missing, f"{path} missing: {missing}")


def main() -> int:
    matrix_path = ROOT / "trace/AGENT_ROUTING_MATRIX.yaml"
    matrix = yaml.safe_load(matrix_path.read_text(encoding="utf-8"))

    agents = matrix["agents"]
    require(set(agents) == {"chatgpt", "claude", "codex", "antigravity", "hermes"},
            "routing matrix must define exactly the governed agent set")
    require(agents["hermes"]["status"] == "inactive",
            "GOV-006 must not activate Hermes")
    require(matrix["final_authority"] == "product_owner",
            "Product Owner must remain final authority")

    routes = matrix["routes"]
    for name in [
        "architecture_design",
        "governance_change_chatgpt_authored",
        "governance_change_claude_authored",
        "product_implementation",
        "independent_qa_security",
        "status_reconciliation",
        "local_model_experiment",
    ]:
        require(name in routes, f"missing default route: {name}")

    require(routes["product_implementation"]["primary"] == "codex",
            "Codex must remain the default implementation worker")
    require(routes["product_implementation"]["reviewer"] == "antigravity",
            "Antigravity must remain the default implementation reviewer")
    require(routes["architecture_design"]["primary"] == "claude",
            "Claude must remain the default architecture worker")
    require("after_activation" in routes["local_model_experiment"]["primary"],
            "Hermes route must be activation-gated")

    require_tokens(
        "docs/governance/chatgpt-project-source/RESPONSE_CONTRACT.md",
        [
            "SYNC_PASS",
            "VERIFIED",
            "WORKER_CLAIM",
            "AGENT_LAUNCH",
            "APPROVE_TO_MERGE",
            "AGENT_ROUTING_AND_DISPATCH.md",
            "RESPONSE_TEMPLATES.md",
        ],
    )
    require_tokens(
        "docs/governance/chatgpt-project-source/RESPONSE_TEMPLATES.md",
        [
            "PROJECT_STATUS",
            "AGENT_RECOMMENDATION",
            "AGENT_LAUNCH",
            "WORKER_RESULT_REVIEW",
            "PRODUCT_OWNER_DECISION",
            "EXPLANATION",
            "BLOCKED_OR_DISCREPANCY",
        ],
    )
    require_tokens(
        "docs/governance/AGENT_ROUTING_AND_DISPATCH.md",
        ["ChatGPT", "Claude", "Codex", "Antigravity", "Hermes", "Proactive recommendation rule"],
    )

    print("GOV-006 routing and response validation: PASS")
    print(f"agents: {len(agents)}; default routes: {len(routes)}; response templates: 7")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print(f"GOV-006 routing and response validation: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
