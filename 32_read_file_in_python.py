try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
except Exception:
    print("Something went wrong :(")
