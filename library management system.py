class Book:
    def __init__(self,Book_ID,Title,Author,Genre,):
        self.Book_ID=Book_ID
        self.Title=Title
        self.Author=Author
        self.Genre=Genre
        self.Status="Available"

    def display_book(self):
        print("Book ID:",self.Book_ID,"Title:",self.Title,"Author:",self.Author,"Genre:",self.Genre,"Status:",self.Status)

    def borrow_book(self):
        if self.Status=="Available":
            self.Status="Borrowed"
            print("Book borrowed successfully")
        else:
            print("Sorry, Book is not available") 

    def return_book(self):
        if self.Status=="Borrowed":
            self.Status="Available"
            print("Book returned successfully")
        else:
            print("Sorry, Book is available")

    def is_available(self):
        return self.Status=="Available"

class Member:
    def __init__(self,memberid,name,phone):
        self.memberid=memberid
        self.name=name
        self.phone=phone
        self.borrowed_books=[]

    def display_member(self):
        print("memberid:",self.memberid,"name:",self.name,"phone:",self.phone)

        if len(self.borrowed_books)==0:
            print("no books borrowed")
        else:
            print("Books borrowed are:")
            for book in self.borrowed_books:
                print(book.Title)

    def borrow_book(self,book):
        self.borrowed_books.append(book)
        print(book.Title," is borrowed successfully.")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print("Book returned successfully")
        else:
            print("Book already available.")

class Library:
    def __init__(self):
        self.book=[]
        self.member=[]

    def add_book(self,book):
        self.book.append(book)
        print("book added successfully")

    def add_member(self,member):
        self.member.append(member)
        print("member registered successfully")

    def display_books(self):
        if len(self.book)==0:
            print("no books available")
        else:
            for book in self.book:
                book.display_book()
                print("_"*30)

    def display_members(self):
            if len(self.member)==0:
                print("no members registered")
            else:
                for member in self.member:
                    member.display_member()
                    print("_"*30)

    def search_book(self,book_id):
        for book in self.book:
            if book.Book_ID==book_id:
                return book
        return None

    def search_member(self,member_id):
            for member in self.member:
                if member.memberid==member_id:
                    return member
            return None

    def borrow_book(self,member_id,book_id):
        member=self.search_member(member_id)
        book=self.search_book(book_id)

        if member is None:
            print("member not found")
            return

        if book is None:
            print("book not found")
            return

        if book.Status=="Available":
            book.borrow_book()
            member.borrow_book(book)
        else:
            print("book is already borrowed")

    def return_book(self,member_id,book_id):
            member=self.search_member(member_id)
            book=self.search_book(book_id)
    
            if member is None:
                print("member not found")
                return
    
            if book is None:
                print("book not found")
                return
    
            if book in member.borrowed_books:
                book.return_book()
                member.return_book(book)
            else:
                print("This member did not borrow the book.")  

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Search Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        genre = input("Enter Genre: ")

        book = Book(book_id, title, author, genre)
        library.add_book(book)

    elif choice == 2:
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Member Name: ")
        phone = input("Enter Phone Number: ")

        member = Member(member_id, name, phone)
        library.add_member(member)

    elif choice == 3:
        library.display_books()

    elif choice == 4:
        library.display_members()

    elif choice == 5:
        book_id = int(input("Enter Book ID to search: "))

        book = library.search_book(book_id)

        if book:
            book.display_book()
        else:
            print("Book not found.")

    elif choice == 6:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        library.borrow_book(member_id,book_id)

    elif choice == 7:
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        library.return_book(member_id, book_id)

    elif choice == 8:
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Try again.")
    