from math import sqrt as math_sqrt
from sys import stdout
from time import sleep
from numpy import roots

# import keyboard

# define outside to retain values and keep recursion
a_Value, b_Value, c_Value, d_Value, e_Value = None, None, None, None, None
plusminus = "±"

red = "\x1b[38;5;196m"
reset = "\x1b[38;5;15m"
green = "\x1b[38;5;46m"
teal = "\x1b[38;5;87m"
bye_color = "\x1b[38;5;220m"
choice_color = "\x1b[38;5;11m"
input_color = "\x1b[38;5;5m"
soln_color = "\x1b[38;5;42m"
use_bubble_text = True


class QuadraticSolver:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Custom square root function to handle imaginary numbers, piggybacks off of math.sqrt
    def sqrt(self, x, first_part) -> complex:

        # both are represented as complex for the sake of simplicity
        if x >= 0:
            # if x is greater than zero than the output will be normal
            return complex(math_sqrt(x) / (2 * self.a), 0)
        else:
            # if x is less than zero than the output will be imaginary so evauluate the root by making it positive again then convert to imag. by using the builtin complex function
            return complex(first_part, round(math_sqrt(-x) / (2 * self.a), 12))

    # Calculates x when the plus minus represents a plus
    def calculate_positive_root(self):
        # get the first part, -b/2a
        first_part = -self.b / (2 * self.a)
        # get the square root part
        sqrt_ans = self.sqrt(self.b ** 2 - (4 * self.a * self.c), first_part)
        # if imaginary then represent as imaginary in a string else return as normal
        if sqrt_ans.imag != 0:
            next_part = f"{str(sqrt_ans).replace('j', 'i').replace('+', ' + ').replace('(', '').replace(')', '')}"
            return (f"{next_part}", sqrt_ans)
        else:
            return (round((-self.b / (2 * self.a)) + sqrt_ans.real,
                          12), sqrt_ans)

    # Calculates x when the plus minus represents a minus
    def calculate_negative_root(self):
        # get the first part of the formula, -b/2a
        first_part = -self.b / (2 * self.a)
        # figure out the square root part
        sqrt_ans = self.sqrt(self.b ** 2 - (4 * self.a * self.c), first_part)
        # if it is imaginary represent it as imaginary in a string else return the normal version
        if sqrt_ans.imag != 0:

            next_part = f"{str(sqrt_ans).replace('j', 'i').replace('+', ' - ')}".replace(
                '(', '').replace(')', '')
            return f"{next_part}"
        else:
            return round((-self.b / (2 * self.a)) - sqrt_ans.real, 12)


def is_numeric(string):
    try:
        return float(string)  # True if string is a number contains a dot
    except:  # String is not a number
        return False


def write_correct_info_placed(ltr):
    n = None
    if ltr == 'a':
        n = a_Value
    elif ltr == 'b':
        n = b_Value
    elif ltr == 'c':
        n = c_Value
    elif ltr == 'd':
        n = d_Value
    elif ltr == 'e':
        n = e_Value
    clear_top_line()
    print(f"{green}What is the [{ltr}] value of the equation?: {n}{reset}")


def clear_top_line():
    stdout.write("\033[1A\033[2K")


preview_color = "\x1b[38;5;192m"


def replace_filler_line_quad(ltr):
    if ltr == 'a':
        stdout.write("\033[1A" * 3)
        print(f"{preview_color}{a_Value}x² + bx + c = 0{reset}")
        stdout.write("\033[1B" * 2)
    elif ltr == 'b':
        stdout.write("\033[1A" * 4)
        print(f"{preview_color}{a_Value}x²{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x + c = 0{reset}")
        stdout.write("\033[1B" * 3)
    elif ltr == 'c':
        stdout.write("\033[1A" * 5)
        print(
            f"{preview_color}{a_Value}x²{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x{' + ' if c_Value > 0 else ' - '}{abs(c_Value)} = 0{reset}")
        stdout.write("\033[1B" * 4)


def replace_filler_line_cube(ltr):
    if ltr == 'a':
        stdout.write("\033[1A" * 3)
        print(f"{preview_color}{a_Value}x³ + bx² + cx + d = 0{reset}")
        stdout.write("\033[1B" * 2)
    elif ltr == 'b':
        stdout.write("\033[1A" * 4)
        print(f"{preview_color}{a_Value}x³{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x² + cx + d = 0{reset}")
        stdout.write("\033[1B" * 3)
    elif ltr == 'c':
        stdout.write("\033[1A" * 5)
        print(
            f"{preview_color}{a_Value}x³{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x²{' + ' if c_Value > 0 else ' - '}{abs(c_Value)}x + d = 0{reset}")
        stdout.write("\033[1B" * 4)
    elif ltr == 'd':
        stdout.write("\033[1A" * 6)
        print(
            f"{preview_color}{a_Value}x³{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x²{' + ' if c_Value > 0 else ' - '}{abs(c_Value)}x{' + ' if d_Value > 0 else ' - '}{abs(d_Value)} = 0{reset}")
        stdout.write("\033[1B" * 5)


def replace_filler_line_quartic(ltr):
    if ltr == 'a':
        stdout.write("\033[1A" * 3)
        print(f"{preview_color}{a_Value}x⁴ + bx³ + cx² + dx + e = 0{reset}")
        stdout.write("\033[1B" * 2)
    elif ltr == 'b':
        stdout.write("\033[1A" * 4)
        print(f"{preview_color}{a_Value}x⁴{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x³ + cx² + dx + e = 0{reset}")
        stdout.write("\033[1B" * 3)
    elif ltr == 'c':
        stdout.write("\033[1A" * 5)
        print(
            f"{preview_color}{a_Value}x⁴{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x³{' + ' if c_Value > 0 else ' - '}{abs(c_Value)}x² + dx + e = 0{reset}")
        stdout.write("\033[1B" * 4)
    elif ltr == 'd':
        stdout.write("\033[1A" * 6)
        print(
            f"{preview_color}{a_Value}x⁴{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x³{' + ' if c_Value > 0 else ' - '}{abs(c_Value)}x²{' + ' if d_Value > 0 else ' - '}{abs(d_Value)}x + e = 0{reset}")
        stdout.write("\033[1B" * 5)
    elif ltr == 'e':
        stdout.write("\033[1A" * 7)
        print(
            f"{preview_color}{a_Value}x⁴{' + ' if b_Value > 0 else ' - '}{abs(b_Value)}x³{' + ' if c_Value > 0 else ' - '}{abs(c_Value)}x²{' + ' if d_Value > 0 else ' - '}{abs(d_Value)}x{' + ' if e_Value > 0 else ' - '}{abs(e_Value)} = 0{reset}")
        stdout.write("\033[1B" * 6)


def get_letter_input(ltr, d=2):
    global a_Value, b_Value, c_Value, d_Value, e_Value
    o = None
    n = None
    if ltr == 'a':
        o = a_Value
    elif ltr == 'b':
        o = b_Value
    elif ltr == 'c':
        o = c_Value
    elif ltr == 'd':
        o = d_Value
    elif ltr == 'e':
        o = e_Value
    if o is None:
        n = input(f"{teal}What is the [{ltr}] value of the equation?: {input_color}")
        n = 1.0 if n == "" else float(n)
        if ltr == 'a' and n == 0:
            raise ValueError
        if ltr == 'a':
            a_Value = n
        elif ltr == 'b':
            b_Value = n
        elif ltr == 'c':
            c_Value = n
        elif ltr == 'd':
            d_Value = n
        elif ltr == 'e':
            e_Value = n
        write_correct_info_placed(ltr)
        if d == 2:
            replace_filler_line_quad(ltr)
        elif d == 3:
            replace_filler_line_cube(ltr)
        elif d == 4:
            replace_filler_line_quartic(ltr)


def solving_suspense(do_extra=False):
    # cool waiting stuff
    # for i in range(150):
    #     keyboard.block_key(i)
    print(
        f"\x1b[38;5;5m\nThank you! Please do not press any keys while the equation is being solved to prevent issues.{reset}")
    sleep(1)
    print(f"{choice_color}Solving")
    for i in range(2):
        sleep(1)
        clear_top_line()
        print("Solving" + (i + 1) * ".")
    sleep(1)
    clear_top_line()
    print(f"Solving...{reset}")
    sleep(1)
    clear_top_line()
    clear_top_line()
    if do_extra:
        clear_top_line()
    # for i in range(150):
    #     keyboard.unblock_key(i)


def format_output_from_np(s):
    final_str = []
    for i in s:
        if i.imag == 0:
            final_str.append(round(i.real, 5))
    final_str.sort()
    for i in s:
        if i.imag != 0:
            j = complex(round(i.real, 5), round(i.imag, 5))
            final_str.append(str(j).replace("j", "i").replace(")", "").replace("(", ""))
    return final_str


# Main function for quadratic
def math_quadratic():
    global a_Value, b_Value, c_Value
    try:
            # inputs
        get_letter_input('a')
        get_letter_input('b')
        get_letter_input('c')

        solving_suspense(True)
        q: QuadraticSolver = QuadraticSolver(a_Value, b_Value, c_Value)
        # get the positive and negative roots
        outP = q.calculate_positive_root()
        outN = q.calculate_negative_root()
        print(f"{soln_color}\nx = {outP[0]}, {outN}")
        # write the output in plus-minus form
        if outP[1].imag != 0:
            print(
                f"Also written as: x = {-b_Value / (2 * a_Value)} {plusminus} {outP[1].imag}i"
            )
        else:
            print(
                f"Also written as: x = {-b_Value / (2 * a_Value)} {plusminus} {outP[1].real}"
            )
        # restart with another function
        a_Value, b_Value, c_Value = None, None, None
        sleep(1)
        print(f"\n{choice_color}Quadratic successfully solved! Going to menu...\n")
        sleep(1)
        clear_top_line()
        clear_top_line()
        menu()

    except ValueError:
        # figure out which input the user goofed on
        if not is_numeric(a_Value):
            a_Value = None
        if not is_numeric(b_Value):
            b_Value = None
        if not is_numeric(c_Value):
            c_Value = None
        clear_top_line()
        print(f"{red}Invalid input, please try again.{reset}", end="\r")
        sleep(1)
        math_quadratic()


# main cubic function
def math_cubic():
    global a_Value, b_Value, c_Value, d_Value
    try:
        get_letter_input('a', 3)
        get_letter_input('b', 3)
        get_letter_input('c', 3)
        get_letter_input('d', 3)

        solving_suspense()

        sol = roots([a_Value, b_Value, c_Value, d_Value])
        final_str = format_output_from_np(sol)
        print(f"{soln_color}x = {', '.join(str(o) for o in final_str)}")

        a_Value, b_Value, c_Value, d_Value = None, None, None, None
        sleep(1)
        print(f"\n{choice_color}Cubic successfully solved! Going to menu...\n")
        sleep(1)
        clear_top_line()
        clear_top_line()
        menu()
    except ValueError:
        # figure out which input the user goofed on
        if not is_numeric(a_Value):
            a_Value = None
        if not is_numeric(b_Value):
            b_Value = None
        if not is_numeric(c_Value):
            c_Value = None
        if not is_numeric(d_Value):
            d_Value = None
        clear_top_line()
        print("Invalid input, please try again.", end="\r")
        sleep(1)
        math_cubic()


# main quartic function
def math_quartic():
    global a_Value, b_Value, c_Value, d_Value, e_Value
    try:
        get_letter_input('a', 4)
        get_letter_input('b', 4)
        get_letter_input('c', 4)
        get_letter_input('d', 4)
        get_letter_input('e', 4)

        solving_suspense()
        sol = roots([a_Value, b_Value, c_Value, d_Value, e_Value])
        final_str = format_output_from_np(sol)

        print(f"{soln_color}x = {', '.join(str(o) for o in final_str)}")

        a_Value, b_Value, c_Value, d_Value, e_Value = None, None, None, None, None
        sleep(1)
        print(f"\n{choice_color}Quartic successfully solved! Going to menu...\n")
        sleep(1)
        clear_top_line()
        clear_top_line()
        menu()
    except ValueError:
        # figure out which input the user goofed on
        if not is_numeric(a_Value):
            a_Value = None
        if not is_numeric(b_Value):
            b_Value = None
        if not is_numeric(c_Value):
            c_Value = None
        if not is_numeric(d_Value):
            d_Value = None
        if not is_numeric(e_Value):
            e_Value = None
        clear_top_line()
        print("Invalid input, please try again.", end="\r")
        sleep(1)
        math_quartic()


if use_bubble_text:
    print(f"\x1b[38;5;39m" + fr'''
   ___                     _                                  _                                               _                                   _    _       
  / _ \  _   _   __ _   __| | _ __  ___           ___  _   _ | |__    ___           __ _  _   _   __ _  _ __ | |_  ___          _ __ ___    __ _ | |_ (_)  ___ 
 | | | || | | | / _` | / _` || '__|/ _ \  _____  / __|| | | || '_ \  / _ \  _____  / _` || | | | / _` || '__|| __|/ _ \  _____ | '_ ` _ \  / _` || __|| | / __|
 | |_| || |_| || (_| || (_| || |  | (_) ||_____|| (__ | |_| || |_) || (_) ||_____|| (_| || |_| || (_| || |   | |_| (_) ||_____|| | | | | || (_| || |_ | || (__ 
  \__\_\ \__,_| \__,_| \__,_||_|   \___/         \___| \__,_||_.__/  \___/         \__, | \__,_| \__,_||_|    \__|\___/        |_| |_| |_| \__,_| \__||_| \___|
                                                                                      |_|                                                                      
''')
else:
    print("\x1b[38;5;39m\n------------------------\nQuadro-cubo-quarto-matic\n------------------------\n")
print("Made by Akshar Desai\n")
print(f"{choice_color}Welcome!")
print(f"This program is designed to solve quadratic, cubic, and quartic equations. Ctrl+C or Ctrl+D to exit.")
print(f"Any input that is not entered will default to one.{reset}\n")


def menu():
    try:

        choice = input(
            f"{teal}What would you like to solve?{choice_color}\n1: Quadratic ({teal}ax²+bx+c=0{choice_color})\n2: Cubic ({teal}"
            f"ax³+bx²+cx+d=0{choice_color})\n3: Quartic ({teal}ax⁴+bx³+cx²+dx+e=0{choice_color})\n{input_color}")
        if not choice.isnumeric():
            print(f"{red}Please restart the program and enter a number.{reset}")
        else:
            if int(choice) == 1:
                print(f"\n\x1b[38;5;226mQuadratic selected{reset}\n")
                sleep(0.5)
                print(f"{preview_color}Equation Preview:\nax² + bx + c = 0\n")
                math_quadratic()
            elif int(choice) == 2:
                print(f"\n\x1b[38;5;226mCubic selected{reset}\n")
                sleep(0.5)
                print(f"{preview_color}Equation Preview:\nax³ + bx² + cx + d = 0\n")
                math_cubic()
            else:
                print(
                    f"\n\x1b[38;5;226mQuartic selected{' (values above three direct to this solver)' if int(choice) > 3 else ''}{reset}\n")
                sleep(0.5)
                print(f"{preview_color}Equation Preview:\nax⁴ + bx³ + cx² + dx + e = 0\n")
                math_quartic()
    except (KeyboardInterrupt, EOFError):
        print('\n')
        print(f"{bye_color}Goodbye!")


menu()
