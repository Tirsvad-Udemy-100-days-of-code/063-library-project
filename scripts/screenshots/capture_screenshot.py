"""@brief Capture the screenshot of lecture steps with a headless browser.

Runs inside the Docker container started by capture_screenshot.sh, never on the
host desktop. The step definitions live in screenshots.json. A "web" step starts
the named app, drives it and takes a screenshot of the page. A "script" step runs
a lecture script and takes a screenshot of its output.
"""

import html
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/out")
BASE_URL = "http://127.0.0.1:5000"
VIEWPORT = {"width": 900, "height": 460}
APPS = {
    "in_memory": ["python", "-m", "library_project.main_in_memory"],
    "library": ["python", "-m", "library_project.main"],
}


def wait_for_server() -> None:
    """@brief Wait until the app answers on BASE_URL."""
    for _ in range(100):
        try:
            # nosemgrep: opengrep.rules.python.lang.security.audit.insecure-transport.urllib.insecure-urlopen
            urllib.request.urlopen(BASE_URL + "/")  # local test server inside the container
            return
        except OSError:
            # nosemgrep: opengrep.rules.python.lang.best-practice.arbitrary-sleep
            time.sleep(0.3)  # poll until the server inside the container answers
    raise RuntimeError("The app did not start.")


def run_actions(page: Page, actions: list[dict[str, str]]) -> None:
    """@brief Drive the page with the actions of a step.

    @param page The browser page.
    @param actions Dictionaries with one of the keys goto, fill, click.
    """
    for action in actions:
        if "goto" in action:
            page.goto(BASE_URL + action["goto"])
        elif "fill" in action:
            page.fill(action["fill"], action["value"])
        elif "click" in action:
            page.click(action["click"])


def capture_web(step: dict[str, object]) -> None:
    """@brief Capture one web step with a fresh app and a fresh database.

    @param step A step definition from screenshots.json.
    """
    shutil.rmtree("instance", ignore_errors=True)
    # nosemgrep: opengrep.rules.python.lang.security.audit.dangerous-subprocess-use-audit
    server = subprocess.Popen(APPS[str(step["app"])])  # fixed commands from APPS
    try:
        wait_for_server()
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport=VIEWPORT)
            run_actions(page, step["actions"])  # type: ignore[arg-type]
            page.screenshot(path=str(OUTPUT_DIR / f"{step['name']}.png"))
            browser.close()
    finally:
        server.terminate()
        server.wait()


def capture_script(step: dict[str, object]) -> None:
    """@brief Capture the output of a lecture script as a screenshot.

    @param step A step definition from screenshots.json.
    """
    shutil.rmtree("instance", ignore_errors=True)
    for path in Path(".").glob("*.db"):
        path.unlink()
    lines = []
    for command in step["commands"]:  # type: ignore[attr-defined]
        # nosemgrep: opengrep.rules.python.lang.security.audit.dangerous-subprocess-use-audit
        done = subprocess.run(  # commands come from screenshots.json in this repository
            command, capture_output=True, text=True, check=False
        )
        lines.append("$ " + " ".join(command))
        lines.append((done.stdout + done.stderr).rstrip())
    page_html = (
        "<body style='font-family:monospace;background:#1e1e1e;color:#ddd;"
        "padding:16px'><h3 style='color:#9cdcfe'>"
        + html.escape(str(step["title"]))
        + "</h3><pre>"
        + html.escape("\n".join(lines))
        + "</pre></body>"
    )
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        page.set_content(page_html)
        page.screenshot(path=str(OUTPUT_DIR / f"{step['name']}.png"))
        browser.close()


def main() -> None:
    """@brief Capture the steps named on the command line, or all with --all."""
    steps = json.loads((ROOT / "screenshots.json").read_text(encoding="utf-8"))
    wanted = sys.argv[1:]
    for step in steps:
        if "--all" in wanted or step["name"] in wanted:
            if step["kind"] == "web":
                capture_web(step)
            else:
                capture_script(step)


if __name__ == "__main__":
    main()
