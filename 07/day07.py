"""
--- Day 7: Supply Stacks  ---
https://adventofcode.com/2022/day/7
"""

out_folders = []


class Folder:
    """represents a folder"""

    def __init__(self, name, parent):
        self.files: list[int] = []
        self.subfolders: list[Folder] = []
        self.name = name
        self.parent = parent

    def get_size(self):
        """calculate the size of a folder recursively"""
        size = sum(self.files)
        for folder in self.subfolders:
            size += folder.get_size()
        out_folders.append(size)
        return size

    def get_name(self):
        """returns the folder name"""
        return self.name


def solve_day6():
    """solve day6"""
    global out_folders
    root_dir = Folder("/", None)

    current_dir = root_dir

    with open("input.txt", encoding="utf-8") as input_file:
        for i, line in enumerate(input_file):
            line = line.strip()
            splitted_line = line.split(" ")
            if i > 0:
                if "$" in splitted_line[0]:
                    if "cd" in splitted_line[1]:
                        if ".." in splitted_line[2]:
                            current_dir = current_dir.parent
                        else:
                            for folder in current_dir.subfolders:
                                if folder.name == splitted_line[2]:
                                    current_dir = folder
                                    break
                elif "dir" in splitted_line[0]:
                    dir_name = splitted_line[1]
                    current_dir.subfolders.append(
                        Folder(dir_name, current_dir))
                else:

                    file_size = int(splitted_line[0])
                    current_dir.files.append(file_size)

    disk_space = root_dir.get_size()
    at_most_100000 = list(filter(lambda x: x <= 100000, out_folders))

    to_delete = disk_space - (70000000 - 30000000)
    todo = min(list(filter(lambda x: x >= to_delete, out_folders)))

    print("sum of directories with a total size of at most 100000:",
          sum(at_most_100000))
    print("smallest directory that, if deleted, would free up enough space on:", todo)


solve_day6()
