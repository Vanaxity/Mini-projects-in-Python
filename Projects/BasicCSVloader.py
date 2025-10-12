import os
import csv

#replace it with your own path
file_path = "C:/Users/ruchi/Desktop/Marks - Sheet1.csv"

try: 
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for things in content:
            print(things)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you do not have permission to open this file")