from collections import defaultdict

from aocd import get_data


def execute_part1(p, regs={}):
    regs = defaultdict(lambda: 0, regs)

    def r(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    ip = 0
    sound = None
    while ip < len(p):
        match p[ip]:
            case ('snd', x):
                sound = r(x)
            case ('set', x, y):
                regs[x] = r(y)
            case ('add', x, y):
                regs[x] += r(y)
            case ('mul', x, y):
                regs[x] *= r(y)
            case ('mod', x, y):
                regs[x] %= r(y)
            case ('rcv', x):
                if r(x) != 0:
                    return sound
            case('jgz', x, y):
                if r(x) > 0:
                    ip += r(y)
                    continue
            case x:
                raise NotImplementedError(x)
        ip += 1
    return regs




def part1(inp):
    return execute_part1(inp)



class Program:
    def __init__(self, p, regs={}):
        self.p = p
        self.q = []
        self.regs = defaultdict(lambda: 0, regs)
        self.ip = 0
        self._blocked = False

    def r(self, x):
        try:
            return int(x)
        except ValueError:
            return self.regs[x]

    def execute_until_empty_queue(self):
        self._blocked = False
        while self.ip < len(self.p):
            match self.p[self.ip]:
                case ('snd', x):
                    yield self.r(x)
                case ('set', x, y):
                    self.regs[x] = self.r(y)
                case ('add', x, y):
                    self.regs[x] += self.r(y)
                case ('mul', x, y):
                    self.regs[x] *= self.r(y)
                case ('mod', x, y):
                    self.regs[x] %= self.r(y)
                case ('rcv', x):
                    if not self.q:
                        self._blocked = True
                        return
                    self.regs[x] = self.q.pop(0)
                case('jgz', x, y):
                    if self.r(x) > 0:
                        self.ip += self.r(y)
                        continue
                case x:
                    raise NotImplementedError(x)
            self.ip += 1

    def blocked(self):
        return self._blocked and not self.q

    def add_to_queue(self, e):
        self.q.append(e)


def part2(inp):
    p0 = Program(inp, {'p': 0})
    p1 = Program(inp, {'p': 1})
    n = 0
    while not p0.blocked() or not p1.blocked():
        for res in p0.execute_until_empty_queue():
            p1.add_to_queue(res)
        for res in p1.execute_until_empty_queue():
            n += 1
            p0.add_to_queue(res)
    return n


if __name__ == '__main__':
    data = get_data(day=18, year=2017)
    inp = [tuple(l.split(' ')) for l in data.splitlines()]
    print(part1(inp))
    print(part2(inp))
