database = [
    {'author': 'John Doe', 'title': 'The Mystery of Life', 'quantity': 3, 'status': 'Available'},
    {'author': 'Jane Smith', 'title': 'Into the Unknown', 'quantity': 0, 'status': 'Not Available'},
    {'author': 'Michael Johnson', 'title': 'Echoes in the Wind', 'quantity': 5, 'status': 'Available'},
    {'author': 'Emily Brown', 'title': 'Whispers in the Dark', 'quantity': 1, 'status': 'Available'},
    {'author': 'David Clark', 'title': 'Lost and Found', 'quantity': 2, 'status': 'Available'},
    {'author': 'John Doe', 'title': 'The Secret Key', 'quantity': 2, 'status': 'Available'},
    {'author': 'John Doe', 'title': 'The Hidden Path', 'quantity': 4, 'status': 'Available'},
    {'author': 'Michael Johnson', 'title': 'Echoes in the Wind', 'quantity': 3, 'status': 'Available'},
    {'author': 'Emily Brown', 'title': 'Whispers in the Dark', 'quantity': 2, 'status': 'Available'},
    {'author': 'David Clark', 'title': 'Lost and Found', 'quantity': 0, 'status': 'Not Available'}
]

def search(option_1, option_2):
    found_records = []
    if option_1 == 1:
        found_records = [record for record in database if record['author'] == option_2]
    else:
        found_records = [record for record in database if record['title'] == option_2]

    for record in found_records:
        print(record['title'], " ", record['author'], " ", record['quantity'], " ", record['status'])

def issue(author, title):
    for record in database:
        if record['author'] == author and record['title'] == title:
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
        if record['author'] == author and record['title'] == title:
            record['quantity'] += 1
            if record['quantity'] == 1:
                record['status'] = 'Available'
            print('Book successfully returned!')
            return
    print("Enter valid details!")
    return
    
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

# For printing the contents of the database
# for record in database:
#     print(record['author'], " ", record['title'], " ", record['quantity'], " ", record['status'])
