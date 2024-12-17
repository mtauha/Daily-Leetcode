class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
            You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

            Return the lexicographically largest repeatLimitedString possible.

            A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.
        """
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(max_heap)
        result = []

        while max_heap:
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            result.append(char * use)

            if count > use and max_heap:
                next_char_neg, next_count = heappop(max_heap)
                result.append(chr(-next_char_neg))
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, count - use))

        return "".join(result)
