from tkinter import *

# Initialize the expression string
expression = ""

# Function to update the expression when a button is pressed
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression and display the result
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Create the main GUI window
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("270x150")

    # Create a text entry field for displaying the expression
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    # Create buttons for digits and arithmetic operations
    button1 = Button(gui, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='0', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    buttondot = Button(gui, text='.', fg='black', bg='red', command=lambda: press("."), height=1, width=7)
    button0.grid(row=5, column=1)


    # ... (similarly create buttons for other digits and operations)

    # Create the "+" button
    plus = Button(gui, text='+', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=4)

    minus= Button(gui, text='+', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=2, column=5)

    divide = Button(gui, text='+', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=3, column=4)

    multiply = Button(gui, text='+', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=3, column=5)

    equalto = Button(gui, text='+', fg='black', bg='red', command=lambda: press("="), height=1, width=7)
    equalto.grid(row=4, column=4)

    # Add more buttons for other arithmetic operations

    # Start the GUI event loop
    gui.mainloop()
