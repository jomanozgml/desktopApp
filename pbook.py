from tkinter import *
# import tktable

window = Tk()
window.title("Purchase Book")
window.geometry("900x600")
window.wm_iconbitmap('logo.ico')
#print "This is Purchase Book Application"
# table = tktable.Table(window, rows=10, cols=4)
# table.pack(side="top", fill="both", expand=True)
titleName = ['Name','PAN No.','Group']
entryName = ['NANC', 300054974, 'Own Company']
#v = StringVar()
height = 10
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
		b = Label(window, text=titleName[j], padx=5, pady=5, bd=1, relief="flat")
		b.grid(row=0, column=j)
		e = Entry(window, relief="groove")
		e.grid(row=i+1, column=j)
		e.insert(0,entryName[j])
		#v.set(entryName[j])

window.mainloop()