class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        H = {}
        for c in chars:
            if c in H: H[c] +=1
            else:      H[c] = 1
        
        
        
        
        for word in words:#word很多字 word是其中一個
            wordH = {}
            for c in word:
                if c in wordH: wordH[c] +=1
                else:           wordH[c] = 1

            bad = 0
            for c in wordH:
            
            
            #裡面要看 能不能用chars來組合word
            
                if(c not in H) or wordH[c] > H[c]:
                    bad = 1
                #看中間會不會成功
            if bad==0: ans += len(word)#成功 ans就增加
        return ans