import math
# Uses a logistic map with r = 3.9
# x_{n+1} = 3.9(x_n)(1-x_n)


class Random(object):

    def __init__(self, seed):
        # f(x) = arctan(x) / pi
        # Maps R onto (0, 1) so we can use this to normalise our seed

        seed = math.atan(seed) / math.pi

        self.current_number = seed

    def generate_number(self):
        ''' Returns a number between 0 and 9 inclusive '''

        self.current_number = (3.9)*(self.current_number)*(1 - self.current_number)
        return int(str(self.current_number)[3]) # Take the fourth digit


# Example

r = Random(234)

randoms_generated = [0 for i in range(10)]

for _ in range(100000):

    num = r.generate_number()

    randoms_generated[num - 1] += 1

print(randoms_generated)
