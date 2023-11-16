import re



# database = []

def read_database_from_file():
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
                database.append(book_info)
        return database
    except FileNotFoundError:
        return []

def write_database_to_file(database):
    with open("book_database.txt", "w") as file:
        for record in database:
            file.write(','.join(record) + '\n')
    return

def search(option_1, option_2):
    found_records = []
    if option_1 == 1:
        pattern = re.compile('^' + option_2, re.IGNORECASE) 
        found_records = [record for record in database if pattern.match(record['author'])]
    else:
        pattern = re.compile('^' + option_2, re.IGNORECASE)
        found_records = [record for record in database if pattern.match(record['title'])]

    for record in found_records:
        print(record['title'], " ", record['author'], " ", record['quantity'], " ", record['status'])

def issue(author, title):
    pattern1=re.compile('^'+author,re.IGNORECASE)
    pattern2=re.compile('^'+title,re.IGNORECASE)
    for record in database:
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

def book_return(author, title):
    for record in database:
        if record['author'].upper() == author.upper() and record['title'].upper() == title.upper():
            record['quantity'] += 1
            if record['quantity'] == 1:
                record['status'] = 'Available'
            print('Book successfully returned!')
            return
    print("Enter valid details!")
    return

database = read_database_from_file() 
choice=1
while choice==1 or choice==2:
    choice = int(input("Enter:\n1 for Search and Issue\n2 for Return\n Any other number for exiting\n"))

    if choice == 1:
        option_2 = int(input("Enter:\n1 for Author\n2 for Title\n"))
        if option_2 == 1:
            author = input("Enter author name: ")
            search(option_2, author)
            title = input("Enter book title you want to issue: ")
            issue(author, title)

        elif option_2 == 2:
            title = input("Enter Book Title: ")
            search(option_2, title)
            author = input("Enter author name you want to issue: ")
            issue(author, title)

    elif choice == 2:
        author = input("Enter author name: ")
        title = input("Enter Book title: ")
        book_return(author, title)
    else:
        break
write_database_to_file(database)