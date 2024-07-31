"""Description:
    You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

    We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

    We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

    Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

    For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
    Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
"""


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(2, n + 1):
            remaining_shelf_width = shelfWidth - books[i - 1][0]
            max_height = books[i - 1][1]
            dp[i] = books[i - 1][1] + dp[i - 1]

            j = i - 1
            while j > 0 and remaining_shelf_width - books[j - 1][0] >= 0:
                max_height = max(max_height, books[j - 1][1])
                remaining_shelf_width -= books[j - 1][0]
                dp[i] = min(dp[i], max_height + dp[j - 1])
                j -= 1

        return dp[n]


sol = Solution()
