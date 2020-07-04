from pathlib import Path
from subprocess import run, PIPE
import pytest

path_tests = Path().resolve()
path_books = path_tests.joinpath("tmpbooks")
path_root = path_tests.parent

def test_build_page(tmpdir):
    """Test building the documentation book."""
    path_output = Path(tmpdir).absolute()
    path_page = path_tests.joinpath("test_pages", "single_page.ipynb")

    run(f"jb page {path_page} --path-output {path_output}".split(), check=True)
    path_html = path_output.joinpath("_build", "html")
    assert path_html.joinpath("single_page.html").exists()
    # The extra page shouldn't have been built with Sphinx (or run)
    assert not path_html.joinpath("extra_page.html").exists()
    # An index file should be created
    path_index = path_html.joinpath("index.html")
    assert path_index.exists()
    assert 'url=single_page.html" />' in path_index.read_text()


class TestPageExecute:

    basename = "nb_test_page_execute"
    cell_out_div = r'<div class="cell_output docutils container">'
    path_page = path_tests.joinpath("test_pages", f"{basename}.ipynb")

    def _run(self, tmpdir, flags=""):
        path_output = Path(tmpdir).absolute()
        out_html = path_output.joinpath("_build", "html", f"{self.basename}.html")
        run(
            f"jb page {self.path_page} --path-output {path_output} {flags}".split(),
            check=True,
        )
        with open(out_html, "r") as fh:
            self.html = fh.read()

    @property
    def has_cell_output(self):
        return self.cell_out_div in self.html

    @pytest.mark.parametrize(
        ("flag", "expected"),
        (("", True), ("--execute", True), ("--no-execute", False),),
    )
    def test_build_page_execute_flags(self, tmpdir, flag, expected):
        self._run(tmpdir, flags=flag)
        assert self.has_cell_output == expected
