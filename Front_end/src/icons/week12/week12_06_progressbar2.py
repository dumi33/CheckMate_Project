from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        lbl_value['text'] = update_progress_label()
    else:
        messagebox.showinfo(message='The progress completed!')


def stop():
    pb.stop()
    lbl_value['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(root, orient='horizontal', mode='determinate',  length=280)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
lbl_value = ttk.Label(root, text=update_progress_label())
lbl_value.grid(column=0, row=1, columnspan=2)

# start button
btn_start = ttk.Button(root, text='Progress', command=progress)
btn_start.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

btn_stop = ttk.Button(root, text='Stop', command=stop)
btn_stop.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

root.mainloop()
