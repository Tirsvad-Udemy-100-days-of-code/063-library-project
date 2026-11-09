#!/usr/bin/env bash
# Capture the screenshots of the named lecture steps inside a Docker container
# (never on the host desktop, see framework/process/gui-testing.md).
# Usage: bash scripts/screenshots/capture_screenshot.sh step-1-1-home [step-name ...]
#        bash scripts/screenshots/capture_screenshot.sh --all
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
export MSYS_NO_PATHCONV=1
mkdir -p "$root/docs/images"
docker build -q -t library-project-screenshots \
	-f "$root/scripts/screenshots/Dockerfile.screenshots" "$root/scripts/screenshots" >/dev/null
docker run --rm \
	-v "$root:/repo:ro" \
	-v "$root/docs/images:/out" \
	-e PYTHONDONTWRITEBYTECODE=1 \
	library-project-screenshots \
	bash /repo/scripts/screenshots/capture_in_container.sh "$@"
