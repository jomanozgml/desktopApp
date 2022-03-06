# from Tkinter import *

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
   # mylist.insert(END, "This is line number " + str(line))

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )

# mainloop()

from tkinter import *

def on_mousewheel(event):
    canvas.yview_scroll(-1*(event.delta/120), "units")
	
root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500), yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.pack(side=LEFT,expand=True,fill=BOTH)
scrollbar.config(command=canvas.yview)
root.mainloop()




