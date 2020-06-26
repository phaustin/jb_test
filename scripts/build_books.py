from pathlib import Path
import click
import subprocess
import shutil
from format_html import link_tuple, make_page
import context

@click.group()
def main():
    """
    build books
    """
    pass


def find_books(books_folder):
    toc_files = Path(books_folder).glob("**/_toc.yml")
    book_folders = [item.parent for item in toc_files]
    return book_folders

def find_albums(albums_folder):
    sphinx_files = Path(albums_folder).glob("**/conf.py")
    albums_folders = [item.parent for item in sphinx_files]
    return albums_folders

@main.command()
@click.option('--verbose', is_flag=True)
def build_books(verbose):
    books_folder = context.root_dir / "books"
    all_books = find_books(books_folder)
    html_copy_dir = books_folder.parent /  "html/books"
    print(f"will write html to {html_copy_dir}")
    if html_copy_dir.exists():
        print(f"removing {html_copy_dir}")
        shutil.rmtree(html_copy_dir)
    for a_book_dir in all_books:
        command = f"jb build {a_book_dir}"
        print(f"running the command \n{command}\n")
        arglist=command.split()
        result = subprocess.run(arglist, capture_output=True)
        if verbose:
            if result.stdout:
                print(f"stdout message: {result.stdout.decode('utf-8')}")
            if result.stderr:
                print(f"stderror message: {result.stderr.decode('utf-8')}")
        html_copy_dir.mkdir(exist_ok=True,parents=True)
        rel_dir = a_book_dir.relative_to(books_folder)
        book_title = rel_dir.parts[0]
        copy_to_dir = html_copy_dir / f"{book_title}_html"
        orig_dir = a_book_dir / "_build/html"
        print(f"copying {orig_dir} to {copy_to_dir}")
        shutil.copytree(orig_dir, copy_to_dir)

@main.command()
@click.option('--verbose', is_flag=True)
def make_index(verbose):
    books_folder = context.root_dir / "html/books"
    link_list = []
    index_files = Path("html").glob("**/index.html")
    for a_file in index_files:
        print(f"processing {a_file}")
        breakpoint()
        if len(a_file.parts) == 3:
            rel_file = a_file.relative_to(context.root_dir)
            html_dir, dir_name, rest = a_file.parts[:3]
            link_list.append(link_tuple(url=a_file.as_posix(),descrip=dir_name))
    page_out = make_page("book_dir",link_list)
    with open("index.html","w",encoding="utf8") as outfile:
        outfile.write(page_out)
    

if __name__ == "__main__":
    main()
