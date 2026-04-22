#text_file_search.py
word = input("Search word: ")

with open("file.txt") as f:
    for i, line in enumerate(f, 1):
        if word in line:
            print(f"Line {i}: {line}")
