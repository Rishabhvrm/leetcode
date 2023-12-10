class Solution:
    def freqAlphabets(self, s: str) -> str:
        ## APPROACH: create map; traverse backwards
        ## replace digits with chars (2 digits for #)
        ## TIME: O(n)
        ## SPACE: O(n), output array

        res = []
        i_a = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10": "j",
            "11": "k",
            "12": "l",
            "13": "m",
            "14": "n",
            "15": "o",
            "16": "p",
            "17": "q",
            "18": "r",
            "19": "s",
            "20": "t",
            "21": "u",
            "22": "v",
            "23": "w",
            "24": "x",
            "25": "y",
            "26": "z"
        }

        i = len(s) - 1

        while i > -1:
            if s[i] == "#":                 # swap 2 digits if char == #
                res.append(i_a[s[i - 2] + s[i - 1]])
                i -= 2
            else: res.append(i_a[s[i]])     # else repalce single digit
            
            i -= 1

        return "".join(res[::-1])

    
obj = Solution()
s = "10#11#12"
# s = "1326#"
print(obj.freqAlphabets(s))