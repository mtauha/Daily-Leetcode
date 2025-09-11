class Solution:
    def sortVowels(self, s: str) -> str:
        pattern = r'[AaeEiIoOuU]'
        vowels = []
        for i in s:
            if re.match(pattern=pattern, string=i):
                heapq.heappush(vowels, i)
        
        t = ""
        for i in s:
            if re.match(pattern=pattern, string=i):
                t += heapq.heappop(vowels)
            else:
                t += i
        
        return t
