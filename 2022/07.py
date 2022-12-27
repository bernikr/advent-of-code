def get_files_and_dirs(inp):
    dir = ""
    files = {}
    dirs = ['/']
    for c in inp:
        match c:
            case []:
                pass
            case [('cd', '/')]:
                dir = '/'
            case [('cd', '..')]:
                dir = '/'.join(dir.split('/')[:-2]) + '/'
            case [('cd', d)]:
                dir += d + '/'
            case [('ls', ), *fs]:
                for size, filename in fs:
                    if size == "dir":
                        dirs.append(dir + filename + '/')
                    else:
                        files[dir + filename] = int(size)
    return files, dirs


def solve1(inp):
    files, dirs = inp
    return sum(s for s in (sum(s for f, s in files.items() if f.startswith(d)) for d in dirs) if s <= 100000)


def solve2(inp):
    files, dirs = inp
    disk_space = 70000000
    needed_space = 30000000
    used_space = sum(files.values())
    additional_required = needed_space - disk_space + used_space
    return sorted(s for s in (sum(s for f, s in files.items() if f.startswith(d)) for d in dirs)
                  if s >= additional_required)[0]


def solve(inp, part1):
    inp = [[tuple(l.split(' ')) for l in c.strip().splitlines()] for c in inp.split('$')]
    inp = get_files_and_dirs(inp)
    return solve1(inp) if part1 else solve2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
