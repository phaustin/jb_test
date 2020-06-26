from pathlib import Path
import sys

this_dir = Path(__file__).parent
root_dir = this_dir.parent
sys.path.insert(0,str(root_dir))
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n"
      f"back of path: {sys.path[-1]}\n{sep}\n")
