class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        sequences = list()
        alphabets = list()
        start = 0
        tmp = ""

        while start < len(s):
            copy = start

            while copy < len(s) and s[copy] not in alphabets:
                tmp += s[copy]
                alphabets.append(s[copy])
                copy += 1
            
            sequences.append(len(tmp))

            alphabets = list()
            tmp = ""
            start += 1
        
        answer = max(sequences)

        return answer