import tkinter

# it creates the button layout on the screen
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", " "]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# Determines the colours of the calculator buttons and display
color_light_gray = "#D4D4D2"
color_black = "#1c1c1c"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

row_count = len(button_values)
column_count = len(button_values[0])

# Defines calculator variables
A = "0"
B = "0"
operator = None
running = True


# Its function is to clear the calculator
def clear_all():
    global A, B, operator

    A = "0"
    B = "0"
    operator = None
    label["text"] = "0"


# Remove .0 from whole numbers
def remove_zero_decimal(num):
    if num % 1 == 0:
        return str(int(num))
    return str(num)


# It makes the buttons functional
def button_clicked(value):
    global A, B, operator

    # AC, +/-, %
    if value in top_symbols:

        if value == "AC":
            clear_all()

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    # Operators
    elif value in right_symbols:

        # Equals
        if value == "=":

            if operator is not None:

                B = label["text"]

                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = numA + numB

                elif operator == "-":
                    result = numA - numB

                elif operator == "×":
                    result = numA * numB

                elif operator == "÷":

                    if numB == 0:
                        label["text"] = "Error"
                        clear_all()
                        return

                    result = numA / numB

                label["text"] = remove_zero_decimal(result)

                # Store result
                A = label["text"]
                B = "0"
                operator = None

        # Other operators
        else:
            A = label["text"]
            operator = value
            label["text"] = "0"

    # Numbers and decimal
    else:

        if value == ".":

            if "." not in label["text"]:
                label["text"] += "."

        elif value in "0123456789":

            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value



# Creates the calculator window

window = tkinter.Tk()

window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)


# Defines how the display should look like and where it should be placed
label = tkinter.Label(
    frame,
    text="0",
    anchor="e",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white,
    width=column_count
)

label.grid(
    row=0,
    column=0,
    columnspan=column_count,
    sticky="we"
)


# It creates buttons
row = 0

while row < row_count:

    column = 0

    while column < column_count:

        value = button_values[row][column]

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 45),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        # Button colours
        if value in top_symbols:

            button.config(
                foreground=color_black,
                background=color_light_gray
            )

        elif value in right_symbols:

            button.config(
                foreground=color_white,
                background=color_orange
            )

        else:

            button.config(
                foreground=color_white,
                background=color_dark_gray
            )

        button.grid(
            row=row + 1,
            column=column
        )

        column += 1

    row += 1


frame.pack()


#It Centres the window

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(
    f"{window_width}x{window_height}+{window_x}+{window_y}"
)

while running:

    try:
        window.update()
        window.update_idletasks()

    except tkinter.TclError:
        running = False


window.destroy()