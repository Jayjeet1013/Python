# Name = input("Input Your Name: ")

# Date = input("Input date: ")
# Date = int(Date)

# print("Dear ",Name,",\nYou are Selected!\n",Date)


letter = '''Dear Name,
You are Selected!

Date : date
'''

name = input("Enter your name")
date = input("Enter your date")

letter = letter.replace('name',name)
letter = letter.replace('date',date)

print(letter)