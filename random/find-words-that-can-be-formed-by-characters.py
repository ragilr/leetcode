class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        # print("count",count)
        ret = 0
        for word in words:
            wordCounter = Counter(word)
            possible = True
            # print("word",word,wordCounter)
            for k,v in wordCounter.items():
                print(k,v)
                if k not in count or v > count[k]:
                    possible = False
                    # print("not possible")
                    break
            if possible:
                ret += len(word)
        return ret
