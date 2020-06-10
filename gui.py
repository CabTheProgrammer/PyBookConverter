import tkinter
from tkinter import filedialog
from PIL import ImageTk,Image
import sys

#import ebookmaker


#Initial stuff
name="Ebook Compiler 0.1"

window=tkinter.Tk()
window.title(name)
window.geometry("400x400")



#Functions
def filech():
    print("This is suppose to select the users directory")
    filename=filedialog.askdirectory()
    print(filename)
    filelabel.config(text=str(filename))

    
def comp():
    print("This is suppose to compile an ebook, based on file directory")
    Author=e11.get()
    Title=e1.get()
    print("Name of Ebook: "+Title)
    print("Name of Author: "+Author)
    
def getCover():
    filename=filedialog.askopenfilename(filetypes=(("jpeg files","*.jpg"),("png files","*.png"),("all files","*")))
    img=Image.open(filename)
    img=img.resize((125,125),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    
    piclabel.configure(image=img)
    piclabel.image(img)
    
    pass
    
#Buttons and labels and entries
bgcolor="grey"
fgcolor="purple"
label=tkinter.Label(window,text=name).pack(expand="yes",fill="both")
bt=tkinter.Button(window,text="Choose Folder Directory",command=filech,bg=bgcolor,fg=fgcolor).pack()

filelabel=tkinter.Label(window)
filelabel.pack()


picbutton=tkinter.Button(window,text="Add Book Cover",bg=bgcolor,fg=fgcolor,command=getCover)
picbutton.pack()
piclabel=tkinter.Label(window)
piclabel.pack()


label2=tkinter.Label(window,text="Enter name of ebook").pack(expand="yes",fill="both")
e1=tkinter.Entry(window,width=25)
e1.pack()

label3=tkinter.Label(window,text="Enter name of author").pack(expand="yes",fill="both")
e11=tkinter.Entry(window,width=25)
e11.pack()



bt3=tkinter.Button(window,text="Compile Ebook",bg=bgcolor,fg=fgcolor,command=comp).pack(side="right")
bt2=tkinter.Button(window,text="Exit Program",bg=bgcolor,fg=fgcolor,command=window.destroy)
bt2.pack(side="left")



#Info from entries
#title=str(e1.get())
#author=str(el1.get())

window.mainloop()
