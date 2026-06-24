"""Adversarial analysis demonstrating policy bypasses against Command Center's risk policy engine.

Written as part of the independent validation review.
"""
import sys

# Add Command Center backend to sys.path
sys.path.append("<LOCAL_USER_HOME>/Projects/AI/magna-command-center/backend")

from app.services.risk_policy_engine import evaluate_policy
from app.models.risk_policy_models import PolicyActionDescriptor, ExecutionIntent, PolicyConfidence

def test_bypass(prompt: str, paths: list[str] = None):
    action = PolicyActionDescriptor(
        action_text=prompt,
        paths=paths or [],
        declared_tier=None,
        intent=ExecutionIntent.RUNNER_BOUND_PROPOSAL,
        confidence=PolicyConfidence.HIGH,
        requires_execution=True,
        runner_bound=True
    )
    result = evaluate_policy(action)
    print(f"Prompt: {prompt}")
    print(f"Paths Checked: {paths}")
    print(f"Effective Tier: {result.effective_tier}")
    print(f"Approval Required: {result.approval_required}")
    print(f"Rules Matched: {result.matched_rules}")
    print(f"Blocked: {result.blocked}")
    for pa in result.path_assessments:
        print(f"  Path Assessment for '{pa.path}': Zone={pa.zone.name}, MatchedRoot={pa.matched_root}, Reason={pa.reason}")
    print("-" * 50)

if __name__ == "__main__":
    print("Running Adversarial Bypass Checks against Command Center...")
    print("-" * 50)
    
    # 1. Directory Traversal via relative paths escaping the project root
    test_bypass("Read configurations", ["../../PrivateVault/secret.txt"])
    test_bypass("Read systems files", ["../../../../etc/passwd"])
    
    # 2. Command bypass using unlink instead of delete
    test_bypass("unlink the system configurations")
    
    # 3. Evading .env regex by using hex representation or shell variable split in command text
    test_bypass("cat .e'nv'")
