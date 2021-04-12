def main(): # main function 
    displayMainMenu() # call displayMainMenu() function 
    while True: # while true statement 
        try:    # start try block 
            option = int(input("Please select an option from the above: "))  # prompt user to enter the option as given in the menu 
        except ValueError: # except block 
            print("String or empty value is not allowed")  #exception  handling message 
        if option == 1: 
            writeBookInfo()     # call writeBookInfo() function if user enters option 1 
        elif option == 2: 
            book_listed = readBookInfo() # get the return value of readBookInfo() function to book_listed when user enters option 2 
            displayBookList(book_listed) # call displayBookList(book_listed) function and pass book_listed as argument 
        elif option == 3: 
            issueBook() # call issueBook() function if user enter option 3 
        elif option == 4: 
            issued_book_list = readIssuedBook() # get the return value of readIssuedBook() function to issued_book_list when user enters option 4 
            displayIssuedBookList(issued_book_list) # call displayIssuedBookList(issued_book_list) function and pass issued_book_list as argument 
        elif option == 5: 
            returnBook() # call returnBook() function if user enter option 5 
        else: 
            print("""Thanks for using the library management software 
                     See you again!""") # print see you again message if the user enter option 6 or more 
            break # terminate the program 
 
def writeBookInfo(): # writeBookInfo function 
    stored_book_information = {}    # initialize empty dictionary 
    continue_or_not = 'Y' # initialize the "Y" to continue or not 
    while continue_or_not == 'Y': # while condition if continue_or_not is equal to "Y" 
        book_call_no = callbookInput(stored_book_information) # call callBookInput method and pass the dictionary as argument to validate the book_call_no 
        book_name = input("Enter book name: ") # Get book name from user 
        author_name = input("Enter author name: ")  # Get author name from user 
        try: # try block 
            published_year = int(input("Enter book publish year: ")) # get published year as int 
            book_quantity = int(input("Enter book quantity: ")) # get book quantity as int 
        except ValueError: 
            print("String value not allowed") # Error handling to check that string values are not allowed 
        book_info_file = open("book.txt", "a") # Open the book.txt file and use "a" to write on the file 
        book_info_file.write(str(book_call_no) + ",")  # write book_call_no to file and separating with commas 
        book_info_file.write(str(book_name) + ",")  # write book_name to file and separating with commas 
        book_info_file.write(str(author_name) + ",")  # write author_name to file and separating with commas 
        book_info_file.write(str(published_year) + ",")  # write published_year to file and separating with commas 
        book_info_file.write(str(book_quantity) + "\n")  # write book_quantity to file and separating with \n for start of next line 
        stored_book_information[book_call_no] = [book_name, author_name, published_year, book_quantity] # passing the book_call_no as key and book details as list to the dictionary we have created 
        book_info_file.close() # close the book file 
        print("The details of the book you entered are as follows:") # print book details message 
        print("Book callno: ", book_call_no) 
        print("Book name: ", book_name) 
        print("Author name: ", author_name) 
        print("Enter publish year: ", published_year) 
        print("Quantity: ", book_quantity) 
        print("The record has been successfully added to the books.txt file") 
        continue_or_not = input("Do you want to enter details for another book (Y/N)?") # prompt user to continue adding for book to the file 
    displayMainMenu() 
 
 
def readBookInfo(): # readBookInfo() function 
    read_stored_book_information = {}   # Initialize empty dictionary 
    book_read_file = open("book.txt", "r") # open the book.txt file and read 
    for line in book_read_file: # for loop to read each line 
        book_info_field = line.rsplit(",") # split the value stored in the text file with commas 
        book_call_no = book_info_field[0] # assign value first value from the file to book_call_no 
        book_name = book_info_field[1]  # assign value second value from the file to book_name 
        book_author = book_info_field[2]    # assign value third value from the file to book author 
        published_year = book_info_field[3] # assign value fourth value from the file to published year 
        book_quantity = book_info_field[4]  # # assign value fifth value from the file to book_quantity 
        read_stored_book_information[book_call_no] = [book_name, book_author, published_year, book_quantity] # pass the values read from the text file to read_stored_book_information 
    book_read_file.close() # close the book.txt file 
    return read_stored_book_information # return the read_stored_book_information dictionary 
 
 
def issueBook(): # issue book 
    book_found = True # initialize book_found Boolean as True 
    continue_or_not = 'Y' # initialize the "Y" to continue or not 
    available_stored_books = readBookInfo()  # assign the return value of readBookInfo() to available_stored_books 
    print(""" 
     ----------------------------------------------   
            Issue Book      
     --------------------------                              
     """) 
    while continue_or_not == 'Y': # continue the loop until the value of continue_or_not is equal to "Y" 
        try: # try block 
            bookCallno = int(input("Enter book callno: ")) 
            book_name = input("Enter book name: ") 
        except ValueError: 
            print("String or empty value is not allowed") # error message to handle if string or empty value are passed to book callno 
        for key, value in available_stored_books.items():   # for loop to check the keys and values in available_stored_books dictionary 
            bookCall = int(key) # assign int key value to bookCall variable 
            available_booK_name = value[0] # assign the list value in position 0 to available_booK_name variable 
            total_available_books = int(value[3]) # assign the int list value in position 3 to total_available_books 
            if bookCallno == bookCall and available_booK_name == book_name and total_available_books > 1: # check if the user entered book call number, book name and the available book is more than 1 
                student_id = input("Enter student ID: ") # get student id from user 
                student_name = input("Enter student name: ") # get student name from user 
                return_date = input('Enter return dat in YYYY-MM-DD format: ') # get return from user 
                print("The book quantity was ", total_available_books) 
                updated_available_books = total_available_books - 1 # Updating the book quantity when the book it borrowed 
                print("Updated book quantity is ", updated_available_books) 
                book_issued_file = open("issuedBook.txt", "a") # opening the issuedBook.txt file and writing issued book details 
                book_issued_file.write(str(bookCallno) + ",")   # writing bookCallno to issuedBook.txt file 
                book_issued_file.write(str(book_name) + ",")    # writing book_name to issuedBook.txt file 
                book_issued_file.write(str(student_id) + ",")   # writing student_id to issuedBook.txt file 
                book_issued_file.write(str(student_name) + ",") # writing student_name to issuedBook.txt file 
                book_issued_file.write(str(return_date) + "\n") # writing return_date to issuedBook.txt file 
                print("Book issued successfully") # print book successfully issued message 
                available_stored_books["1"][3] = str(updated_available_books) # update the available books after issuing 
                print("The new updated book list is ", available_stored_books) 
                book_issued_file.close() # close the book file 
                book_found = True # set book_found to True 
                break # Terminate the if condition 
            else: 
                book_found = False # set book_found to False 
        if book_found is False: # check if book_found is False and print error message 
            print("The book you are searching is not found") 
        continue_or_not = input("Do you want to issue another book (Y/N)? ") # prompt user to either continue the program or not 
    displayMainMenu() 
 
 
def readIssuedBook(): # readIssueBook() function that return book_issued_list 
    book_issued_list = {} # initialize an empty dictionary 
    read_issued_book = open("issuedBook.txt", "r")   # open the issuedBook.txt file and read 
    for line in read_issued_book: # for loop to check each line in issuedBook.txt file 
        book_issued_field = line.rsplit(",") # use rsplit method in line function to separate the value in the text file 
        bookCallno = book_issued_field[0] # assign value first value from the file to book_call_no 
        book_name = book_issued_field[1] # assign value second value from the file to book_name 
        student_ID = book_issued_field[2] # assign value third value from the file to Student Id 
        student_Name = book_issued_field[3] # assign value fourth value from the file to student_Name 
        return_date = book_issued_field[4] # assign value fifth value from the file to  return_date 
        book_issued_list[bookCallno] = [book_name, student_ID, student_Name, return_date] # enter the above value in the dictionary with bookcallno as key and other value as list of issued books 
    read_issued_book.close() 
    return book_issued_list # return book_issued_list as dictionary 
 
 
def displayIssuedBookList(display_booklist): # displayIssuedBookList function that takes display_bookList as argument 
    print(""" 
     ---------------------------------------------- 
        List issued Books 
     -------------------------- 
     ============================================================================ 
      Callno      Book Name          Student ID     Students Name       Return Date 
     ============================================================================ 
 
           """) 
    for key, value in display_booklist.items(): # for loop to check all the keys and values in display_booklist dictionary and display them as follows 
        print('{:^20}   {:^10}   {:^15}   {:^10} {:^20}'.format(key, value[0], value[1], value[2], value[3])) 
    displayMainMenu() 
 
 
def returnBook(): # readbook() function 
    continue_or_not = 'Y' 
    book_issued = readIssuedBook()  # initialize the book_issued as return value from readIssuedBook() function 
    books_available = readBookInfo()  # initialize the books available as return value from readBookInfo() function 
    print(""" 
    ----------------------- 
     Return Book 
    ----------------------- 
     """) 
    while continue_or_not == 'Y': # while loop continues if the continue_or_not value is equal to 'Y' 
        try: 
            book_Call = int(input("Enter book callno: ")) # get user input for call no 
        except ValueError: 
            print("String or empty value are not allowed") 
        student_Id = input("Enter student ID: ") # get user input for student id 
        for key, value in book_issued.items(): # for loop to check all the keys and values in book_issued dictionary 
            bookCallNumber = int(key)   # assign the key value to bookCallNumber variable 
            studentId = value[1] # assign the list value in position 1 to studentId variable 
            if book_Call == bookCallNumber and student_Id == studentId: # check if the user enter book call number and student Id matches 
                removed_books_issued = book_issued.pop(str(book_Call))  # remove from dict and return value 
                print("Book returned successfully") # print message from successfully returning the book 
        for key, value in books_available.items(): # for loop to check all the keys and values in book available dictionary 
            bookCallNo = int(key)  # assign the key value to bookCallNo variable 
            book_quantity = int(value[3]) # assign the list value in position 3 to book_quantity variable 
            if book_Call == bookCallNo: # check if user enter book call number matches the existing book call number in the dictionary 
                updated_book_quanitity = book_quantity + 1 #add the returned book 
                print("The book quantity was ", book_quantity) 
                print("The updated book quantity is ", updated_book_quanitity) 
        books_available["1"][3] = str(updated_book_quanitity) # update the dictionary with the returned book 
        print("The new updated book list is ", books_available) 
        continue_or_not = input("Do you want to return another book (Y/N)? ") # prompt user to continue to return other books or not 
    displayMainMenu() 
 
 
def callbookInput(data_dict):   # callBookInput() function that takes dictionary as argument and return callbook_no 
    while True: 
        callbook_no = input('Enter Callbook no: ') # prompt user to enter the Call book no 
        if not callbook_no.isdigit():   # check if the user input is digit or not 
            print('Callbook no can be numeric only. Try again') # print error message if the user input is no numerical 
        elif callbook_no in data_dict:  # Check if the call book no exist in the dictionary or not 
            print('Callbook no already exists. Try again') # error message showing that the callbook no already exist 
        else: 
            return callbook_no # return callbook_no if all the condition are met 
 
 
def displayBookList(stored_book_information): # displayBookList() function to display the book that are available 
    print(""" 
    ---------------------------------------------- 
        List Available Books 
    ------------------------- 
     ========================================================================= 
       Callno        Name        Author        Publish Year       Quantity 
     ========================================================================= 
     """) 
    for key, value in stored_book_information.items(): # for loop to check the all the key and values in stored_book_information dictionary that is received via argument and display them 
        print('{:^17}   {:^10}   {:^15}   {:^10} {:^20}'.format(key, value[0], value[1], value[2], value[3])) 
    displayMainMenu() 
 
 
def displayMainMenu(): # displayMainMenu() function for library management software 
    print(""" 
    ================================= 
      LIBRARY MANAGEMENT SOFTWARE            
         MAIN MENU 
    ================================== 
    <1> Add book 
    <2> List Available Books 
    <3> Issue Book 
    <4> List Issued Books 
    <5> Return Book 
    <6> Exit 
    =================================== 
 
    """) 
 
 
main() 
 