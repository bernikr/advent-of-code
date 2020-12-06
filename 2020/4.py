import re

from aocd import get_data


def part1(a):
    return sum(all(k in i for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) for i in a)


def part2(a):
    return sum(all(k in i for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) and
               all([
                   1920 <= int(i['byr']) <= 2002,
                   2010 <= int(i['iyr']) <= 2020,
                   2020 <= int(i['eyr']) <= 2030,
                   (
                           (i['hgt'][3:] == 'cm' and 150 <= int(i['hgt'][:3]) <= 193)
                           or (i['hgt'][2:] == 'in' and 59 <= int(i['hgt'][:2]) <= 76)
                   ),
                   re.match(r'^#[0-9a-f]{6}$', i['hcl']) is not None,
                   i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                   re.match(r'^\d{9}$', i['pid']) is not None])
               for i in a)


if __name__ == '__main__':
    data = get_data(day=4, year=2020)
    input = [{k: v for k, v in (j.split(':') for j in i.replace('\n', ' ').split(' '))} for i in data.split('\n\n')]
    print(part1(input))
    print(part2(input))
