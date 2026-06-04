def write_file():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")
    print("Message written to file successfully")
write_file()
