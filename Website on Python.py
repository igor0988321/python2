import dominate
from dominate.tags import *
import os



doc = dominate.document()

with doc:
    h1("Hello World")

    with ol():
        li("1. aaa")
        li("2. bbb")
        li("3. ccc")

    p("End of page")


file = open("index.html", 'w')
file.write(doc.render())
file.close()

os.system("start index.html")