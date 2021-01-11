import math
# Uses a logistic map with r ~ 3.5699456
# x_{n+1} = 3.5699456(x_n)(1-x_n)


class Random(object):

    def __init__(self, seed):
        # f(x) = arctan(x) / pi
        # Maps R onto (0, 1) so we can use this to normalise our seed

        seed = math.atan(seed) / math.pi

        self.current_number = seed

    def generate_number(self):
        ''' Returns a number between 0 and 9 inclusive '''

        self.current_number = (3.5699456)*(self.current_number)*(1 - self.current_number)

        return int(str(self.current_number)[-1])


# Example

r = Random(123)
p = Random(12345)
for i in range(10):
    print("seed: 123, number: {}, seed: 12345: number: {}".format(r.generate_number(), p.generate_number()))