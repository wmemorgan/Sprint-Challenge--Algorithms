'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Iterative Solution
def count_th_iter(word):
    count = 0
    while len(word) > 0:
        if word[0:2] == "th":
            count += 1
            
        word = word[1:]

    return count

# Recursive Solution
def count_th(word):
    if len(word) == 0:
        return 0

    if word[0:2] == "th":
        return 1 + count_th(word[1:])

    return count_th(word[1:])
