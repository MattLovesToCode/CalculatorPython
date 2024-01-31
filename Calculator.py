import tkinter as tk

def button_click(symbol):
    if symbol == 'C':
        display.delete(0, tk.END)
    elif symbol == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, symbol)

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_num = 1
col_num = 0
for button_symbol in buttons:
    tk.Button(root, text=button_symbol, padx=20, pady=20, command=lambda symbol=button_symbol: button_click(symbol)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
