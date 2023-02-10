def find_uniq(a):
    memo = {x: 0 for x in a}
    for i in a:
        if i in memo:
            memo[i] = memo[i]+1
    return [key for key, value in memo.items() if 1 == value][0]
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))