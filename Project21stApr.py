# project 2: Library management from user and admin ends
# user borrow return, available books for 1 month
#admin Load check stop penalty

ifBorrower="Borrower"
ifAdmin="Admin"
#userChoice=Continue
#userChoice2=Exit

Book1,Book2,Book3,Book4,Book5,Book6,Book7,Book8,Book9,Book10="Python Crash Course","Head-First Python (2nd edition)","Learn Python the Hard Way (3rd Edition)","Python Programming: An Introduction to Computer Science (3rd Edition)","Learning with Python: How to Think Like a Computer Scientist","A Byte of Python","Introduction to Machine Learning with Python: A Guide for Data Scientists","Fluent Python: Clear, Concise, and Effective Programming","Python Cookbook: Recipes for Mastering Python 3","Programming Python: Powerful Object-Oriented Programming"

"""def userSelectionfunction():
    userBorrow=input('''Which python book do you want?
                 Available choice are:
                 1> Python Crash Course
                 2> Head-First Python (2nd edition)
                 3> Learn Python the Hard Way (3rd Edition)
                 4> Python Programming: An Introduction to Computer Science (3rd Edition)
                 5> Learning with Python: How to Think Like a Computer Scientist
                 6> A Byte of Python
                 7> Introduction to Machine Learning with Python: A Guide for Data Scientists
                 8> Fluent Python: Clear, Concise, and Effective Programming
                 9> Python Cookbook: Recipes for Mastering Python 3
                 10> Programming Python: Powerful Object-Oriented Programming
                 : ''')"""
#Number of books available
book1Count=book2Count=book3Count=book4Count=book5Count=book6Count=book7Count=book8Count=book9Count=book10Count=10

import datetime

today = datetime.date.today()
future_day = today.day
future_month = (today.month + 1) % 12
future_year = today.year + ((today.month + 1) // 12)
one_month_later = datetime.date(future_year, future_month, future_day)


userDetail=input("Please select if you are a borrower or admin? Type in uppercase BORROWER OR ADMIN")

if userDetail=="BORROWER":
    userBooksBorrowedCount=0
    while  userBooksBorrowedCount<=2:
        userBorrow=input('''Which python book do you want?
                     Available choice are:
                     1> Python Crash Course
                     2> Head-First Python (2nd edition)
                     3> Learn Python the Hard Way (3rd Edition)
                     4> Python Programming: An Introduction to Computer Science (3rd Edition)
                     5> Learning with Python: How to Think Like a Computer Scientist
                     6> A Byte of Python
                     7> Introduction to Machine Learning with Python: A Guide for Data Scientists
                     8> Fluent Python: Clear, Concise, and Effective Programming
                     9> Python Cookbook: Recipes for Mastering Python 3
                     10> Programming Python: Powerful Object-Oriented Programming
                     : ''')
        if userBooksBorrowedCount<=2:
            if userBorrow==Book1 or userBorrow==Book2 or userBorrow==Book3 or userBorrow==Book3 or userBorrow==Book4 or userBorrow==Book5 or userBorrow==Book6 or userBorrow==Book7 or userBorrow==Book8 or userBorrow==Book9 or userBorrow==Book10:
                print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                userBooksBorrowedCount=userBooksBorrowedCount+1
            else:
                print("This book is not available")
                continue

            if userBorrow==Book1:
                book1Count=book1Count-1
            elif userBorrow==Book2:
                book2Count=book2Count-1
            elif userBorrow==Book3:
                book3Count=book3Count-1
            elif userBorrow==Book4:
                book4Count=book4Count-1
            elif userBorrow==Book5:
                book5Count=book5Count-1
            elif userBorrow==Book6:
                book6Count=book6Count-1
            elif userBorrow==Book7:
                book7Count=book7Count-1
            elif userBorrow==Book8:
                book8Count=book8Count-1
            elif userBorrow==Book9:
                book9Count=book9Count-1
            elif userBorrow==Book10:
                book10Count=book10Count-1

            print("Total number of books that a member can available is 2")
            print("Number of books you have borrowed is:               ", userBooksBorrowedCount)
            user2ndSelection=input("DO YOU NEED ANOTHER BOOK? Please enter your selection YES/NO in uppercase")
    
            if user2ndSelection=="YES":
                userBooksBorrowedCount=userBooksBorrowedCount+1
                print("CURRENT BOOK AVAILABILITY STATUS")
                print("1)  Python Crash Course                                                           - Availability:" ,book1Count)
                print("2)  Head-First Python (2nd edition)                                               - Availability:" ,book2Count)
                print("3)  Learn Python the Hard Way (3rd Edition)                                       - Availability:" ,book3Count)
                print("4)  Python Programming: An Introduction to Computer Science (3rd Edition)         - Availability:" ,book4Count)
                print("5)  Learning with Python: How to Think Like a Computer Scientist                  - Availability:" ,book5Count)
                print("6)  A Byte of Python                                                              - Availability:" ,book6Count)
                print("7)  Introduction to Machine Learning with Python: A Guide for Data Scientists     - Availability:" ,book7Count)
                print("8)  Fluent Python: Clear, Concise, and Effective Programming                      - Availability:" ,book8Count)
                print("9)  Python Cookbook: Recipes for Mastering Python 3                               - Availability:" ,book9Count)
                print("10) Programming Python: Powerful Object-Oriented Programming                      - Availability:" ,book10Count)

                userNewSelection=input("What would be your selection amongst the above available books?")
                if userNewSelection==Book1:
                    if book1Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book1Count=book1Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book2:
                    if book2Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book2Count=book2Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book3:
                    if book3Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book3Count=book3Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book4:
                    if book4Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book4Count=book4Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book5:
                    if book5Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book5Count=book5Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book6:
                    if book6Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book6Count=book6Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book7:
                    if book7Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book7Count=book7Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book8:
                    if book8Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book8Count=book8Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book9:
                    if book9Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book9Count=book9Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                elif userNewSelection==Book10:
                    if book10Count>=1:
                        print("This book is issued to you on" ,datetime.date.today(),".", "You need to return it by", one_month_later, ". Else, you will have to fined")
                        book10Count=book10Count-1
                        print("Total number of books you have borrowed:",  userBooksBorrowedCount)
                    else:
                        print("Sorry someone has already taken this book")
                    
            elif user2ndSelection=="NO": 
                print("Thank you,please visit us again")
            elif user2ndSelection!="YES" or user2ndSelection!="NO":
                print("Please enter a valid selection")
                continue
            break
        else:
            print("You already have ",userBooksBorrowedCount, "books. Maximum number allowed of books allowed to borrower: 2") 
        #print("Total number of books you have borrowed:",  userBooksBorrowedCount)
        
    
        '''booksAvailabilityStatusCheck=input("Do you want to check the updated status? Please enter your selection YES/NO in uppercase")
        if booksAvailabilityStatusCheck=="YES":
            print("UPDATED BOOKS AVAILABILITY STATUS")
            print("1)  Python Crash Course                                                           - Availability:" ,book1Count)
            print("2)  Head-First Python (2nd edition)                                               - Availability:" ,book2Count)
            print("3)  Learn Python the Hard Way (3rd Edition)                                       - Availability:" ,book3Count)
            print("4)  Python Programming: An Introduction to Computer Science (3rd Edition)         - Availability:" ,book4Count)
            print("5)  Learning with Python: How to Think Like a Computer Scientist                  - Availability:" ,book5Count)
            print("6)  A Byte of Python                                                              - Availability:" ,book6Count)
            print("7)  Introduction to Machine Learning with Python: A Guide for Data Scientists     - Availability:" ,book7Count)
            print("8)  Fluent Python: Clear, Concise, and Effective Programming                      - Availability:" ,book8Count)
            print("9)  Python Cookbook: Recipes for Mastering Python 3                               - Availability:" ,book9Count)
            print("10) Programming Python: Powerful Object-Oriented Programming                      - Availability:" ,book10Count)
        else:
            print("OK")'''

    else:
        print("You have borrowed booked",userBooksBorrowedCount," books")
     
if userDetail=="ADMIN":
    booksAvailabilityStatusCheck=input("Do you want to check the updated status? Please enter your selection YES/NO in uppercase")
    if booksAvailabilityStatusCheck=="YES":
        print("BOOKS AVAILABILITY STATUS")
        print("1)  Python Crash Course- Availability:" ,book1Count)
        print("2)  Head-First Python (2nd edition)- Availability:" ,book2Count)
        print("3)  Learn Python the Hard Way (3rd Edition):" ,book3Count)
        print("4)  Python Programming: An Introduction to Computer Science (3rd Edition):" ,book4Count)
        print("5)  Learning with Python: How to Think Like a Computer Scientist:" ,book5Count)
        print("6)  A Byte of Python:" ,book6Count)
        print("7)  Introduction to Machine Learning with Python: A Guide for Data Scientists:" ,book7Count)
        print("8)  Fluent Python: Clear, Concise, and Effective Programming:" ,book8Count)
        print("9)  Python Cookbook: Recipes for Mastering Python 3:" ,book9Count)
        print("10) Programming Python: Powerful Object-Oriented Programming:" ,book10Count)
    else:
        print("OK")

    import datetime
    bookReturnDate=input("Please enter the book return date by the borrower in YYYY-MM-DD format")
    try:
        formatStrToDate=datetime.datetime.strptime(bookReturnDate,"%Y-%m-%d").date()
        numberOfDays=formatStrToDate-today
        if formatStrToDate>one_month_later:
            print("Borrower kept the book for ", numberOfDays, ". He needs to pay fine of Rs 5 per exceeding day")
        else:
            print("Thank you")

    except:
        print("Enter date in YYYY-MM-DD format")
    
    
