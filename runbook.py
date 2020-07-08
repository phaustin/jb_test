from jupyter_book.commands import main
from pathlib import Path
import shutil

def remove_default(path):
    """Remove all subfolders in _build except .jupyter_cache."""
    print(f"inside {path} -- removing all except cache")
    to_remove = [
        dd for dd in path.iterdir() if dd.is_dir() and dd.name != ".jupyter_cache"
    ]
    for dd in to_remove:
        shutil.rmtree(path.joinpath(dd.name))


if __name__ == "__main__":
    this_dir = Path().resolve()
    build_dir = this_dir / "books/toc_urllink/_build"
    if build_dir.is_dir():
        print("removing _build")
        remove_default(build_dir)
    main()
