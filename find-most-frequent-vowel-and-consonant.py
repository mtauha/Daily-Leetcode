class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = defaultdict(int)
        consonant_count = defaultdict(int)
        max_vowel = max_cons = 0

        for i in s:
            if i in vowels:
                vowel_count[i] += 1
                max_vowel = max(max_vowel, vowel_count[i])
            else:
                consonant_count[i] += 1
                max_cons = max(max_cons, consonant_count[i])

        return max_vowel + max_cons
