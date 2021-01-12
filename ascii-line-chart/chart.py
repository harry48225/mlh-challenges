import math

class Chart(object):

    WIDTH = 50 # Make the chart 50 characters wide
    HEIGHT = 30

    def __init__(self, function, domain, height = HEIGHT, width = WIDTH):
        '''Pass a real valued function, domain should be a list representing an interval'''
        self.function = function

        if domain[1] <= domain[0]:

            print("domain error")

            return

        self.domain = domain

        self.height = height
        self.width = width

        self.compute_chart()

        self.print_chart()

    def compute_chart(self):
        ''' Constructs the array represented the graph that will be printed '''

        domain_increment = (self.domain[1] - self.domain[0])/self.width

        linspace = [self.domain[0] + x*domain_increment for x in range(self.width + 1)]
        # Work out the range of the function
        value_pairs = {}

        for point in linspace:
            
            value_pairs[str(point)] = round(self.function(point), 1)

        function_range = [min(value_pairs.values()), max(value_pairs.values())]

        # Now we have the domain and range.
        # Scale the y axis so that the range takes up all of the height

        chart = [[" " for _ in range(self.width + 1)] for _ in range(self.height + 1)]

        # Draw the x axis at the bottom

        chart[-1][0] = "+"

        for i in range(1, len(chart[-1])-2):

            chart[-1][i] = "-"

        

        # Draw the y axis at the left
        for i in range(2, len(chart)-1):
            chart[i][0] = "|"


        # Plot the values

        # Formula for the adjusted y coordinate
        adjust_y = lambda y : int(((y - function_range[0])/(function_range[1] - function_range[0])) * self.height)

        for x_index, value in enumerate(value_pairs.values()):

            # Add to the chart
            chart[self.height - adjust_y(value)][x_index] = "#"

    
        # Put the axis markers on
        chart[-1][-2] = ">"
        chart[-1][-1] = "x"
        chart[0][0] = "y"
        chart[1][0] = "^"
        self.chart = chart
        
    def print_chart(self):
        
        for row in self.chart:

            print("".join(row))


# Test

def f(x):
    return x*x

#domain = [int(input("Please enter the first point of the domain: ")), int(input("and the second: "))]
domain = [-10,10]
c = Chart(f, domain)
print("x^2")

c = Chart(math.sin, domain, height = 10)
print("sin(x)")


c = Chart(lambda x : (x-1)*(x-4)*(x+3), [-5,5])
print("(x-1)(x-4)(x+3)")