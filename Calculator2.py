import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    else:
        entry_var.set(current_text + button_text)


root = tk.Tk()
root.title("Zander Calculator")
root.resizable(False, False)
root.geometry("")
root.configure(bg="#262626", padx=10, pady=10)



# for input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", border=5)
entry.grid(row=0, column=0, columnspan=4, ipadx=20, ipady=0, pady=10)


buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('C','0','=','+')
]



for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text in ['C','=','/','*','-','+']:
            button = tk.Button(root, text=text, font=("Roboto", 18), width=3, height=1, bg="orange", fg="#262626", relief='raised', border=10, command=lambda t=text: on_click(t))
            button.grid(row=i+1, column=j, padx=5, pady=5)
        else:
            button = tk.Button(root, text=text, font=("Roboto", 18), width=3, height=1, bg="white", fg="#262626", relief='raised', border=10, command=lambda t=text: on_click(t))
            button.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()

