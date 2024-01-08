import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Input Bar Example")

# Function to get the value from the input bar
def get_input(event=None):
    user_input1 = entry1.get()
    user_input1_int = int(user_input1)
    hidden_text1 = '*' * len(user_input1)
    label_hidden1.config(text=hidden_text1)
    print("User Input1:", user_input1)
    return user_input1_int  # Return user_input1_int

def new_input(event=None):
    user_input2 = entry2.get()
    user_input2_int = int(user_input2)
    hidden_text2 = '*' * len(user_input2)
    label_hidden2.config(text=hidden_text2)
    print("User Input2:", user_input2)
    return user_input2_int  # Return user_input2_int

def add_data():
    # Get the input values by calling the functions
    user_input1_int = get_input()
    user_input2_int = new_input()

    # Perform addition using the obtained input values
    if user_input1_int is not None and user_input2_int is not None:
        result = user_input1_int + user_input2_int
        print("Addition of both are:", result)

# Create Entry widgets
entry1 = tk.Entry(root, show='*')
entry1.pack(padx=20)
entry2 = tk.Entry(root, show='*')  # Show asterisks for input in entry2 as well
entry2.pack(padx=20, pady=20)

label_hidden1 = tk.Label(root, text='', width=30)
label_hidden1.pack()
label_hidden2 = tk.Label(root, text='', width=30)
label_hidden2.pack()

# Create buttons to get the input and perform addition
button1 = tk.Button(root, text="Show 1st integer", command=get_input)
button2 = tk.Button(root, text="Show 2nd integer", command=new_input)
button3 = tk.Button(root, text="Add Both", command=add_data)
button1.pack(pady=5)
button2.pack(pady=10)
button3.pack(pady=10)

entry1.bind('<KeyRelease>', get_input)
entry2.bind('<KeyRelease>', new_input)

# Run the main Tkinter loop
root.mainloop()
