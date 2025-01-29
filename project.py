import tkinter as tk 
#window 
window= tk.Tk()
window.geometry('600x565')
#window name 
window.title("Calculator")

#widgets 
#function to to eval expression and display 
def evaluate():
    exp = eval(entry.get())
    entry.delete(0, tk.END)
    entry .insert(tk.END, str(exp))



def clear():
    entry.delete(0,tk.END)

#entry widget 
entry = tk.Entry(window, width=15, borderwidth=3,  font='Arial, 24')
entry.grid(row=0, column=0, columnspan=5)

#button press 

def Squash(key):
    curr = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, curr + str(key))




#button labels for app
buttons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
('4', 2, 0), ('5', 2, 1), ('6',2, 2), ('-', 2, 3),
('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('/', 3, 3),
('0', 4, 0), ('AC', 4, 1), ('+', 4, 2), ('=', 4, 3)]

#add buttons to grid 

for(text, row, col,) in buttons :
    if text == '=':
        button = tk.Button(window, text=text, width=10, height=4, font=("Arial", 19), command=evaluate)
    elif text == 'AC':
        button = tk.Button(window, text=text, width=10, height=4, font=("Arial", 19), command=clear )
    else:
        button = tk.Button(window, text=text, width=10, height=4, font=("Arial", 19), command= lambda t=text :Squash(t) ) 
    button.grid(row=row, column=col)   

tk.mainloop()


