class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        list_ = []
        for i,word in enumerate(words):
            first_word = word
            
            for j in range(i+1, len(words)):
                sec_word= words[j]
                
                
                if first_word in sec_word:
                        list_.append(first_word)
                elif sec_word in first_word:
                    list_.append(sec_word)

                else:
                    continue

                    

        list_ = list(set(list_))
        return list_