import re

class libraryManager:
    def __init__(self):
        self.database = self.read_database_from_file()

    def read_database_from_file(self):
        database = []
        try:
            with open("database.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    record = line.strip().split(",")
                    book_info = {
                        'author': record[0],
                        'title': record[1],
                        'quantity': int(record[2]),
                        'status': record[3]
                    }
                    print(book_info)
                    database.append(book_info)
            return database
        except FileNotFoundError:
            return []

    def write_database_to_file(self):
        with open("database.txt", "w") as file:
            for record in self.database:
                res=""
                for key in record:
                    res+=str(record[key])
                    if key=='status':
                        res+="\n"
                    else:
                        res+=","
                file.write(res)

    def search(self, option_1, option_2):
        found_records = []
        if option_1 == 1:
            pattern = re.compile('^' + option_2, re.IGNORECASE) 
            found_records = [record for record in self.database if pattern.match(record['author'])]
        else:
            pattern = re.compile('^' + option_2, re.IGNORECASE)
            found_records = [record for record in self.database if pattern.match(record['title'])]

        for record in found_records:
            print(record['title'], " ", record['author'], " ", record['quantity'], " ", record['status'])

    def add_new_book(self, author, title, quantity):
        for record in self.database:
            if record['author'] == author and record['title'] == title:
                record['quantity']+=quantity
                print("Book already there so qunatity updated!")
                return
        self.database.append({'author': author, 'title': title, 'quantity': quantity, 'status': 'available'})
        print("New Book added successfully!")

    def issue(self, author, title):
        pattern1 = re.compile('^'+author, re.IGNORECASE)
        pattern2 = re.compile('^'+title, re.IGNORECASE)
        for record in self.database:
            if pattern1.match(record['author']) and pattern2.match(record['title']):
                if record['quantity'] == 0:
                    print("No books available!")
                    return
                record['quantity'] -= 1
                if record['quantity'] == 0:
                    record['status'] = 'Not Available'
                print("Book issued successfully!")
                return
        print("Book not found in the database!")

    def book_return(self, author, title):
        for record in self.database:
            if record['author'].upper() == author.upper() and record['title'].upper() == title.upper():
                record['quantity'] += 1
                if record['quantity'] == 1:
                    record['status'] = 'Available'
                print('Book successfully returned!')
                return
        print("Enter valid details!")

library_manager = libraryManager()

choice = 1
while choice in (0, 1, 2):
    choice = int(input("Enter:\n0 for Adding New Book \n1 for Search and Issue\n2 for Return\n Any other number for exiting\n"))
    if choice == 0:
        author = input('Enter author name: ')
        title = input('Enter book title: ')
        quantity = int(input('Enter quantity: '))
        library_manager.add_new_book(author, title, quantity)
    elif choice == 1:
        option_2 = int(input("Enter:\n1 for Author\n2 for Title\n"))
        if option_2 == 1:
            author = input("Enter author name: ")
            library_manager.search(option_2, author)
            title = input("Enter book title you want to issue: ")
            library_manager.issue(author, title)
        elif option_2 == 2:
            title = input("Enter Book Title: ")
            library_manager.search(option_2, title)
            author = input("Enter author name you want to issue: ")
            library_manager.issue(author, title)
    elif choice == 2:
        author = input("Enter author name: ")
        title = input("Enter Book title: ")
        library_manager.book_return(author, title)
    else:
        break

library_manager.write_database_to_file()
