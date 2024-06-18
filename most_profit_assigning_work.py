"""Description:
    You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

    difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
    worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
    Every worker can be assigned at most one job, but one job can be completed multiple times.

    For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
    Return the maximum profit we can achieve after assigning the workers to the jobs.
"""

class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        profits = 0
        current_profit = 0
        worker.sort()
        job_no = 0

        for ability in worker:
            while job_no < len(jobs) and ability >= jobs[job_no][0]:
                current_profit = max(current_profit, jobs[job_no][1])
                job_no+=1
            
            profits += current_profit

        return profits

sol = Solution()
difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]
print(sol.maxProfitAssignment(difficulty,profit,worker))
