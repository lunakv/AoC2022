class File:
    def __init__(self, parent_dir, name: str, size: int):
        self.parent_dir = parent_dir
        self.size = size
        self.name = name

    def get_size(self) -> int:
        return self.size


class Dir:
    def __init__(self, parent_dir, name: str):
        self.name = name
        self.parent_dir = parent_dir
        self.files = {}
        self.dirs = {}

    def add_file(self, name, size):
        self.files[name] = File(self, name, size)

    def add_dir(self, name):
        self.dirs[name] = Dir(self, name)

    def cd(self, name):
        if name == "..":
            return self.parent_dir
        return self.dirs[name]

    def get_size(self) -> int:
        return sum(self.files[name].get_size() for name in self.files)

    def get_dir_sizes(self) -> list[(str, int)]:
        return self.__get_dir_sizes()[1]

    def __get_dir_sizes(self) -> (int, list[(str, int)]):
        dir_sizes = []
        self_size = 0
        for name in self.dirs:
            child_size, child_dir_sizes = self.dirs[name].__get_dir_sizes()
            dir_sizes += child_dir_sizes
            self_size += child_size

        for name in self.files:
            self_size += self.files[name].get_size()

        dir_sizes.append((self.name, self_size))
        return self_size, dir_sizes


def get_line():
    try:
        return input()
    except EOFError:
        return None


def parse_cd(arg: str) -> str:
    global current_dir
    global root
    if arg == "/":
        current_dir = root
    else:
        current_dir = current_dir.cd(arg)
    return get_line()


def parse_ls() -> str:
    line = get_line()
    while line and line[0] != "$":
        item = line.split()
        if item[0] == "dir":
            current_dir.add_dir(item[1])
        else:
            current_dir.add_file(item[1], int(item[0]))
        line = get_line()
    return line


def parse_command(line: str) -> str:
    command = line.split()
    if command[1] == "cd":
        return parse_cd(command[2])
    elif command[1] == "ls":
        return parse_ls()
    else:
        raise ValueError("Bad command " + line)


root = Dir(None, "/")
root.parent_dir = root
current_dir = root

line = get_line()
while line:
    line = parse_command(line)

small_dir_sizes_total = sum(
    item[1] for item in root.get_dir_sizes() if item[1] <= 100000
)
print(small_dir_sizes_total)
