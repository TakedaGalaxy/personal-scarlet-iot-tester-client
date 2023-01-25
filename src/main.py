from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    app = Tk()
    frame = ttk.Frame(app, padding=10)
    frame.grid()
    ttk.Label(frame, text="Olá mundo !").grid(column=0, row=0)
    ttk.Button(frame, text="Sair", command=app.destroy).grid(column=0, row=1)
    app.mainloop()
