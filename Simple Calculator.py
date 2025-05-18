import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("360x640")
root.configure(bg="lightgray")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 30), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=27, padx=10, pady=(50, 20), sticky="we")

# History label
history_var = tk.StringVar()
history_label = tk.Label(root, textvariable=history_var, font=("Arial", 12), bg="lightgray", anchor='e')
history_label.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="we")

# Functions
def press(num):
    entry.insert(tk.END, str(num))

def clear():
    entry.delete(0, tk.END)
    history_var.set("")

def delete():
    entry.delete(len(entry.get()) - 1)

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        history_var.set(f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        history_var.set("Invalid Expression")

# Buttons layout
buttons = [
    [('AC', clear), ('DEL', delete), ('%', lambda: press('%')), ('/', lambda: press('/'))],
    [('7', lambda: press('7')), ('8', lambda: press('8')), ('9', lambda: press('9')), ('*', lambda: press('*'))],
    [('4', lambda: press('4')), ('5', lambda: press('5')), ('6', lambda: press('6')), ('-', lambda: press('-'))],
    [('1', lambda: press('1')), ('2', lambda: press('2')), ('3', lambda: press('3')), ('+', lambda: press('+'))],
    [('0', lambda: press('0')), ('.', lambda: press('.')), ('=', calculate), ('00', lambda: press('00'))]
]

# Create buttons
for i, row in enumerate(buttons):
    for j, (text, command) in enumerate(row):
        # Set background color conditionally
        if text == 'AC':
            bg_color = "#ff9999"  # Light red for AC
        elif text == 'DEL':
            bg_color = "#ffcc66"  # Orange-yellow for DEL
        else:
            bg_color = "white"    # Default for others

        btn = tk.Button(root, text=text, font=("Arial", 16), width=4, height=1,
                        command=command, bg=bg_color, relief=tk.RAISED, bd=2)
        btn.grid(row=i+2, column=j, padx=6, pady=6, sticky="nsew")

# Equal column/row distribution
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()