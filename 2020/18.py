# https://code.activestate.com/recipes/384122-infix-operators/
class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rand__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __and__(self, other):
        return self.function(other)


plus = Infix(lambda x, y: x + y)
times = Infix(lambda x, y: x * y)


def part1(a):
    return sum(eval(l.replace('+', '|plus|').replace('*', '|times|')) for l in a)


def part2(a):
    return sum(eval(l.replace('+', '&plus&').replace('*', '|times|')) for l in a)


def solve(inp, ispart1):
    inp = inp.splitlines()
    return part1(inp) if ispart1 else part2(inp)


if __name__ == '__main__':
    from aocd import data, submit, AocdError

    try:
        submit(solve(data, True), part="a")
        submit(solve(data, False), part="b")
    except AocdError as e:
        print(e)
