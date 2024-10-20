"""
n-1 + n-2
Max =< 4000000
sum(n % 1 == 0)
"""

class Fibonacci:
    def __init__(self):
        self.scale = [0, 1, 1, 2, 3, 5]
        self.max_reached = False

    def sum_value_scale(self):
        if self.scale[-1] + self.scale[-2] > 4000000:
            self.max_reached = True
            return
        self.scale.append((self.scale[-1] + self.scale[-2]))

    def generate_scale(self):
        while not self.max_reached:
            self.sum_value_scale()

    def sum_evens(self):
        total = 0
        for n in self.scale:
            if n % 2 == 1:
                total = total + n
        return total
    
    def run(self):
        self.generate_scale()
        value = self.sum_evens()
        return value
    
fibonnaci = Fibonacci()
print(fibonnaci.run())