from guizero import *


def run(master):
    win = Window(master, title="Calculator")

    equation = []

    txtout = Text(
        win,
        text="|CALCULATOR|",
        size=20
    )

    def update_display():
        txtout.value = "".join(equation)

    def make_num(num):
        def handler():
            equation.append(str(num))
            update_display()

        return handler

    def make_sym(sym):
        def handler():
            equation.append(sym)
            update_display()

        return handler

    def parse_equation(equ):
        str1 = ""
        str2 = ""
        operator = ""

        for char in equ:
            if char in ["+", "-", "÷", "×"]:
                operator = char

            elif operator == "":
                str1 += char

            else:
                str2 += char

        try:
            n1 = float(str1)
            n2 = float(str2)

            if operator == "+":
                return n1 + n2

            elif operator == "-":
                return n1 - n2

            elif operator == "×":
                return n1 * n2

            elif operator == "÷":
                if n2 == 0:
                    return "|CANNOT DIVIDE BY ZERO|"

                return n1 / n2

            return "|ERROR|"

        except ValueError:
            return "|INVALID EQUATION|"

    def calculate():
        result = parse_equation(equation)

        equation.clear()
        equation.append(str(result))

        update_display()

    def clear():
        equation.clear()
        txtout.value = "|CALCULATOR|"

    # Calculator button grid
    buttons = [
        ("1", 0, 0),
        ("2", 1, 0),
        ("3", 2, 0),
        ("+", 3, 0),

        ("4", 0, 1),
        ("5", 1, 1),
        ("6", 2, 1),
        ("-", 3, 1),

        ("7", 0, 2),
        ("8", 1, 2),
        ("9", 2, 2),
        ("÷", 3, 2),

        ("=", 0, 3),
        ("0", 1, 3),
        ("C", 2, 3),
        ("×", 3, 3),

        (".", 1, 4),
        ("CLOSE", 2, 4)
    ]

    button_box = Box(
        win,
        layout="grid"
    )

    for text, x, y in buttons:

        if text.isdigit():
            command = make_num(int(text))

        elif text == "C":
            command = clear

        elif text == "=":
            command = calculate

        elif text == "CLOSE":
            command = win.destroy

        else:
            command = make_sym(text)

        PushButton(
            button_box,
            text=text,
            grid=[x, y],
            width=8,
            height=3,
            command=command
        )


if __name__ == "__main__":
    app = App()
    run(app)
    app.display()