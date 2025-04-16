import tkinter as tk # Importing the tkinter library for GUI creation(the only library you need)
from tkinter import ttk # Importing the ttk module from tkinter for themed widgets

def handling_button_click(clicked_button_txt):
    current_text = result_var.get() # Get the current text from the result variable

    if clicked_button_txt == "=":
        try:
            expression = current_text.replace("x", "*").replace("÷", "/") # Replace 'x' with '*' and '÷' with '/'
            result = eval(expression) # Evaluate the expression

            if result.is_integer():
                result = int(result)

            result_var.set(result) # Set the result in the result variable
        except Exception as e:
            result_var.set("ERROR")

    elif clicked_button_txt == "C":
        result_var.set("")
    elif clicked_button_txt == "%":

        try:
            current_text = float(current_text)
            result_var.set(current_text / 100) # Calculate percentage
        except ValueError:
            result_var.set("ERROR")

    elif clicked_button_txt == "±":
        try:
            current_text = float(current_text)
            result_var.set(-current_text) # Negate the current value
        except ValueError:
            result_var.set("ERROR")
    else:
        result_var.set(current_text + clicked_button_txt)

        ROOT = tk.Tk() # Create the main window
        ROOT.title("Simple Calculator") # Set the title of the window

        result_var = tk.StringVar() # Create a StringVar to hold the result
        result_entry = ttk.Entry(ROOT, textvariable=result_var, font=("Arial", 24), justify="right") # Create an entry widget for the result
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew") # Place the entry widget in the grid

        buttons = [
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
        ]
        # Create buttons and place them in the grid

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16), height=4, width=10) # Configure the button style

        for button_info in buttons:
            button_text, row, col = button_info[:3]
            colspan = button_info[3] if len(button_info) > 3 else 1
            button = ttk.button(root, text=button_text, commnand=lambda txt=button_text: handling_button_click(txt), style="TButton")
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)
            # Place the button in the grid with padding
        
        for i in range(6):
            ROOT.grid_rowconfigure(i, weight=1)
        for j in range(4):
            ROOT.grid_columnconfigure(j, weight=1)
        # Configure the grid to expand properly

        width = 500
        height = 600
        ROOT.geometry(f"{width}x{height}") # Set the window size

        root.resizable(False, False) # Make the window non-resizable

        root.bind("<Return>", lambda event: handling_button_click("=")) # Bind the Enter key to the equals button
        root.bind('<backspace>', lambda event: handling_button_click("C")) # Bind the Backspace key to the clear button

        root.mainloop() # Start the main event loop




