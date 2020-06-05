from ebooklib import epub
import os

def test():
    print("Hello")

#Function to count number of files in a directory
def dcount(address):
    num=0
    for stuff in os.listdir(address):
        num+=1
    return int(num)
# function to chunkify process?
def chunk(whole,chunksize):
    Arr=[0,0]
    Arr[0]=round(whole/chunksize)# Chapter size of each volume
    Arr[1]=whole-((Arr[0]-1)*chunksize)# Chapter size of the last volume 
    return Arr

def op():
    print("Would you like to create the ebook in volumes or in just one ominibus?")
    print("Chapters available: "+str(dcount(addr))+ " chapters!")
    print("1) Volumes\n2) Omnibus\n")
    option=input()
    if int(option) is 1:
        print("How many chapters per volume? ")
        csize=input()
        vsize=chunk(dcount(addr),int(csize))
        print("Ok, "+str(vsize[0])+" volumes will be created")
        Ans=vsize
    else:
        print("Ok, one ebook with "+str(dcount(addr))+ " chapters will be created")
        Ans=dcount(addr)
    return Ans

def int_check(i):
    if isinstance(i,int) is True:
        print("True")
    else:
        print("False")
        

class PsuedoBook:
    def __init__(Author,Title,Cover,Addr):
        self.Author=Author
        self.Title=Title
        self.Cover=Cover #holds the address of the image to be used as the book cover

        book=epub.EpubBook()
        book.set_identifier()
        book.set_title(self.Title)
        book.set_language('en')
        book.add_author(self.Author)
        book.set_cover(self.Cover,open(self.Cover,'rb').read())
        book.spine=['cover']
    
book=epub.EpubBook()
addr= "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"
#Adding MetaData:
#book.set_identifier('PGE')
book.set_title('A Practical Guide to Evil')
#book.set_language('en')
#book.add_author('erraticerrata')

#book.set_cover("Evil.jpg",open('Evil.jpg','rb').read())
i=0
l=op()
int_check(i)
#print(str(l))


    
#book.spine=['cover']
chapwrite=epub.EpubHtml(title='Chapter%s'%str(i),file_name='Chapter%s.xhtml'%str(i),lang='en')
book.toc=(epub.Link('Chapter%s.xhtml'%i,'Chapter%s'%i),(chapwrite))

while(i<103):
    cfile=open(addr+"\\Chapter %s.txt"%str(i),encoding="UTF-8")
    ctext=cfile.read()
    chapwrite=epub.EpubHtml(title='Chapter%s'%str(i),file_name='Chapter%s.xhtml'%str(i),lang='en')
    chapwrite.content=ctext
    book.add_item(chapwrite)
    book.toc+=(epub.Link('Chapter%s.xhtml'%i,'Chapter %s'%i),(chapwrite))
    book.spine=book.spine+[chapwrite]
    print(book.spine)
    
    cfile.close()
    i=i+1
    if i > 10:
        break
    #while loop to add all chapters


epub.write_epub('Test01.epub',book,{})
print('Book Complete!')
