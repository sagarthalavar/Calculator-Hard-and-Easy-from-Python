import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields for numbers
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Dropdown for selecting operation
operator = tk.StringVar(root)
operator.set('+')  # default value
operator_menu = tk.OptionMenu(root, operator, '+', '-', '*', '/')
operator_menu.pack()

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Display area for result
result_label = tk.Label(root)
result_label.pack()

# Start the main loop
root.mainloop()
