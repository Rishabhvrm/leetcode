class Solution:
    '''
    approach: brute force using built-in
    time: O(n * m), n: words in sentence, m: avg len of words
    '''
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")

        for idx, word in enumerate(sentence):
            # if word[: len(searchWord)] == searchWord:
            if word.startswith(searchWord):
                return idx + 1

        return -1
    
    '''
    approach-2: brute force w/o built-in function
    time: O(n * m), n: words in sentence, m: avg len of words
    space: O(n)
    '''
    def checkPrefix(self, prefix: str, word: str) -> bool:
        a, b = 0, 0
        while a < len(prefix) and b < len(word):
            if prefix[a] == word[b]:
                a, b = a + 1, b + 1
            else:
                return False
        return True if a == len(prefix) else False

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")

        for idx, word in enumerate(sentence, start=1):
            if self.checkPrefix(searchWord, word):
                return idx
        
        return -1


    '''
    approach-3: 2 pointers
    time: O(n), n: words in sentence
    space: O(1)
    '''
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a = 0
        word_idx = 1

        while a < len(sentence):
            b = 0
            
            # why does this not work if written here ??
            # while a < len(sentence) and b < len(searchWord) and sentence[a] == searchWord[b]:
            #     a, b = a + 1, b + 1


            # skip space and increment word count
            while a < len(sentence) and sentence[a] == " ":
                a += 1
                word_idx += 1
           
            # move both pointers for matching chars
            while a < len(sentence) and b < len(searchWord) and sentence[a] == searchWord[b]:
                a, b = a + 1, b + 1
            
            if b == len(searchWord):
                return word_idx
            
            # move to the end of current word
            while a < len(sentence) and sentence[a] != " ":
                a += 1

        return -1