from collections import Counter, defaultdict


class Solution:
    '''
    a: 2
    b: 3
    c: 1
    d: 5
    e: 2
    f:
    g:
    h: 

    1 - 8
    9 - 16
    17 - 24
    > 24
    '''
    '''
    Approach: Using hash-map, most frequent char mapped first
    you'd want to place such chars at 1st position of the key
    Time: O(n), even though we're sorting it'll be constant bcz max chars is 26
    Space: O(n), using extra map, could be O(1) bcz it'll never store more than 26 chars
    '''
    def minimumPushes(self, word: str) -> int:
        char_freq = Counter(word)
        char_freq = dict(sorted(char_freq.items(), key= lambda x: x[1], reverse=True))

        new_map = defaultdict(int)
        i = 1
        for k, v in char_freq.items():
            new_map[i] = v
            i += 1

        presses = 0
        for k, v in new_map.items():
            if k <= 8:
                presses += v
            elif 9 <= k <= 16:
                presses += (2 * v)
            elif 17 <= k <= 24:
                presses += (3 * v)
            else:
                presses += (4 * v)
            # presses += v * (1 + (k // 8))         # doesn't work
        
        return presses

    '''
    Approach: array
    Time: O(n), even though we're sorting it'll be constant bcz max chars is 26
    Space: O(n), could be O(1) bcz it'll never store more than 26 chars
    '''
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26

        for c in word:
            counts[ord(c) - ord('a')] += 1
        counts.sort(reverse=True)

        res = 0
        for i, c in enumerate(counts):
            res += c * (1 + (i // 8))

        return res