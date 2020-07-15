import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image
import ebookmaker

# Initial stuff
name = "Ebook Compiler 0.2"
window = tkinter.Tk()
window.title(name)
window.geometry("500x350")
window.minsize(width=500, height=250)
global radio
filename = "blank"
im = "blank"
radio = 0


# Functions

def popupmsg(msg):
    popup = tkinter.Tk()
    popup.title = "Alert!"
    label = tkinter.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = tkinter.Button(popup, text="OK", command=popup.destroy)
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
        file_label.config(text=str(filename))
        num_label.config(text="Number of Chapters " + str(ebookmaker.d_count(filename)))


def comp():
    print("This is supposed to compile an ebook, based on file directory")
    auth = AuthEntry.get()
    title = EbookNameEntry.get()
    chap_size = ChapSizeEntry.get()
    addr = filename
    book_cover = im

    # These are for validation to ensure that the back-end doesn't get anything
    if addr == "blank":
        popupmsg("Error, no address was selected")
        return
    if title == "":
        title = "Empty"
        popupmsg("Error, no title was Given")
        return
    if auth == "":
        auth = "Blank McBlankface"
        popupmsg("Error, no auth was Given")
        return
    if chap_size == "" or radio == 0:
        chap_size = 0

    print("Compiling " + title + " By " + auth + " with " + str(chap_size) + " chapters")

    # Going to create and save ebook here
    #  A= ebookmaker.PsuedoBook(auth,title,book_cover,addr,chap_size)
    #  A.build_book()


def getCover():
    file_name = filedialog.askopenfilename(
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*")))
    img = Image.open(file_name)
    img = img.resize((80, 80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    global im
    im = img
    pic_label.configure(image=img)
    pic_label.image(img)


# Buttons and labels and entries
bg_color = "grey"
fg_color = "purple"
label = tkinter.Label(window, text=name)
bt = tkinter.Button(window, text="Choose Folder Directory", command=filech, bg=bg_color, fg=fg_color)

file_label = tkinter.Label(window)
num_label = tkinter.Label(window)

ChapSizeLabel = tkinter.Label(window, text="Size of Chapter")
# These two should only appear if the radio button for volumes are selected
ChapSizeEntry = tkinter.Entry(window, width=25)  # This is for the entry of the chapter size

pic_button = tkinter.Button(window, text="Add Book Cover", bg=bg_color, fg=fg_color, command=getCover)
pic_label = tkinter.Label(window)

b1 = tkinter.Radiobutton(window, text="Omnibus", variable=radio, value=1, command=hide)
b2 = tkinter.Radiobutton(window, text="Volume", variable=radio, value=2, command=reveal)


EbookName = tkinter.Label(window, text="Enter name of ebook")
EbookNameEntry = tkinter.Entry(window, width=25)

AuthLabel = tkinter.Label(window, text="Enter name of author")
AuthEntry = tkinter.Entry(window, width=25)

CompileIt = tkinter.Button(window, text="Compile Ebook", bg=bg_color, fg=fg_color, command=comp)
ExitButton = tkinter.Button(window, text="Exit Program", bg=bg_color, fg=fg_color, command=window.destroy)

# Grid section
label.grid(row=0, column=2)
bt.grid(row=1, column=2)
file_label.grid(row=2, column=2)
num_label.grid(row=3, column=2)

pic_button.grid(row=5, column=2)
pic_label.grid(row=5, column=3)

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
