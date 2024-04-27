class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        min_time = 0
        current_point = points[0]

        for point in points:
            min_time += max(
                abs(point[0] - current_point[0]), abs(point[1] - current_point[1])
            )
            current_point = point
        
        return min_time


if __name__ == "__main__":
    solution = Solution()
    points = [
        [559, 511],
        [932, 618],
        [-623, -443],
        [431, 91],
        [838, -127],
        [773, -917],
        [-500, -910],
        [830, -417],
        [-870, 73],
        [-864, -600],
        [450, 535],
        [-479, -370],
        [856, 573],
        [-549, 369],
        [529, -462],
        [-839, -856],
        [-515, -447],
        [652, 197],
        [-83, 345],
        [-69, 423],
        [310, -737],
        [78, -201],
        [443, 958],
        [-311, 988],
        [-477, 30],
        [-376, -153],
        [-272, 451],
        [322, -125],
        [-114, -214],
        [495, 33],
        [371, -533],
        [-393, -224],
        [-405, -633],
        [-693, 297],
        [504, 210],
        [-427, -231],
        [315, 27],
        [991, 322],
        [811, -746],
        [252, 373],
        [-737, -867],
        [-137, 130],
        [507, 380],
        [100, -638],
        [-296, 700],
        [341, 671],
        [-944, 982],
        [937, -440],
        [40, -929],
        [-334, 60],
        [-722, -92],
        [-35, -852],
        [25, -495],
        [185, 671],
        [149, -452],
    ]

    print(solution.minTimeToVisitAllPoints(points=points))


# #* Another Method with O(n^2):
# def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
#         min_time, i, last_point = 0, 0, points[len(points) - 1]
#         current_point = points[0]

#         while i < len(points) - 1:
#             if points[i] != last_point:
#                 while True:
#                     if current_point[0] == points[i + 1][0]:
#                         if current_point[1] == points[i + 1][1]:
#                             break
#                         elif current_point[1] < points[i + 1][1]:
#                             current_point[1] += 1
#                             min_time += 1

#                         else:
#                             current_point[1] -= 1
#                             min_time += 1

#                     elif current_point[0] < points[i + 1][0]:
#                         current_point[0] += 1
#                         if current_point[1] == points[i + 1][1]:
#                             min_time += 1
#                         elif current_point[1] < points[i + 1][1]:
#                             current_point[1] += 1
#                             min_time += 1

#                         else:
#                             current_point[1] -= 1
#                             min_time += 1

#                     else:
#                         current_point[0] -= 1
#                         if current_point[1] == points[i + 1][1]:
#                             min_time += 1
#                         elif current_point[1] < points[i + 1][1]:
#                             current_point[1] += 1
#                             min_time += 1

#                         else:
#                             current_point[1] -= 1
#                             min_time += 1

#                 i += 1

#             else:
#                 break

#         return min_time
