books = [
    ("Atomic Habits", "James Clear", 2018, [
        (1, "The Surprising Power of Atomic Habits"),
        (2, "How Your Habits Shape Your Identity"),
        (3, "How to Build Better Habits")
    ]),
    
    ("Deep Work", "Cal Newport", 2016, [
        (1, "Deep Work is Valuable"),
        (2, "Deep Work is Rare"),
        (3, "Deep Work is Meaningful")
    ]),
    
    ("Clean Code", "Robert Martin", 2008, [
        (1, "Clean Code"),
        (2, "Meaningful Names"),
        (3, "Functions")
    ]),
    
    ("The Pragmatic Programmer", "Andrew Hunt", 1999, [
        (1, "A Pragmatic Philosophy"),
        (2, "A Pragmatic Approach"),
        (3, "The Basic Tools")
    ]),
    
    ("Python Crash Course", "Eric Matthes", 2019, [
        (1, "Getting Started"),
        (2, "Variables and Data Types"),
        (3, "Introducing Lists")
    ])
]


CHAPTER_INDEX_LIST = 3
CHAPTER_SELECT_INDEX = 1
while True:
    for index,(title,author,year,chapters) in enumerate(books):
        print(f"{index+1} : {title}")
    print("6 : Search Author")
    print("7 : Search Chapter")
    print("0 : Exit")

    # Print author and year when user selects book
    choice = int(input("Choose a book "))

    if 1 <= choice <= len(books) :    
       print(f"You selected {books[choice-1][0]}\nAuthor: {books[choice-1][1]}\n Year : {books[choice-1][2]}")
       chapters = books[choice-1][CHAPTER_INDEX_LIST]

       for index,(chapter_no,chapter) in enumerate(chapters):
           print(f"{chapter_no} : {chapter}")

       choice_chapter = int(input("Choose a chapter"))
       if 1 <= choice_chapter <= len(chapters):
            title, author, year, chapters = books[choice-1]

            print(f"You selected {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")

            while True :
                for chapter_no, chapter in chapters:
                    print(f"{chapter_no} : {chapter}")
                choice_chapter = int(input("Choose a chapter: "))

                if 1 <= choice_chapter <= len(chapters):
                    selected_chapter = chapters[choice_chapter-1][CHAPTER_SELECT_INDEX]
                    print(f"Reading {selected_chapter}")
                    print("*"*40)

                    another_choice = input("Read another chapter from this book? (y/n): ")
                    if another_choice.lower() == "n":
                       break
                else:
                    print("Invalid chapter")
          
    # Print author and year when user selects book
    elif choice == 0:
        print("Exit")
        break


    elif choice == 6:
        author_name = input("Enter author name for search ")
        found = 0
        for title,author,year,chapters in books:
            if author_name.casefold() == author.casefold():
                print(f"{title} by {author_name}")
                found = 1
        if not found:
            print("Author Not found")

    elif choice == 7:
        keyword = input("Enter keyword for search ")
        found = 0
        for title,author,year,chapters in books:
            if keyword.casefold() in title.casefold():
                print(title)
                for index,chapter in chapters :
                    found = 1
                    if keyword.casefold() in chapter.casefold():
                       print(f"{title} -> {chapter}")
        if not found :
            print("Keyword not found")
    else:
        break