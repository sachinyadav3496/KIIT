
import tkinter
import random

colors = [ 'red', 'green', 'blue', 'cyan', 'magenta', '#123456', 'brown',
         'black']

root = tkinter.Tk()
l1 = tkinter.Label(root, text="My Personal Calculator",
                  font=('Times', 20, 'bold'), fg='red')
l1.pack()

s = tkinter.StringVar()
e = tkinter.Entry(root, textvariable=s, font=('Times', 30, 'bold'), 
                 bg="#123456", fg='white')
e.pack()


def add_label():
    color = random.choice(colors)
    ans = eval(s.get())
    text = f"{s.get()} = {ans:.2f}"
    label = tkinter.Label(root, text=text,  font=('Times', 20, 'bold'), fg=color)
    s.set('')
    label.pack()
    
    
b = tkinter.Button(root, text="!Solve Me!", command=add_label,
                  font=15, bg='#123456', fg='white', height=1, width=25)
b.pack()

exit_button = tkinter.Button(root, text="!EXIT!", command=root.destroy,
                            font=15, bg='#123456', fg='white', height=1, width=25)
exit_button.pack()

root.title('Calculator')
root.wm_minsize(800, 600)
root.mainloop()
