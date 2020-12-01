from itertools import product

if __name__ == '__main__':
    with open("1.input") as f:
        a = f.readlines()
    a = [int(i.strip()) for i in a]
    a = product(a, a)
    for i in a:
        if i[0]+i[1] == 2020:
            print(i[0]*i[1])
