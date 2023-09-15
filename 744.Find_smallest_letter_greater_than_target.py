
def nextGreatestLetter(letters, target):
    for ele in letters:
        if ele > target:
            return ele

l = ["c","f","j"]
t = "a"

print(nextGreatestLetter(l,t))