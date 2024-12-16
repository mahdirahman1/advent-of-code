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

def calculate_min(x,y, p_x, p_y):
    """
    Algebra approach, system of eqns only has one unique soln so no need to worry about findining min
    Ax*S + Bx+T = Px
    Ay*S + By*T = Py

    1 AxBy*S + BxBy*T = PxBy
    2 AyBxS + ByBx*T = PyBx

    1-2:
    AxBy*S - AyBxS = PxBy - PyBx
    S = PxBy - PyBx // AxBy - AyBx
    T = (PyBx - AyBxS)//ByBx

    """
    a_x, b_x = x
    a_y, b_y = y
    s = ((p_x*b_y) - (p_y*b_x))/((a_x*b_y) - (a_y*b_x))
    t = ((p_y*b_x) - (a_y*b_x*s))/(b_y*b_x)
    if (s % 1 == 0 and t % 1 == 0):
        return [int(s), int(t)]
    
    return False

def find_min_cost():
    res = 0
    for i in range(len(prizes)):
        target_x = prizes[i][0]
        target_y = prizes[i][1]
        x_options = x_buttons[i]
        y_options = y_buttons[i]
        presses = calculate_min(x_options, y_options, target_x, target_y)
        if presses:
            res += 3 * presses[0] + presses[1]
    
    return res

print(find_min_cost())