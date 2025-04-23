class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = Counter()

        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            counter[key] += 1
        
        maxvalue = max(counter.values())

        return sum(1 for _ in counter.values() if _ == maxvalue)

        
