#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import sys, os
from blmbook import *

con = sqlite3.connect('books.db')

books = []
menu_actions = {}

### Book Section ###

def list_books():
    for mbook in books:
        print "Name: %s" % mbook.Name
        print "Author: %s %s" % (mbook.Author_First, mbook.Author_Last)
        print "Price: %.2f" % mbook.Price
        print "Category: %s" % mbook.Category
        print ""

def add_book():
    global books
    name = raw_input("Book Name: ")
    author_first = raw_input("Author First Name: ")
    author_last = raw_input("Author Last Name: ")
    price = raw_input("Price: ")
    category = raw_input("Category: ")
    append_book(con, books, name, author_first, author_last, float(price), category)
    books = []
    get_books(con, books)

### End Book Section ###

### Menu Section ###

def main_menu():
    os.system('clear')
    print "Please choose what you would like to do:"
    print "1. Add a book"
    print "2. List Books"
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid Selection, please try again.\n"
            menu_actions['main_menu']()
    return

def menu1():
    print "Adding a book!\n"
    add_book()
    print "-----"
    menu_actions['main_menu']()

def menu2():
    print "Listing Books!\n"
    list_books()
    raw_input("Press enter to return")
    menu_actions['main_menu']()

def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()

menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}
### End Menu Section ###

# Main Program
if __name__ == "__main__":
    # Launch the main menu
    get_books(con, books)
    main_menu()
