class Solution:
    '''
    Approach: Store the curr state in a map
    if seen before, update the length
    Time: O(N)
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}
        state = [0, 0, 0, 0, 0]
        curr_state = "00000"    # for a, e, i, o, u
        mp[curr_state] = -1     # state "00000" i.e all even was seen at idx -1 first

        res = 0
        for i in range(len(s)):
            if s[i] == "a":
                state[0] = (state[0] + 1) % 2
            elif s[i] == "e":
                state[1] = (state[1] + 1) % 2
            elif s[i] == "i":
                state[2] = (state[2] + 1) % 2
            elif s[i] == "o":
                state[3] = (state[3] + 1) % 2
            elif s[i] == "u":
                state[4] = (state[4] + 1) % 2

            curr_state = ""
            for ele in state:
                curr_state += str(ele)
            
            if curr_state in mp:
                res = max(res, i - mp[curr_state])  # length
            else:
                mp[curr_state] = i

        return res

    '''
    Approach: Same as above, just using XOR instead of incrementing the count and % 2
    Time: O(N)
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}
        state = [0, 0, 0, 0, 0]
        curr_state = "00000"    # for a, e, i, o, u
        mp[curr_state] = -1     # state "00000" i.e all even was seen at idx -1 first

        res = 0
        for i in range(len(s)):
            if s[i] == "a":
                state[0] ^= 1
            elif s[i] == "e":
                state[1] ^= 1
            elif s[i] == "i":
                state[2] ^= 1
            elif s[i] == "o":
                state[3] ^= 1
            elif s[i] == "u":
                state[4] ^= 1

            curr_state = ""
            for ele in state:
                curr_state += str(ele)
            
            if curr_state in mp:
                res = max(res, i - mp[curr_state])  # length
            else:
                mp[curr_state] = i

        return res

    '''
    Approach-2: using an integer 'mask' instead of array
    Time: O(N)
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {}
        mask = 0                # 00000
        mp[mask] = -1     # state "00000" i.e all even was seen at idx -1 first

        res = 0
        for i in range(len(s)):
            if s[i] == "a":
                mask = mask ^ (1 << 0)
            elif s[i] == "e":
                mask = mask ^ (1 << 1)
            elif s[i] == "i":
                mask = mask ^ (1 << 2)
            elif s[i] == "o":
                mask = mask ^ (1 << 3)
            elif s[i] == "u":
                mask = mask ^ (1 << 4)

            if mask in mp:
                res = max(res, i - mp[mask])
            else:
                mp[mask] = i

        return res
