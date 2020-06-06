from ebooklib import epub
import os


def test():
    print("Hello")


# Function to count number of files in a directory
def dcount(address):
    num = 0
    for stuff in os.listdir(address):
        num += 1
    return int(num)


# function to chunkify process?
def chunk(whole, chunksize):
    Arr = [0, 0,"flag",0]
    Arr[0] = round(whole / chunksize)  # Chapter size of each volume
    Arr[1] = whole - ((Arr[0] - 1) * chunksize)  # Chapter size of the last volume
    Arr[3]=chunksize
    return Arr


def op():
    print("Would you like to create the ebook in volumes or in just one ominibus?")
    print("Chapters available: " + str(dcount(addr)) + " chapters!")
    print("1) Volumes\n2) Omnibus\n")
    option = input()
    if int(option) == 1:
        print("How many chapters per volume? ")
        chap_size = input()
        vol_size = chunk(dcount(addr), int(chap_size))
        vol_size[2]="Non-Omnibus"
        print("Ok, " + str(vol_size[0]) + " volumes will be created")
        print(str(vol_size[1]))
        return_val = vol_size
    else:
        vol_size=[0,0]
        vol_size[0]=dcount(addr)
        print("One ebook with " + str(vol_size[0]) + " chapters will be created")
        vol_size[1] = "Omnibus"
        return_val = vol_size
    return return_val

def LeLoop(Arr): #Yup this could have been done differently smh
    i = 0
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
            if i > 10: #DELETE THIS
                break
            # while loop to add all chapters

        epub.write_epub('Test01.epub', book, {})
        print('Book Complete!')

    else:
        print("NonOmnibus Loop")
        t_volume=dcount(addr)
        i=0
        count=0
        vol_num=0#Count for each book volume
        print(str(Arr[0]))
        while t_volume> count:
            for iter in range(Arr[3]):#This is for each volume
                cfile = open(addr + "\\Chapter %s.txt" % str(i), encoding="UTF-8")
                ctext = cfile.read()
                chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
                chapwrite.content = ctext
                book.add_item(chapwrite)
                book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter %s' % i), chapwrite)
                book.spine = book.spine + [chapwrite]

                cfile.close()
                count+=1 #iterates l in the outer loop
                #if i > 10:  # DELETE THIS
                    #break
                # while loop to add all chapters
            vol_num+=1
            epub.write_epub('Volume %s.epub' %str(vol_num), book, {})
            book.reset()# Were my prayers answered or is this a dud?
            print('Book Complete!')



class PsuedoBook:
    def __init__(self, auth, title, cover, addr):
        self.Author = auth
        self.Title = title
        self.Cover = cover  # holds the address of the image to be used as the book cover

        book = epub.EpubBook()
        book.set_identifier()
        book.set_title(self.Title)
        book.set_language('en')
        book.add_author(self.Author)
        book.set_cover(self.Cover, open(self.Cover, 'rb').read())
        book.spine = ['cover']


book = epub.EpubBook()
addr = "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"
# Adding MetaData:
# book.set_identifier('PGE')
book.set_title('A Practical Guide to Evil')
# book.set_language('en')
# book.add_author('erraticerrata')

# book.set_cover("Evil.jpg",open('Evil.jpg','rb').read())
i = 0
l = op()

LeLoop(l)
# print(str(l))


# book.spine=['cover']
chapwrite = epub.EpubHtml(title='Chapter%s' % str(i), file_name='Chapter%s.xhtml' % str(i), lang='en')
book.toc = (epub.Link('Chapter%s.xhtml' % i, 'Chapter%s' % i), (chapwrite))


