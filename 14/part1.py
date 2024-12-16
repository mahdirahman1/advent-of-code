positions = []
velocities = []

with open("input.txt", "r") as filename:
    for line in filename.readlines():
        line = line.rstrip()
        position, vel = line.split(" ")
        x = int(position.split("=")[1].split(",")[0])
        y = int(position.split("=")[1].split(",")[1])
        positions.append([x,y])
        vel_x = int(vel.split("=")[1].split(",")[0])
        vel_y = int(vel.split("=")[1].split(",")[1])
        velocities.append([vel_x, vel_y])

    filename.close()

width = 101
height = 103
time = 100
quadrant_count = [0] * 4

def add_to_quadrant(pos_x, pos_y):
    mid_x = width//2
    mid_y = height//2
    if pos_x < mid_x:
        # left half
        if pos_y < mid_y:
            quadrant_count[0] += 1
        elif pos_y > mid_y:
            quadrant_count[1] += 1

    elif pos_x > mid_x:
        # right half
        if pos_y < mid_y:
            quadrant_count[2] += 1
        elif pos_y > mid_y:
            quadrant_count[3] += 1


def calc_position(pos_x, pos_y, vel_x, vel_y):
    pos_x = (pos_x + (vel_x * time)) % width
    pos_y = (pos_y + (vel_y * time)) % height
    return [pos_x, pos_y]

for i in range(len(positions)):
    x,y = positions[i]
    vel_x, vel_y = velocities[i]
    x,y = calc_position(x,y,vel_x,vel_y)
    add_to_quadrant(x,y)

res = 1
for q in quadrant_count:
    res *= q

print(res)