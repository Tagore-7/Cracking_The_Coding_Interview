# implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def (s):
    # use two for loops but that's o(n^2) solution 
    if len(s) > 128:
        return False
    char_set = [False] * 128
    for i in range(len(s)):
        val = ord(s[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True
