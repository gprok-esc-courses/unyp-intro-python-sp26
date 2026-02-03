
print("==== MENU ====")
print("1. Open")
print("2. Save")
print("3. Delete")
print("0. EXIT")
choice = int(input("Select:> "))

if choice == 1:
    print("Openning file ...")
elif choice == 2:
    print("File saved.")
elif choice == 3:
    print("File deleted.")
elif choice == 0:
    print("bye!")
else:
    print("Invalid choice")