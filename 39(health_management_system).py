# 3 clients : Shaan, Bill , Warren 
# 6 files to be created
# Function that takes client name and locks either "Excersie" or "diet" and take the time at what time it was taken
# function to retrieve what the client did
import datetime
def gettime():
    return datetime.datetime.now()
print("Welcome to the the Health Management System")
lock_or_retrieve=int(input("Hey choose:\n 1 for Lock\n 2 for Retrieve\n"))
if lock_or_retrieve==1:
    def lock():
        """This function log the details of food and excercise"""  
    client=int(input("Choose:\n 1 for Shaan\n 2 for Bill\n 3 for Warren\n Type your choice:"))
    if client==1:

        # SHAAN LOCK

        print("Hi Shaan")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            print("Hey Shaan Type your Exercise here:\n")
            value=str(input())
            f=open("Shaan.Exercise.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
            f.close()
        elif choose==2:
            print("Hey Shaan Type your Diet here:\n")
            value=str(input())
            f=open("Shaan.Diet.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
        f.close()

        # BILL LOCK

    elif client==2:
        print("Hi Bill")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            print("Hey Bill Type your Exercise here:\n")
            value=str(input())
            f=open("Bill.Exercise.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
            f.close()
        elif choose==2:
            print("Hey Bill Type your Diet here:\n")
            value=str(input())
            f=open("Bill.Diet.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
        f.close()

        # WARREN LOCK

    if client==3:
        print("Hi Warren")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            print("Hey Warren Type your Exercise here:\n")
            value=str(input())
            f=open("Warren.Exercise.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
            f.close()
        elif choose==2:
            print("Hey Warren Type your Diet here:\n")
            value=str(input())
            f=open("Warren.Diet.txt","a")
            f.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully added!!")
        f.close()
elif lock_or_retrieve==2:
    def retrieve():
        """This function retrieve the details of food and excercise""" 
    client=int(input("Choose:\n 1 for Shaan\n 2 for Bill\n 3 for Warren\n Type your choice:"))
    if client==1:

        # SHAAN Retrieve

        print("Hi Shaan")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            f=open("Shaan.Exercise.txt")
            print(f.read())
            f.close()
        elif choose==2:
            f=open("Shaan.Diet.txt")
            print(f.read())
            f.close()

        # BILL Retrieve

    elif client==2:
        print("Hi Bill")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            f=open("Bill.Exercise.txt")
            print(f.read())
            f.close()
        elif choose==2:
            f=open("Bill.Diet.txt")
            print(f.read())
            f.close()

        # WARREN LOCK

    if client==3:
        print("Hi Warren")
        print("Choose\n 1 for Exercise\n 2 for Diet\n")
        choose=int(input("Type your choice:"))
        if choose==1:
            f=open("Warren.Exercise.txt")
            print(f.read())
            f.close()
        elif choose==2:
            f=open("Warren.Diet.txt")
            print(f.read())
            f.close()
        f.close()       