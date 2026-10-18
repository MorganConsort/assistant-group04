from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI_PAGE = ROOT / "ui" / "index.html"
UI_README = ROOT / "ui" / "README.md"
CHAT_MOCKUP = ROOT / "docs" / "ui-chat-placeholder.md"


def test_ui_requirement_files_exist():
    assert UI_PAGE.is_file()
    assert UI_README.is_file()
    assert CHAT_MOCKUP.is_file()


def test_placeholder_contains_required_controls():
    html = UI_PAGE.read_text(encoding="utf-8")

    assert "Study Assistant" in html
    assert 'id="question"' in html
    assert "<button" in html
    assert "Send" in html
    assert 'aria-live="polite"' in html


def test_readme_explains_backend_integration():
    readme = UI_README.read_text(encoding="utf-8")

    assert "from assistant.rules import reply" in readme
    assert "reply(user_message)" in readme


def test_chat_documentation_contains_mockup():
    documentation = CHAT_MOCKUP.read_text(encoding="utf-8")

    assert "## Mockup" in documentation
    assert "Your question" in documentation