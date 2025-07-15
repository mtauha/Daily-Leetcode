class Solution:
    def isValid(self, word: str) -> bool:
        pattern = r"^(?=.*[aeiouAEIOU])(?=.*[A-Za-z])(?=.*[^aeiouAEIOU0-9])[A-Za-z0-9]{3,}$"
        return True if re.fullmatch(pattern, word) else False
