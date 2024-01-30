class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_isbn(self):
        return self.isbn
    
    def display(self):
        print("Title:", self.title, "\nAuthor:", self.author, "\nISBN:", self.isbn, "\n")


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, isbn):
        removed = False
        for book in self.books:
            if book.get_isbn() == isbn:
                self.books.remove(book)
                print("Book with ISBN", isbn, "removed from the library.")
                removed = True
                break
        if not removed:
            print("Book with ISBN", isbn, "not found in the library.")
    
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                book.display()


def main():
    library = Library()

    print("Enter books for the library. Enter 'done' to finish.")

    while True:
        title = input("Enter title (or 'done' to finish): ")
        if title == "done":
            break

        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")

        new_book = Book(title, author, isbn)
        library.add_book(new_book)

    while True:
        library.display_books()
        isbn = input("Enter ISBN to remove a book (or 'exit' to stop): ")
        if isbn == "exit":
            print("Exiting the program.")
            break
        library.remove_book(isbn)


if __name__ == "__main__":
    main()
