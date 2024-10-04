class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
            You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
            The chemistry of a team is equal to the product of the skills of the players on that team.
            Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
        """
        skill.sort()
        n = len(skill)
        totalChemistry = 0
        teams = defaultdict(list)
        for i in range(n//2):
            teams[i].append(skill[i] + skill[n-1 - i])
            teams[i].append(skill[i] * skill[n-1 - i])
        
        check = set()
        for i in teams.values():
            check.add(i[0])
            totalChemistry += i[1]
        if len(check) > 1:
            return -1

        return totalChemistry
