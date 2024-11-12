class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
            You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

            You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

            Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
        """
        answer = []
        dictionary = {}
        for price, beauty in items:
            if price not in dictionary.keys():
                dictionary[price] = [beauty]
            else:
                dictionary[price].append(beauty)
        
        for i in dictionary.keys():
            dictionary[i].sort(reverse=True)
        
        dictionary = OrderedDict(sorted(dictionary.items(), key=lambda x: x[1][0], reverse=True))
        
        for query in queries:
            curr = 0
            for price in dictionary.keys():
                if price <= query:
                    curr = dictionary[price][0]
                    break
            answer.append(curr)
        
        return answer
