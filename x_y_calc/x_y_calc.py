def maph2(eqtn):
    print("Running maph2")
    import sympy

    x = -100
    y = -100
    while True:
        try:
            result = sympy.sympify(eqtn.replace('x', str(x)).replace('y', str(y)))
            eqtn2 = eqtn.replace('x', str(x)).replace('y', str(y)).replace('==', ' = ')
            if result is True:
                print(f"For x={x} and y={y} the equation: {eqtn2} evaluates to: {result}")
            x = round((x+0.1), 2)
            if x == 100:
                x = -100
                y = round((y+0.1), 2)
            if y == 100:
                break
        except:
            print("\n//\n\nError occurred...")
            break
    import os
    video_script_path = os.path.abspath("main_menu.py")
    os.system(f'python "{video_script_path}"')


def maph():
    
    import sympy

    print("Enter the equation:")
    eqtn = input("(Note, you have to specify multiplication as * and division as /)\n")
    eqtn = eqtn.replace('=', '==')
    multi2 =  eqtn.count("y")
    if multi2>0:
        return maph2(eqtn)
    x = -100

    while True:
        try:
            eqtn2 = eqtn.replace('x', str(x)).replace('==', ' = ')
            result = sympy.sympify(eqtn.replace('x', str(x)))
            if result is True:
                print(f"For x = {x}, in {eqtn2} the equation is true")
            x = round((x+0.1), 2)
            if x > 100:
                break
        except:
            break
    import os
    video_script_path = os.path.abspath("main_menu.py")
    os.system(f'python "{video_script_path}"')
    
if __name__ == "__main__":
    maph()