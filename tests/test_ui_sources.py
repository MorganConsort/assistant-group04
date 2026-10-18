from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UI_PAGE = ROOT / "ui" / "index.html"
UI_README = ROOT / "ui" / "README.md"
SOURCE_MOCKUP = ROOT / "docs" / "ui-sources.md"


def test_source_design_document_exists():
    assert SOURCE_MOCKUP.is_file()


def test_source_design_contains_two_examples():
    documentation = SOURCE_MOCKUP.read_text(encoding="utf-8")

    assert "## Example 1: One source" in documentation
    assert "## Example 2: Multiple sources" in documentation
    assert documentation.count("**Sources**") == 2


def test_placeholder_demonstrates_accessible_sources():
    html = UI_PAGE.read_text(encoding="utf-8")

    assert 'aria-label="User message"' in html
    assert 'aria-label="Assistant message"' in html
    assert "user-avatar" in html
    assert "assistant-avatar" in html
    assert 'id="sources-heading"' in html
    assert 'aria-labelledby="sources-heading"' in html
    assert "Computational Thinking Course Schedule" in html


def test_readme_explains_source_metadata_flow():
    readme = UI_README.read_text(encoding="utf-8")

    assert "source metadata" in readme
    assert "docs/ui-sources.md" in readme
    assert "will not inspect `data/offices.csv` directly" in readme
