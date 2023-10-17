def canConstruct(ransomNote: str, magazine: str) -> bool:
    char_count = {}

    for ele in magazine:
        char_count[ele] = char_count.get(ele, 0) + 1

    # if ele of ransomNote is not present in the dictionary => return False
    # if ele of ransomNote is present but not enough occurances => return False
    for ele in ransomNote:
        if ele in char_count and char_count[ele] > 0:
            char_count[ele] -= 1
        else: return False
    
    return True