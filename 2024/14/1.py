with open('./2024/14/input.txt', 'r') as file:
    raw_robots = file.read().splitlines()

STEPS = 100
X_LENGTH = 101
Y_LENGTH = 103

class Robot():
    def __init__(self, config):
        positon, velocity = config.split(' ')
        positon = positon.split('=')[-1].split(',')
        velocity = velocity.split('=')[-1].split(',')
        self.positon = (int(positon[0]), int(positon[1]))
        self.velocity = (int(velocity[0]), int(velocity[1]))
    
    def move(self):
        x = (self.positon[0] + self.velocity[0] * STEPS) % X_LENGTH
        y = (self.positon[1] + self.velocity[1] * STEPS) % Y_LENGTH
        self.positon = (x, y)

Q1 = ((0, 0), (X_LENGTH // 2 - 1, Y_LENGTH // 2 - 1))
Q2 = ((X_LENGTH // 2 + 1, 0), (X_LENGTH - 1, Y_LENGTH // 2 - 1))
Q3 = ((0, Y_LENGTH // 2 + 1), (X_LENGTH // 2 - 1, Y_LENGTH - 1))
Q4 = ((X_LENGTH // 2 + 1, Y_LENGTH // 2 + 1), (X_LENGTH - 1, Y_LENGTH - 1))

quadrents = [Q1, Q2, Q3, Q4]
quadrents_count = [0, 0, 0, 0]

robots = []
for raw_robot in raw_robots:
    robot = Robot(raw_robot)
    robots.append(robot)
    
    robot.move()

    for i, Q in enumerate(quadrents):
        if Q[0][0] <= robot.positon[0] <= Q[1][0] and Q[0][1] <= robot.positon[1] <= Q[1][1]:
            quadrents_count[i] += 1
            break

print(quadrents_count[0] * quadrents_count[1] * quadrents_count[2] * quadrents_count[3])