from tkinter import filedialog

dir_path = filedialog.askdirectory(initialdir="/",title='Please select a directory')
print(dir_path)