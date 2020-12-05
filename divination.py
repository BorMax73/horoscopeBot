import random

file = open("Data/randomLine.txt", "r", encoding='utf8')
l = []
for k in file:
    l.append(k)


def random_line():
    return l[random.randint(0, len(l) - 1)]
