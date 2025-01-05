from typing import List
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
            You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

            Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

            Return the final string after all such shifts to s are applied.
        """
        n = len(s)
        shift_arr = np.zeros(n + 1, dtype=int)

        for start, end, direction in shifts:
            shift_arr[start] += 1 if direction == 1 else -1
            shift_arr[end + 1] -= 1 if direction == 1 else -1
        
        shift_arr = np.cumsum(shift_arr[:-1])

        def shift_char(c, shift):
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        
        return ''.join(shift_char(c, shift) for c, shift in zip(s, shift_arr))
