from pathlib import Path
import click
import subprocess
import shutil
from format_html import link_tuple, make_page
import context
import sys
import json

@click.group()
def main():
    """
    build books
    """
    pass


def find_books(books_folder):
    toc_files = Path(books_folder).glob("**/_toc.yml")
    book_folders = [item.parent for item in toc_files]
    print(f"found these folders {book_folders}")
    str_paths = [item.as_posix() for item in book_folders]
    with open("all_books.json",'w') as outfile:
        json.dump(str_paths,outfile,indent=4)
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
    platform_specific = f"html/books/{sys.platform}"
    html_copy_dir = books_folder.parent /  platform_specific
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
def clean():
    with open("all_books.json",'r') as infile:
        book_list = json.load(infile)
    for a_book in book_list:
        the_command = f"jb clean -a {a_book}"
        arglist = the_command.split()
        print(f"running command {the_command}")
        result = subprocess.run(arglist, capture_output=True)
        if result.stdout:
            print(f"stdout message: {result.stdout.decode('utf-8')}")
        if result.stderr:
            print(f"stderror message: {result.stderr.decode('utf-8')}")
        
        
@main.command()
@click.option('--verbose', is_flag=True)
def make_index(verbose):
    books_folder = context.root_dir / "html/books"
    link_list = []
    index_files = Path("html").glob("**/index.html")
    for a_file in index_files:
        full_path = a_file.resolve()
        local_path = full_path.relative_to(context.root_dir)
        print(f"processing {full_path}")
        #local_path.parts
        # ('html', 'books', 'darwin', 'toc_wrongkey_html', 'index.html')
        if len(a_file.parts) == 5:
            dir_name = f"{local_path.parts[2]}_{local_path.parts[3]}"
            link_list.append(link_tuple(url=a_file.as_posix(),descrip=dir_name))
    page_out = make_page("book_dir",link_list)
    with open("index.html","w",encoding="utf8") as outfile:
        outfile.write(page_out)
    

if __name__ == "__main__":
    main()
