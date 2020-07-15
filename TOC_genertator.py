import os

"""
This is intended to generate a table of contents for an e-book as well as the toc.ncx file
The generated files will be named nav.xhtml and toc.ncx respectively 
Developed by CabTheProgrammer
"""


def d_count(addr):  # Counts the number of files in a directory
    num = 0
    for stuff in os.listdir(addr):
        num += 1
    return int(num)



B_Title = "This content has been generated through python"

toc_head = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n\
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">\n\
  <head>\n\
    <meta content="MOL" name="dtb:uid"/>\n\
    <meta content="2" name="dtb:depth"/>\n\
    <meta content="calibre (3.26.1)" name="dtb:generator"/>\n\
    <meta content="0" name="dtb:totalPageCount"/>\n\
    <meta content="0" name="dtb:maxPageNumber"/>\n\
  </head>\n\
  <docTitle>\n\
    <text>%s</text>\n\
  </docTitle>' % B_Title

toc_tail = '   </navPoint>\n\
</navMap>\n\
  </ncx>'

head = '?xml version=\'1.0\' encoding=\'utf-8\'?>\n\
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n\
    <head>\n\
        <title>Navigation</title>\n\
    </head>\n\
    <body>\n\
    <nav epub:type="toc">\n\
  <ol>'

tail = '</ol>\n\
</nav>\n\
</body>\n\
</html>'

cover = ' <li><a href="EPUB/cover.xhtml">Cover</a></li>'  # Needed if the e-book will have a cover

global add_string, toc_string, nav, toc
add_string = ""
toc_string = ""
nav = ""
toc = ""


def create(address):
    count = d_count(address)
    global toc_string, add_string, nav, toc
    i = 1
    while i < count:
        add_string = add_string + '\n<li><a href="EPUB/Chapter%s.xhtml">Chapter %s</a></li>' % (i, i)

        toc_string = toc_string + '</navPoint><navPoint id="num_%s" playOrder="%s">\n\
          <navLabel>\n\
            <text>Chapter 00%s</text>\n\
          </navLabel>\n\
          <content src="EPUB/Chapter%s.xhtml"/>' % (i, i, i, i)

        i = i + 1
    nav = head + cover + add_string + tail
    toc = toc_head + toc_string + toc_tail

    # TODO: Delete these comments to  create the actual navigation file
    # file = open("nav.xhtml", "w")
    # file.write(nav)
    # file.close()

    # t_file = open("toc.ncx", "w")
    # t_file.write(toc)
    # t_file.close()


def create_vol(array, address):  # overridden method for constructing multiple files
    # arr[0] is the size of the chapter of the volumes
    # arr[1] is the chapter size of the last volume
    # arr[3] is the size of the chunk?
    count = d_count(address)
    global toc_string, add_string, nav, toc
    int_cnt = 1
    i = 0
    while int_cnt <= count:
        for cnt in range(array[0]):
            int_cnt += 1
            add_string = add_string + '\n<li><a href="EPUB/Chapter%s.xhtml">Chapter %s</a></li>' % (cnt, int_cnt)
            toc_string = toc_string + '</navPoint><navPoint id="num_%s" playOrder="%s">\n\
          <navLabel>\n\
            <text>Chapter 00%s</text>\n\
          </navLabel>\n\
          <content src="EPUB/Chapter%s.xhtml"/>' % (cnt, cnt, cnt, int_cnt)

            if int_cnt == count or int_cnt + array[1] == count:  # Prevents int count from exceeding the chapter count
                print("\n")
                break
        # code to write files
        nav = head + cover + add_string + tail
        toc = toc_head + toc_string + toc_tail

        # TODO: DELETE THESE COMMENTS TO WRITE FILES
        # file = open("nav%s.xhtml" % i, "w")
        # file.write(nav)
        # file.close()

        # file = open("toc%s.ncx" % i, "w")
        # file.write(toc)
        # file.close()
        i += 1

        # clears add_string
        add_string = ""
        toc_string = ""

        if int_cnt + array[1] == count:
            add_string = ""
            toc_string = ""
            for stuff in range(array[1]):
                int_cnt += 1
                add_string = add_string + '\n<li><a href="EPUB/Chapter%s.xhtml">Chapter %s</a></li>' % (stuff, int_cnt)
                toc_string = toc_string + '</navPoint><navPoint id="num_%s" playOrder="%s">\n\
                          <navLabel>\n\
                            <text>Chapter 00%s</text>\n\
                          </navLabel>\n\
                          <content src="EPUB/Chapter%s.xhtml"/>' % (stuff, stuff, stuff, int_cnt)

                if int_cnt == count:
                    nav = head + add_string + tail
                    toc = toc_head + toc_string + toc_tail

                    # TODO: Delete these comments as well to write files
                    # file = open("toc_tail.ncx", "w")
                    # file.write(toc)
                    # file.close()

                    # file = open("nav_tail.xhtml", "w")
                    # file.write(nav)
                    # file.close()
                    break

        if int_cnt >= count:  # Prevents int count from exceeding the chapter count
            break
    print("Complete")


# arr = [20, 4, 80, 40]
# create_vol(arr)
