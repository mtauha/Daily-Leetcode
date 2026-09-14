class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x = (rec1[0], rec1[2])
        rec1_y = (rec1[1], rec1[3])
        rec2_x = (rec2[0], rec2[2])
        rec2_y = (rec2[1], rec2[3])

        if (
            min(rec1_x) < max(rec2_x)
            and max(rec1_x) > min(rec2_x)
            and min(rec1_y) < max(rec2_y)
            and max(rec1_y) > min(rec2_y)
        ):
            return True
        else:
            return False
