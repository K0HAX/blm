#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import sys
from blmbook import *

con = sqlite3.connect('books.db')

books = []
get_books(con, books)

for mbook in books:
    print "Name: %s" % mbook.Name
    print "Author: %s %s" % (mbook.Author_First, mbook.Author_Last)
    print "Price: %.2f" % mbook.Price
    print "Category: %s" % mbook.Category
    print ""
