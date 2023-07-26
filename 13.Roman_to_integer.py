def romanToInt(s):

    total = 0
    n = len(s)

    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(n-1):
        # Roman numerals are usually written largest to smallest from left to right.
        # if not then it means it's a case like IV or IX
        if romans[s[i]] < romans[s[i+1]]:
            total -= romans[s[i]]
        else:
            total += romans[s[i]]

    # add last element
    total += romans[s[-1]]

    return total

print(romanToInt("VII"))

