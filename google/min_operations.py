"""
increment_integer(n) -> +1
divib (if dib) by 2 -> 
result = c of divis to 
We have an integer (10) we need to build 2def: divide (if divisible by 2) by 2, and sum 1
smallest = result(25) +1 26 /2  13+ 1 -> 14 /2 7 + 1 //2 
always positive (for now)
"""


class SmallestNumberOfDivision:
    def __init__(self):
        self.operation_count = 0

    def increment_op(self, n):
        self.operation_count += 1
        return n + 1

    def divide_b_two(self, n):
        self.operation_count += 1
        return n / 2

    def verify_can_divide_by_two(self, n):
        if n % 2 == 0:
            return True
        return False

    def find_smallest_count(self, n):
        while n != 1:
            if self.verify_can_divide_by_two(n):
                n = self.divide_b_two(n)
            else:
                n = self.increment_op(n)
        return self.operation_count


def count_minimum_operations(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n += 1
        count += 1

    return count


sol = SmallestNumberOfDivision()
print(sol.find_smallest_count(25))  # Time Complexity: O(N) Space Complexity: O(1)
print(count_minimum_operations(25))  # Time Complexity: O(N) Space Complexity: O(1)
