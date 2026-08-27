def count_words(file_name):
    """ Count the approximat number of words in a file"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"The file name {file_name}, does not exist.")
    else:
        words = contents.split()
        print(f"The file {file_name}, has {len(words)} words.")



file_names = ["alice.txt", "Siddhartha.txt", "mobydick.txt", "littlewoman.txt"]

for file_name in file_names:
    count_words(file_name)







