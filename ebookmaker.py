from ebooklib import epub
import os
import TOC_genertator


# Developed by CabTheProgrammer
# This is the back-end for the ebook gui! This script converts pre-formatted text files into an ebook format
# for easy reading
# Function to count number of files in a directory

def d_count(address):  # Counts the number of files in a directory
    num = 0
    for stuff in os.listdir(address):
        num += 1
    return int(num)


# function to "chunkify" process?
def chunk(whole, chunksize):
    Arr = [0, 0, "flag", 0]
    Arr[0] = round(whole / chunksize)  # Chapter size of each volume
    Arr[1] = whole - ((Arr[0] - 1) * chunksize)  # Chapter size of the last volume
    Arr[3] = chunksize  # This is the size of the "chunk" (number of chapters in each volume)
    return Arr


def op(addr, chapsize):
    if int(chapsize) != 0:
        chap_size = chapsize
        vol_size = chunk(d_count(addr), int(chap_size))
        vol_size[2] = "Non-Omnibus"
        print(str(vol_size[0]) + " volumes will be created")
        print(str(vol_size[1]))
        return_val = vol_size
    else:
        vol_size = [0, 0]
        vol_size[0] = d_count(addr)
        print("One ebook with " + str(vol_size[0]) + " chapters will be created")
        vol_size[1] = "Omnibus"
        return_val = vol_size
    return return_val


def LeLoop(arr, addr, book):  # Yup this could have been done differently smh
    i = 0
    name = book.title
    if "Omnibus" in arr:  # Option to create a single ebook
        print("Omnibus Loop")
        TOC_genertator.create(addr)
        while arr[0] > i:
            c_file = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
            c_text = c_file.read()
            chap_write = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
            chap_write.set_content(c_text)
            book.add_item(chap_write)
            book.toc = (epub.Link('Chapter%s.xhtml' % str(i), 'Chapter %s' % str(i)), chap_write)
            book.spine = book.spine + [chap_write]
            c_file.close()
            i = i + 1

            if i > 10:  # TODO Delete This
                break
            # while loop to add all chapters
        epub.write_epub('%s.epub' % book.title, book, {})
        print('Book Complete!')

    else:  # Option to create volumes instead of omnibus
        print("NonOmnibus Loop")
        t_volume = d_count(addr)
        count = 0
        vol_num = 0  # Count for each book volume
        print(str(arr[0]))
        TOC_genertator.create_vol(arr, addr)
        print("Table of Contents created")
        while t_volume > count:
            if count + arr[1] == t_volume:
                """ This generates the last volume specifically as its chapter size
                 may be greater or lesser than the given size"""
                book.title = name
                for iter in range(arr[1] - 1):
                    c_file = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
                    c_text = c_file.read()
                    chap_write = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i),
                                               lang='en')
                    chap_write.content = c_text
                    book.add_item(chap_write)
                    book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chap_write)
                    book.spine = book.spine + [chap_write]

                    c_file.close()
                    count += 1  # iterates l in the outer loop
                    i += 1

                vol_num += 1
                epub.write_epub('%s Volume %s.epub' % (book.title, str(vol_num)), book, {})
                book.reset()  # Were my prayers answered or is this a dud?
                print('Volume %s of %s  complete!' % (vol_num, arr[0]))
                print('Volume Generation Complete!')
                return

            for iter in range(arr[3]):  # This is for each volume
                c_file = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
                c_text = c_file.read()
                chap_write = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
                chap_write.content = c_text
                book.add_item(chap_write)
                book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chap_write)
                book.spine = book.spine + [chap_write]

                c_file.close()
                count += 1  # iterates count in the outer loop
                # while loop to add all chapters
                i += 1
            vol_num += 1
            epub.write_epub('%s Volume %s.epub' % (book.title, str(vol_num)), book, {})
            book.reset()  # Were my prayers answered or is this a dud?
            book.title = name
            print('Volume %s of %s  complete!' % (vol_num, arr[0]))


class PseudoBook:
    def __init__(self, auth, title, cover, addr, chapsize):  # For initialization and stuff
        self.Author = auth
        self.Title = title
        self.cover = cover  # holds the address of the image to be used as the book cover
        self.addr = addr
        # "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"
        # usually addr of the directory with the formatted files.
        self.chap_size = chapsize
        self.book = epub.EpubBook()
        self.book.set_identifier("EBK")
        self.book.set_title(self.Title)
        self.book.set_language('en')
        self.book.add_author(self.Author)
        self.book.spine = ['cover']

        if self.cover != "none":
            self.book.set_cover(self.cover, open(self.cover, 'rb').read())
        else:
            print("There is no cover")

        # Changes working directory
        os.chdir(self.addr)
        os.makedirs('./Ebook', exist_ok=True)
        os.chdir('Ebook')

    def build_book(self):  # To Actually build the book
        c_info = op(self.addr, self.chap_size)
        LeLoop(c_info, self.addr, self.book)

    def gimme_addr(self):
        return self.addr

# For testing purposes below
# B = Psuedo_Book("John Mayer", "Test Volume", "none", "MT", 40)
# B.build_book()

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
