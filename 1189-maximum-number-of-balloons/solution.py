import math
from collections import Counter


class Solution:
    def max_number_of_balloons(self, text):
        texts = Counter(text)

        balloons = Counter('balloon')

        max_number = math.inf

        for c in balloons:
            max_number = min(max_number, texts[c] // balloons[c])

        return max_number
