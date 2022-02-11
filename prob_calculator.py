import random


class Hat:
    def __init__(self, *args):
        self.content = []
        for elem in args:
            elem = elem.split('=')
            for i in range(int(elem[1])):
                self.content.append(elem[0])

    def draw(self, number):
        if number < len(self.content):
            balls = []
            for i in range(number):
                balls.append(random.choice(self.content))
            return balls
        else:
            return self.content


def experiment(_hat, expected_balls, num_balls_drawn, num_experiments):
    n = 0
    m = 0
    eballs = []
    keys = list(expected_balls.keys())
    values = list(expected_balls.values())
    j = 0
    for value in values:
        for i in range(value):
            eballs.append(keys[j])
        j += 1
    for i in range(num_experiments):
        n += 1
        balls = _hat.draw(num_balls_drawn)
        if all(item in balls for item in eballs):
            m += 1
    return m / n


hat = Hat('black=6', 'red=4', 'green=3')
probability = experiment(_hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)
