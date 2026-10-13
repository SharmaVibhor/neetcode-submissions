class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                neighbor[pattern].append(word)

        visited = set()
        queue = collections.deque()
        visited.add(beginWord)
        queue.append(beginWord)
        distance = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return distance

                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for neWord in neighbor[pattern]:
                        if neWord not in visited:
                            visited.add(neWord)
                            queue.append(neWord)


            distance +=1

        return 0