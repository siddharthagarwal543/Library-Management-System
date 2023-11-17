import streamlit as st
import re

class BookManager:
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

        return found_records

    def add_new_book(self, author, title, quantity):
        for record in self.database:
            if record['author'] == author and record['title'] == title:
                st.warning("Book already exists!")
                return
        self.database.append({'author': author.capitalize(), 'title': title.capitalize(), 'quantity': quantity, 'status': 'available'})
        st.success("Book added successfully!")

    def issue(self, author, title):
        pattern1 = re.compile('^'+author, re.IGNORECASE)
        pattern2 = re.compile('^'+title, re.IGNORECASE)
        for record in self.database:
            if pattern1.match(record['author']) and pattern2.match(record['title']):
                if record['quantity'] == 0:
                    st.warning("No books available!")
                    return
                record['quantity'] -= 1
                if record['quantity'] == 0:
                    record['status'] = 'Not Available'
                st.success("Book issued successfully!")
                return
        st.error("Book not found in the database!")

    def book_return(self, author, title):
        for record in self.database:
            if record['author'].upper() == author.upper() and record['title'].upper() == title.upper():
                record['quantity'] += 1
                if record['quantity'] == 1:
                    record['status'] = 'Available'
                st.success('Book successfully returned!')
                return
        st.warning("Enter valid details!")

book_manager = BookManager()

st.title('Library Management System')

choice = st.sidebar.radio("Choose an option:", ('Add New Book', 'Search and Issue', 'Return'))

if choice == 'Add New Book':
    st.subheader('Add New Book')
    author = st.text_input("Enter author name:")
    title = st.text_input("Enter book title:")
    quantity = st.number_input("Enter quantity:", value=1)
    if st.button("Add Book"):
        book_manager.add_new_book(author, title, quantity)

elif choice == 'Search and Issue':
    st.subheader('Search and Issue')
    option_2 = st.radio("Search by:", ('Author', 'Title'))

    if option_2 == 'Author':
        author = st.text_input("Enter author name:")
        if st.button("Search"):
            found_records = book_manager.search(1, author)
            for record in found_records:
                st.write(f"Author: {record['author']}")
                st.write(f"Title: {record['title']}")
                st.write(f"Quantity: {record['quantity']}")
                st.write(f"Status: {record['status']}")
                st.markdown("---")

            title_issue = st.text_input("Enter book title you want to issue:")
            if st.button("Issue Book"):
                book_manager.issue(author, title_issue)

    elif option_2 == 'Title':
        title = st.text_input("Enter book title:")
        if st.button("Search"):
            found_records = book_manager.search(2, title)
            for record in found_records:
                st.write(f"Author: {record['author']}")
                st.write(f"Title: {record['title']}")
                st.write(f"Quantity: {record['quantity']}")
                st.write(f"Status: {record['status']}")
                st.markdown("---")

            author_issue = st.text_input("Enter author name you want to issue:")
            if st.button("Issue Book"):
                book_manager.issue(author_issue, title)

else:
    st.subheader('Return')
    author_return = st.text_input("Enter author name:")
    title_return = st.text_input("Enter book title:")
    if st.button("Return Book"):
        book_manager.book_return(author_return, title_return)

book_manager.write_database_to_file()
