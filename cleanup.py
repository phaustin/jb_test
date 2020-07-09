import click
from pathlib import Path
import shutil

@click.command()
@click.argument("book_path", type=str, nargs=1)
def remove_default(book_path):
    """Remove all subfolders in _build except .jupyter_cache."""
    print(f"inside {book_path} -- removing all except cache")
    build_path = Path(book_path) / "_build"
    to_remove = [
        dd for dd in build_path.iterdir() if dd.is_dir() and dd.name != ".jupyter_cache"
    ]
    for dd in to_remove:
        shutil.rmtree(build_path.joinpath(dd.name))

if __name__ == "__main__":
    remove_default()
