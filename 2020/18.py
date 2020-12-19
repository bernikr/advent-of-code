from aocd import get_data


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


if __name__ == '__main__':
    data = get_data(day=18, year=2020)
    inp = data.splitlines()
    print(part1(inp))
    print(part2(inp))
