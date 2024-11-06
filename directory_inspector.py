import os

def list_dir_cont(path):
    try:
        print(f"Okay, printing everything in that filepath. One sec..!\n{"*"*20}" )
        for line in os.listdir(path):
            print(line)
    except IOError as e:
        print(f"An error occurred: {e}")
    except PermissionError as e:
        print(f"Permission Error. Check your path.")
    except FileNotFoundError as e:
        print(f"File not found. Check your path.")
    except Exception as e:
        print(f"An unexpected erorr occured: {e}")

print(f"This program only runs once, so start over if you have any issues.")

path = input("Please input the file path: ")

list_dir_cont(path)