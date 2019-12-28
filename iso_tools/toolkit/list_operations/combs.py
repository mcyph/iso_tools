def get_L_all_combs(items, n):
    if n==0: 
        yield []
    else:
        for i in range(len(items)):
            for cc in get_L_all_combs(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc


def get_L_unique_combs(items, n):
    if n==0: 
        yield []
    else:
        for i in range(len(items)):
            for cc in get_L_unique_combs(items[i+1:],n-1):
                yield [items[i]]+cc


def get_L_selections(items, n):
    if n==0: 
        yield []
    else:
        for i in range(len(items)):
            for ss in get_L_selections(items, n-1):
                yield [items[i]]+ss


def get_L_all_perms(items):
    return get_L_all_combs(items, len(items))


if __name__=="__main__":
    print("Permutations of 'love'")
    for p in xpermutations(['l','o','v','e']): print(''.join(p))

    print()
    print("Combinations of 2 letters from 'love'")
    for c in xcombinations(['l','o','v','e'],2): print(''.join(c))

    print()
    print("Unique Combinations of 2 letters from 'love'")
    for uc in xuniqueCombinations(['l','o','v','e'],2): print(''.join(uc))

    print()
    print("Selections of 2 letters from 'love'")
    for s in xselections(['l','o','v','e'],2): print(''.join(s))

    print()
    print(list(map(''.join, list(xpermutations('done')))))
