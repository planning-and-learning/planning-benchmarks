#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd -- "${SCRIPT_DIR}/.." && pwd)

while IFS= read -r generator; do
    relative_path=${generator#"${REPO_ROOT}/"}
    echo "Generating ${relative_path}"
    python3 "${generator}"
done < <(find "${SCRIPT_DIR}" -name generate_instances.py -type f | sort)

python3 "${SCRIPT_DIR}/obfuscate_pddl.py" \
    --source "${SCRIPT_DIR}" \
    --target "${REPO_ROOT}/obfuscated_data"
