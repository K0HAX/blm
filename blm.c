#include <stdio.h>
#include <string.h>
#include <sqlite3.h>

typedef struct Isbn
{
  int gs1[3];
  int group[2];
  int publisher[4];
  int title[3];
  int check[1];
};

typedef struct Book
{
  char name[255];
  char author[255];
  struct Isbn isbn;
  float price;
  char category[255];
  char genre[255];
};

sqlite3 *db;
sqlite3_stmt *res;
int rc;

int main(void)
{
  int i, choice;
  char oname[100];
  struct Book * book;
  char c;

  rc = sqlite3_open("books.db", &db);

  if (rc != SQLITE_OK) {
      fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
      sqlite3_close(db);
      return 1;
  }

  ListBooks();

  sqlite3_finalize(res);
  sqlite3_close(db);

  return 0;
}

int ListBooks() {
    char *sql = "SELECT Name, Author, Price, Category, Genre FROM Books";
    rc = sqlite3_prepare_v2(db, sql, -1, &res, 0);

    if (rc == SQLITE_OK) {
        sqlite3_bind_int(res, 1, 3);
    } else {
        fprintf(stderr, "Failed to execute statement: %s\n", sqlite3_errmsg(db));
    }

    int step = sqlite3_step(res);

    if (step == SQLITE_ROW) {
        printf("Name: %s\n", sqlite3_column_text(res, 0));
        printf("Author: %s\n", sqlite3_column_text(res, 1));
        printf("Price: %f\n", sqlite3_column_double(res, 2));
        printf("Category: %s\n", sqlite3_column_text(res, 3));
        printf("Genre: %s\n", sqlite3_column_text(res, 4));
    }

    return 0;
}


int CreateBook(struct Book* book, FILE *fp1) {
  int booksize;
  booksize = sizeof(book);

  fseek(fp1, 0, SEEK_END);
  printf("Enter book Name : ");
  scanf("%s", &book->name);
  printf("Enter Book Author : ");
  scanf("%s", &book->author);
  printf("Enter Book Price : ");
  scanf("%f", &book->price);
  printf("Enter Book Category : ");
  scanf("%s", &book->category);
  printf("Enter Book Genre : ");
  scanf("%s", &book->genre);
  fwrite(&book,booksize,1,fp1);
  return 0;
}
