import subprocess

while True:
    print("""
    Choose an option:
    1. Search Wikipedia by search term
    2. Search Wikipedia by URL
    3. Exit
    """)
    choice = input("Enter choice: ")

    if choice == '1':
        search_term = input("Enter search term: ")
        subprocess.call(["python", "wiki.py", "--search", search_term])
    elif choice == '2':
        url = input("Enter URL: ")
        subprocess.call(["python", "wiki.py", "--url", url])
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")