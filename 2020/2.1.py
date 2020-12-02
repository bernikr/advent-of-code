import re

p = re.compile(r"^(\d+)-(\d+) (\w): (.+)$")

if __name__ == '__main__':
    with open("2.input") as f:
        a = f.readlines()
    print(len([True for min, max, letter, string in [p.match(i).groups() for i in a]
               if int(min) <= string.count(letter) <= int(max)]))
