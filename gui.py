import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image
import ebookmaker

# Initial stuff
name = "Ebook Compiler 0.2"
window = tkinter.Tk()
window.title(name)
window.geometry("500x350")
window.minsize(width=500, height=350)
global radio
filename = "blank"
im = "blank"
radio = 0


# Functions

def popupmsg(msg):
    popup=tkinter.Tk()
    popup.title="Alert!"
    label=tkinter.Label(popup,text=msg)
    label.pack(side="top",fill="x",pady=10)
    b1=tkinter.Button(popup,text="OK",command=popup.destroy)
    b1.pack()

    popup.mainloop()


def hide():
    ChapSizeLabel.grid_forget()
    ChapSizeEntry.grid_forget()
    global radio
    radio = 0


def reveal():
    print("This reveal the options for volume")
    ChapSizeLabel.grid(row=10, column=1)
    ChapSizeEntry.grid(row=10, column=3)
    global radio
    radio = 1


def  filech():
    print("This is supposed to select the users directory")
    global filename
    filename = filedialog.askdirectory()
    print(filename)
    if filename != '':
        filelabel.config(text=str(filename))
        numlabel.config(text="Number of Chapters " + str(ebookmaker.dcount(filename)))


def comp():
    print("This is supposed to compile an ebook, based on file directory")
    Author = AuthEntry.get()
    Title = EbookNameEntry.get()
    Chapsize = ChapSizeEntry.get()
    Addr = filename
    BookCover = im

    #These are for validation to ensure that the back-end doesn't get anything
    if Addr == "blank":
        popupmsg("Error, no address was selected")
        return
    if Title == "":
        Title = "Empty"
    if Author == "":
        Author = "Blank McBlankface"
    if Chapsize == ""or radio == 0:
        Chapsize =0

    print("Compiling "+Title + " By "+Author+" with "+str(Chapsize)+ " chapters")

    # Going to create and save ebook here
    # A= ebookmaker.PsuedoBook(Author,Title,BookCover,Addr,Chapsize)


def getCover():
    filename = filedialog.askopenfilename(
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*")))
    img = Image.open(filename)
    img = img.resize((80, 80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    global im
    im = img
    piclabel.configure(image=img)
    piclabel.image(img)


# Buttons and labels and entries
bgcolor = "grey"
fgcolor = "purple"
label = tkinter.Label(window, text=name)
bt = tkinter.Button(window, text="Choose Folder Directory", command=filech, bg=bgcolor, fg=fgcolor)

filelabel = tkinter.Label(window)
numlabel = tkinter.Label(window)

ChapSizeLabel = tkinter.Label(window,
                              text="Size of Chapter")  # These two should only appear if the radio button for volumes are selected
ChapSizeEntry = tkinter.Entry(window, width=25)  # This is for the entry of the chapter size

picbutton = tkinter.Button(window, text="Add Book Cover", bg=bgcolor, fg=fgcolor, command=getCover)
piclabel = tkinter.Label(window)

b1 = tkinter.Radiobutton(window, text="Omnibus", variable=radio, value=1, command=hide)
b2 = tkinter.Radiobutton(window, text="Volume", variable=radio, value=2, command=reveal)


EbookName = tkinter.Label(window, text="Enter name of ebook")
EbookNameEntry = tkinter.Entry(window, width=25)

AuthLabel = tkinter.Label(window, text="Enter name of author")
AuthEntry = tkinter.Entry(window, width=25)

CompileIt = tkinter.Button(window, text="Compile Ebook", bg=bgcolor, fg=fgcolor, command=comp)
ExitButton = tkinter.Button(window, text="Exit Program", bg=bgcolor, fg=fgcolor, command=window.destroy)

# Grid section
label.grid(row=0, column=2)
bt.grid(row=1, column=2)
filelabel.grid(row=2, column=2)
numlabel.grid(row=3, column=2)

picbutton.grid(row=5, column=2)
piclabel.grid(row=6, column=3)

EbookName.grid(row=8, column=1)
EbookNameEntry.grid(row=8, column=3)
AuthLabel.grid(row=9, column=1)
AuthEntry.grid(row=9, column=3)

b1.grid(row=11, column=1)
b2.grid(row=11, column=2)

CompileIt.grid(row=13, column=3)
ExitButton.grid(row=13, column=1)

# Info from entries
# title=str(e1.get())
# author=str(el1.get())

window.mainloop()
