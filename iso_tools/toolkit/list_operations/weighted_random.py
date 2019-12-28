from collections import Counter
from random import randint


def weighted_random(pairs):
    """
    https://stackoverflow.com/questions/14992521/python-weighted-random
    """
    total = sum(pair[0] for pair in pairs)
    r = randint(1, total)

    for (weight, value) in pairs:
        r -= weight
        if r <= 0:
            return value


if __name__ == '__main__':
    results = Counter(
        weighted_random([(1,'a'),(1,'b'),(18,'c')])
        for _ in range(20000)
    )
    print(results)
