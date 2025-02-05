class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1, s2 = list(s1), list(s2)
        i, j = 0, 0
        mismatch = 0
        s1_set, s2_set = set(), set()

        for i in range(len(s1)):
            if s1[i] != s2[j]:
                mismatch += 1
                s1_set.add(s1[i])
                s2_set.add(s2[j])
            j += 1

        return True if mismatch in [0, 2] and s1_set == s2_set else False