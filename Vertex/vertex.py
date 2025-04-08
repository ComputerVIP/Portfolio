
def get_vertex_form(a, b, c):
    # Find h (x-coordinate of vertex): h = -b/(2a)
    h = -b / (2 * a)
    # Find k (y-coordinate of vertex): k = f(h)
    k = a * h**2 + b * h + c
    return h, k

def main():
    print('Quadratic Equation Converter')
    print('From: y = ax² + bx + c')
    print('To: y = (x ± h)² ± k')
    
    a = float(input("Enter a (coefficient of x²): "))
    b = float(input("Enter b (coefficient of x): "))
    c = float(input("Enter c (constant term): "))
    
    h, k = get_vertex_form(a, b, c)
    
    # Format the vertex form equation
    h_term = f"(x + {abs(h)})" if h < 0 else f"(x - {h})"
    k_term = f"+ {k}" if k > 0 else f"- {abs(k)}"
    
    print(f"\nStandard form: y = {a}x² + {b}x + {c}")
    print(f"Vertex form: y = {a}{h_term}² {k_term}")

if __name__ == '__main__':
    while True:
        try:
            main()
            again = input("\nConvert another equation? (y/n): ")
            if again.lower() != 'y':
                import os
                video_script_path = os.path.abspath("main_menu.py")
                os.system(f'python "{video_script_path}"')
                break
        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError:
            print("The coefficient 'a' cannot be zero in a quadratic equation.")
