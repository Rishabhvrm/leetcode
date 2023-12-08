class Solution:
    def interpret(self, command: str) -> str:
        # return command.replace("()", "o").replace("(al)", "al")

        ## APPROACH: store mapping, 
        # traverse string and if any substring found in map, 
        # add it's mapped value to result
        # reset temp (substring helper)

        ## TIME: O(n)
        ## SPACE: O(1)

        d = {
            "(al)": "al",
            "()": "o",
            "G": "G"
        }

        temp, res = "", ""

        for i in range(len(command)):
            temp += command[i]
            if temp in d:
                res += d[temp]      # add mapped value to result
                temp = ""           # reset temp

        return res