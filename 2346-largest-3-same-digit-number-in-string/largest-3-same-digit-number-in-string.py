class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_d = "-1"
        previous = ""
        count = 1
        for d in num:
            if d == previous:
                count += 1
                if count == 3:
                    largest_d = str(max(int(largest_d), int(d)))
            else:
                previous = d
                count = 1

        return "" if largest_d == "-1" else largest_d * 3