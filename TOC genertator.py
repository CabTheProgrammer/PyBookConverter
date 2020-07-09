import ebookmaker

"""
This is intended to generate a table of contents for an e-book as well as the toc.ncx file
The generated file will be named nav.xhtml and toc.ncx respectively 
Developed by CabTheProgrammer
"""
address = "C:\\Users\\CAB\\PycharmProjects\\PracticalGrab\\A Practical Guide to Evil\\A Practical Guide to Evil"
count = ebookmaker.dcount(address)
B_Title = "Test"

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
i = 1

add_string = ""
toc_string = ""
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
# creating the actual navigation file

file = open("nav.xhtml", "w")
file.write(nav)
file.close()

t_file = open("toc.ncx", "w")
t_file.write(toc)
t_file.close()
