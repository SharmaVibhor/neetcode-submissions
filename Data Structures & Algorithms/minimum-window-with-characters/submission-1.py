class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or not s or not t:
            return ""

        window = defaultdict(int)
        hash_t = defaultdict(int)
        
        for i in range(len(t)):
            hash_t[t[i]]+=1

        res, reslen = [-1,-1], len(s)+1
        have, need = 0, len(hash_t)
        l = 0

        for r in range(len(s)):
            window[s[r]]+=1

            if s[r] in hash_t and window[s[r]]==hash_t[s[r]]:
                have+=1

            while have == need:
                if (r-l+1)<reslen:
                    reslen = r-l+1
                    res =[l,r]

                window[s[l]]-=1

                if s[l] in hash_t and window[s[l]]<hash_t[s[l]]:
                    have-=1
                l+=1
        
        l,r = res


        return s[l:r+1] if reslen <= len(s) else ""

        