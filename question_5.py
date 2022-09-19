# Write a program that takes the name of a text file,
# reads from the file and displays the number of lines in that file.
def num_line(filename):
   with open(filename) as f:
      read_text= f.readlines()
      print(read_text)
      x= len(read_text)
      print(f"The number of lines are {x}")   

num_line("texsttt.txt")



# with open("texsttt.txt") as f:
#    read_text= f.readlines()
#    for index, value in enumerate(read_text, 1):
#       print(f"{value}{index}")
#    # print(read_text)
#    # print(len(read_text))