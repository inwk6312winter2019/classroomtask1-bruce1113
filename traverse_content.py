"""This is the traverse the content of home file"""

def traverse(directory):
    import os
    mylist = list()
    for files in os.listdir(directory):
        mylist.append(files)

    print(mylist)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    new_list = mylist
    print(new_list[::-1])



>>>>>>> modified
>>>>>>> modified
