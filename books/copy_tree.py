from pathlib import Path
import subprocess
from collections import namedtuple
import shutil

toc_pair = namedtuple("toc_pair",["dest_folder","target_toc"])

jbook = Path.home() / "repos/jupyter-book/tests/books/toc"
all_files = list(jbook.glob("*"))
good_files = [item for item in all_files if str(item.name)[0] != '_']
target_dirs = list(Path().glob("toc*"))
# for the_target in target_dirs:
#     for the_source in good_files:
#         the_command = f"cp -af {str(the_source)} {str(the_target)}/."
#         print(f"running {the_command}")
#         args = the_command.split()
#         result=subprocess.run(args,capture_output=True)
#         if result.stdout:
#             print(f"stdout message: {result.stdout.decode('utf-8')}")
#         if result.stderr:
#             print(f"stderror message: {result.stderr.decode('utf-8')}")

toc_files =  [item for item in all_files if str(item.name).find('_toc') > -1]
def folder_name(toc_file):
    new_name = None
    parts = toc_file.name.split('_')
    if len(parts) == 3:
        new_name = Path(f"{parts[1]}_{parts[2]}").with_suffix("")
    return new_name

pair_list = []
for a_file in toc_files:
    out = folder_name(a_file)
    if out:
        pair_list.append(toc_pair(out,a_file.resolve()))

from pprint import pprint
pprint(pair_list)
print(len(pair_list))
for item in pair_list:
    command = f"cp -af {str(item.target_toc)} {str(item.dest_folder)}/_toc.yml"
    args = command.split()
    result=subprocess.run(args,capture_output=True)
    if result.stdout:
        print(f"stdout message: {result.stdout.decode('utf-8')}")
    if result.stderr:
        print(f"stderror message: {result.stderr.decode('utf-8')}")
    
