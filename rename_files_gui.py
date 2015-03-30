import Tkinter
from rename_files import *

def run():
    source_patt = source_field.get()
    dest_pattern = dest_field.get()
    pathname = path_field.get()
    rename_files(pathname, source_patt, dest_pattern)
def quit():
    root.destroy()

root = Tkinter.Tk()

label = Tkinter.Label(root, text="Rename File Group")
label.pack()

space = Tkinter.Label(root, text=" ")
space.pack()

source_pattern = Tkinter.Label(root, text="Source Pattern")
source_pattern.pack()

source_field = Tkinter.Entry(root)
source_field.pack()

dest = Tkinter.Label(root, text="Destination Pattern")
dest.pack()
dest_field = Tkinter.Entry(root)
dest_field.pack()

path = Tkinter.Label(root, text="Path")
path.pack()
path_field = Tkinter.Entry(root)
path_field.pack()

button = Tkinter.Button(root, text="Run", command=run)
button.pack()

quit = Tkinter.Button(root, text="Quit", command=quit)
quit.pack()

root.mainloop()
