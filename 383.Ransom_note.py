def canConstruct(ransomNote: str, magazine: str) -> bool:
    # char_count = {}

    # for ele in magazine:
    #     char_count[ele] = char_count.get(ele, 0) + 1

    # # if ele of ransomNote is not present in the dictionary => return False
    # # if ele of ransomNote is present but not enough occurances => return False
    # for ele in ransomNote:
    #     if ele in char_count and char_count[ele] > 0:
    #         char_count[ele] -= 1
    #     else: return False
    
    # return True

    ## ANOTHER WAY: USING FUNCTIONS
    def count_chars(s):
        char_count = {}
        for ele in s:
            char_count[ele] = char_count.get(ele, 0) + 1

        return char_count

    ransom_count = count_chars(ransomNote)
    magazine_count = count_chars(magazine)

    for ele, count in ransom_count.items():
        if ele not in magazine_count or count < magazine_count[ele]:
            return False
    
    return True

