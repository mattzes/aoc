import time

with open('./2024/14/input.txt', 'r') as file:
    raw_robots = file.read().splitlines()

STEPS = 10000
X_LENGTH = 101
Y_LENGTH = 103

class Robot():
    def __init__(self, config):
        positon, velocity = config.split(' ')
        positon = positon.split('=')[-1].split(',')
        velocity = velocity.split('=')[-1].split(',')
        self.positon = (int(positon[0]), int(positon[1]))
        self.velocity = (int(velocity[0]), int(velocity[1]))

    def step(self):
        self.positon = ((self.positon[0] + self.velocity[0]) % X_LENGTH, (self.positon[1] + self.velocity[1]) % Y_LENGTH)

robots = [Robot(raw_robot) for raw_robot in raw_robots]

for i in range(STEPS):
    co = [['.' for _ in range(X_LENGTH)] for _ in range(Y_LENGTH)]

    print(i + 1)
    
    for robot in robots:
        robot.step()
        co[robot.positon[1]][robot.positon[0]] = '#'
    
    for line in co:
        count = line.count('#')
        if count > 25:
            for l in co:
                print(''.join(l))

    time.sleep(0.02)