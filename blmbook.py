#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

class Book(object):
    Name = ""
    Author_First = ""
    Author_Last = ""
    Price = 0.00
    Category = ""

    def __init__(self, name, author_first, author_last, price, category):
        self.Name = name
        self.Author_First = author_first
        self.Author_Last = author_last
        self.Price = price
        self.Category = category

def make_book(name, author_first, author_last, price, category):
    book = Book(name, author_first, author_last, price, category)
    return book

def add_book(name, author_first, author_last, price, category):
    mbook = make_book(name, author_first, author_last, price, category)
    books.append(mbook)

def get_books(con, books):
    with con:
        cur = con.cursor()
        cur.execute("SELECT Name, Author_First, Author_Last, Price, Category FROM Books ORDER BY Author_Last")

        rows = cur.fetchall()
        for row in rows:
            mbook = make_book(row[0], row[1], row[2], row[3], row[4])
            books.append(mbook)
