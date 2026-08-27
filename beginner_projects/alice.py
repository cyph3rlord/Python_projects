
file_name = "alice.txt"
try:
 
  with open(file_name) as file_object:
     contents = file_object.read()

except FileNotFoundError:
    print(f"The file name {file_nmae}, does not exist.")
else:
    words = contents.split()
    print(len(f"The book Alice in Wonderland has {words} words."))
