from ebooklib import epub
import os


# Function to count number of files in a directory
def dcount(address):
    num = 0
    for stuff in os.listdir(address):
        num += 1
    return int(num)


# function to chunkify process?
def chunk(whole, chunksize):
    Arr = [0, 0, "flag", 0]
    Arr[0] = round(whole / chunksize)  # Chapter size of each volume
    Arr[1] = whole - ((Arr[0] - 1) * chunksize)  # Chapter size of the last volume
    Arr[3] = chunksize  # This is the size of the "chunk"
    return Arr


def op(addr):
    print("Would you like to create the ebook in volumes or in just one ominibus?")
    print("Chapters available: " + str(dcount(addr)) + " chapters!")
    print("1) Volumes\n2) Omnibus\n")
    option = input()
    if int(option) == 1:
        print("How many chapters per volume? ")
        chap_size = input()
        vol_size = chunk(dcount(addr), int(chap_size))
        vol_size[2] = "Non-Omnibus"
        print("Ok, " + str(vol_size[0]) + " volumes will be created")
        print(str(vol_size[1]))
        return_val = vol_size
    else:
        vol_size = [0, 0]
        vol_size[0] = dcount(addr)
        print("One ebook with " + str(vol_size[0]) + " chapters will be created")
        vol_size[1] = "Omnibus"
        return_val = vol_size
    return return_val


def LeLoop(Arr, addr, book):  # Yup this could have been done differently smh
    i = 0
    name = book.title
    if "Omnibus" in Arr:
        print("Omnibus Loop")
        while Arr[0] > i:
            cfile = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
            ctext = cfile.read()
            chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
            chapwrite.content = ctext
            book.add_item(chapwrite)
            book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chapwrite)
            book.spine = book.spine + [chapwrite]
            # print(book.spine)
            cfile.close()
            i = i + 1
            if i > 10:  # DELETE THIS
                break
            # while loop to add all chapters

        epub.write_epub('%s.epub' % book.Title, book, {})
        print('Book Complete!')

    else:
        print("NonOmnibus Loop")
        t_volume = dcount(addr)
        count = 0
        vol_num = 0  # Count for each book volume
        print(str(Arr[0]))
        while t_volume > count:
            if count + Arr[
                1] == t_volume:  # This generates the last volume specifically as its chapter size may be greater or lesser than the given size
                book.title = name
                for iter in range(Arr[1]):
                    cfile = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
                    ctext = cfile.read()
                    chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i),
                                              lang='en')
                    chapwrite.content = ctext
                    book.add_item(chapwrite)
                    book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chapwrite)
                    book.spine = book.spine + [chapwrite]

                    cfile.close()
                    count += 1  # iterates l in the outer loop
                    i += 1
                vol_num += 1
                epub.write_epub('%s Volume %s.epub' % (book.title, str(vol_num)), book, {})
                book.reset()  # Were my prayers answered or is this a dud?
                print('Volume %s of %s  complete!' % (vol_num, Arr[0]))
                print('Volume Generation Complete!')
                return

            for iter in range(Arr[3]):  # This is for each volume
                cfile = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
                ctext = cfile.read()
                chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
                chapwrite.content = ctext
                book.add_item(chapwrite)
                book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chapwrite)
                book.spine = book.spine + [chapwrite]

                cfile.close()
                count += 1  # iterates count in the outer loop
                # while loop to add all chapters
                i += 1
            vol_num += 1
            epub.write_epub('%s Volume %s.epub' % (book.title, str(vol_num)), book, {})
            book.reset()  # Were my prayers answered or is this a dud?
            book.title = name
            print('Volume %s of %s  complete!' % (vol_num, Arr[0]))


class PsuedoBook:
    def __init__(self, auth, title, cover, addr):  # For initialization and stuff
        self.Author = auth
        self.Title = title
        self.cover = cover  # holds the address of the image to be used as the book cover
        self.addr = "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"  # usually addr

        self.book = epub.EpubBook()
        self.book.set_identifier("EBK")
        self.book.set_title(self.Title)
        self.book.set_language('en')
        self.book.add_author(self.Author)
        if self.cover != "none":
            print("This is not none")
            self.book.set_cover(self.cover, open(self.cover, 'rb').read())
        print("This is  none")
        self.book.spine = ['cover']

    def build_book(self):  # To Actually build the book
        c_info = op(self.addr)
        LeLoop(c_info, self.addr, self.book)


B = PsuedoBook("John Mayer", "Test Volume", "none", "MT")
B.build_book()

# book = epub.EpubBook()
# addr = "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"
# Adding MetaData:
# book.set_identifier('PGE')
# book.set_title('A Practical Guide to Evil')
# book.set_language('en')
# book.add_author('erraticerrata')

# book.set_cover("Evil.jpg",open('Evil.jpg','rb').read())
# i = 0
# l = op(addr)

# LeLoop(l)
# print(str(l))


# book.spine=['cover']
# chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
# book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter%s' % i), (chapwrite))
