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
                x = int(r.split(",")[0].split("=")[1]) + 10000000000000
                y = int(r.split(",")[1].split("=")[1]) + 10000000000000
                prizes.append([x,y])
                x_button = []
                y_button = []
    
    filename.close()

def calculate_min(target_x, options_x, target_y, options_y):
    x1,x2 = max(options_x), min(options_x)
    for x1_presses in range(target_x//x1, -1, -1):
        left = target_x - (x1 * x1_presses)
        if left % x2 == 0:
            if options_x[0] == x1:
                # p1 is a
                if check_y_presses(target_y, options_y, x1_presses, left//x2):
                    return [x1_presses, left//x2]
            else:
                # p2 is a
                if check_y_presses(target_y, options_y, left//x2, x1_presses):
                    return [left//x2, x1_presses]

    return False

def check_y_presses(target, options, a_presses, b_presses):
    return options[0] * a_presses + options[1] * b_presses == target

def find_min_cost():
    res = 0
    for i in range(len(prizes)):
        target_x = prizes[i][0]
        target_y = prizes[i][1]
        x_options = x_buttons[i]
        y_options = y_buttons[i]
        presses = calculate_min(target_x, x_options, target_y, y_options)
        if presses:
            res += 3 * presses[0] + presses[1]
    
    return res
        
print(find_min_cost())