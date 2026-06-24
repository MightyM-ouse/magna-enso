# GOV-004 Held and Excluded Items Summary

Held and excluded objects remain untouched in the local source. This report contains only
category-level safe metadata; source hashes and relative paths are available in the
manifest without exposing file contents.

| Reason code | Objects | Files | Bytes | Treatment |
|---|---:|---:|---:|---|
| `GENERATED_ARCHIVE_PACKAGE` | 3 | 3 | 3,856,795 | Held; generated ZIP transport packages are not source |
| `RAW_LOG_TRACE_OR_SCREENSHOT` | 139 | 139 | 3,114,649 | Held; raw command output, logs, render outputs, and repeated screenshots belong in an approved artifact store |
| `RAW_VALIDATION_ARTIFACT_DIRECTORY` | 7 | 0 | 0 | Held; directory records retained only in manifest |
| `MACHINE_GENERATED_FILE` | 6 | 6 | 98,821 | Excluded; OS metadata and compiled cache files |
| `MACHINE_GENERATED_DIRECTORY` | 1 | 0 | 0 | Excluded; generated cache directory |

No secrets, credentials, unsafe personal-data binaries, oversize files, symlinks, special
objects, or unreadable files were detected. No held or excluded object was staged.
