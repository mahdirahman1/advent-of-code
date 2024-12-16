x_buttons = []
y_buttons = []
prizes = []
x_button = []
y_button = []
with open("input.txt", "r") as filename:

    for line in filename.readlines():
        line = line.rstrip()
        if line != "":
            l,r = line.split(":")
            if "Button" in l:
                x = int(r.split(",")[0].split("+")[1])
                y = int(r.split(",")[1].split("+")[1])
                x_button.append(x)
                y_button.append(y)
            else:
                x_buttons.append(x_button)
                y_buttons.append(y_button)
                x = int(r.split(",")[0].split("=")[1])
                y = int(r.split(",")[1].split("=")[1])
                prizes.append([x,y])
                x_button = []
                y_button = []
    
    filename.close()

def calculate_min(target, options):
    p1,p2 = max(options), min(options)
    for p1_presses in range(target//p1, -1, -1):
        left = target - (p1 * p1_presses)
        if left % p2 == 0:
            if options[0] == p1:
                # p1 is a
                return [p1_presses, left//p2]
            else:
                # p2 is a
                return [left//p2, p1_presses]

    return False

def check_y_presses(target, options, a_presses, b_presses):
    pass

def find_min_cost():
    res = 0
    for i in range(len(prizes)):
        target_x = prizes[i][0]
        target_y = prizes[i][1]
        x_options = x_buttons[i]
        y_options = y_buttons[i]
        x_presses = calculate_min(target_x, x_options)
        if x_presses:
            print(x_presses)

find_min_cost()