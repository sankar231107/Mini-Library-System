library = {
    "The Alchemist": 3,
    "Harry Potter": 5,
    "Rich Dad Poor Dad": 4,
    "Wings of Fire": 2,
    "The Hobbit": 3,
    "Atomic Habits": 6,
    "Think and Grow Rich": 2,
    "Sherlock Holmes": 4,
    "Ikigai": 3,
    "The Power of Now": 2,
    "Naruto Manga": 5,
    "One Piece": 4,
    "Spider-Man Comics": 3,
    "Batman Comics": 2,
    "Avengers Comics": 3,
    "Physics Basics": 4,
    "Chemistry Guide": 3,
    "Mathematics Vol 1": 5,
    "Biology Essentials": 2,
    "Computer Science Intro": 4
}

while True:
    print("\nMini Library System")
    print("1. Show all books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Search book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nBooks and Quantity:")
        for book, qty in library.items():
            print(book, "- Copies:", qty)

    elif choice == "2":
        book = input("Enter book name to borrow: ")
        if book in library:
            if library[book] > 0:
                library[book] -= 1
                print("You borrowed:", book)
            else:
                print("No copies available!")
        else:
            print("Book not found!")

    elif choice == "3":
        book = input("Enter book name to return: ")
        if book in library:
            library[book] += 1
            print("You returned:", book)
        else:
            print("Book not found!")

    elif choice == "4":
        search = input("Enter book name to search: ")
        found = False
        for book in library:
            if search.lower() in book.lower():
                print(book, "- Copies:", library[book])
                found = True
        if not found:
            print("No matching books found!")

    elif choice == "5":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Try again.")
