from pathlib import Path
import os, sys

def sort_path_check(path: str) -> bool:
    if Path is None:
        return False
    p = Path(path)
    return p.exists() and p.is_dir()

def manage_file(file_path:Path):
    if not file_path.is_file:
        return
    parent_path = file_path.parent
    extension = file_path.suffix[1:]
    dir_destination = parent_path / extension
    if not dir_destination.exists():
        print(f"CREATING NEW {extension} DIRECTORY")
        os.makedirs(str(dir_destination))    
    os.replace(str(file_path), str(dir_destination/file_path.name))

path_to_sort = None
if len(sys.argv)>=2:
    path_to_sort = Path(sys.argv[1])

if path_to_sort is not None and sort_path_check(path_to_sort):
    children = list(path_to_sort.glob('*'))
    for f in children:
        manage_file(f)
else:
    print("ERROR: Path not found.")