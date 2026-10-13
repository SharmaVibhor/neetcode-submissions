class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        res = []
        cache = {}

        def isvalid(word):
            if word in cache:
                return cache[word]
            for i in range(1,len(word)):
                pre = word[:i]
                suf = word[i:]

                if pre in wordset and suf in wordset:
                    cache[word] = True
                    return True
                if pre in wordset and isvalid(suf):
                    cache[word] = True
                    return True

            cache[word] = False
            return False

        for w in words:
            if isvalid(w):
                res.append(w)
        
        return res
        