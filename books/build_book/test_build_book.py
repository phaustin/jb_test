from pathlib import Path
from subprocess import run, PIPE
import shutil

def test_build_book(tmpdir):
    """Test building the book template and a few test configs."""
    # Create the book from the template
    the_path = Path(tmpdir).joinpath("mybook").absolute()
    if the_path.exists():
        shutil.rmtree(the_path)
    run(f"jb create {the_path}".split())

    # Ensure the book is created properly
    assert the_path.joinpath("_config.yml").exists()

    # Build the book
    run(f"jb build {the_path}".split(), check=True)
    path_html = the_path.joinpath("_build", "html")
    assert path_html.joinpath("index.html").exists()
    assert path_html.joinpath("intro.html").exists()

    # Test custom config values
    path_config = Path().joinpath("config_book")
    run(f"jb build {path_config}".split(), check=True)
    html = path_config.joinpath("_build", "html", "index.html").read_text(
        encoding="utf8"
    )
    assert '<h1 class="site-logo" id="site-title">TEST PROJECT NAME</h1>' in html
    assert '<div class="sphinx-tabs docutils container">' in html
    assert '<link rel="stylesheet" type="text/css" href="_static/mycss.css" />' in html
    assert '<script src="_static/js/myjs.js"></script>' in html

if __name__ == "__main__":
    tmpdir = "default_book"
    test_build_book(tmpdir)
