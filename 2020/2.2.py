import re

p = re.compile(r"^(\d+)-(\d+) (\w): (.+)$")

if __name__ == '__main__':
    with open("2.input") as f:
        a = f.readlines()
    print(len([True for pos1, pos2, letter, string in [p.match(i).groups() for i in a]
               if (string[int(pos1)-1] == letter) ^ (string[int(pos2)-1] == letter)]))
