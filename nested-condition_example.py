# """
# i=10
# if(i>=10):
#     # First if statement
#     if(i<15):
#         print("i is smaller than 15")

#         # Nested if statements
#         if(i<12):
#             print("i is smaller than 12 too")
#         else: 
#             print("i is greater than")

# """

# name = input("Enter the name: ").title()
# class_name = input("Enter class name: ").title()
# section = input("Enter section: ").title()
# subject = input("Enter subject: ").title()
# mark = float(input("Mark score in the subject: "))

# print("\n -------------------------------- \n Tracing your", subject, "mark")
# print("Name: ", name)
# print("Class: ", class_name)
# print("Section: ", section)

# if mark < 0 or mark > 100:
#     print("Error: Mark should be between 0 and 100 only")
# elif mark < 50:
#     print(subject, "mark is ", mark)
#     print("Failed in", subject)
# elif mark >= 50:
#     print(subject, "mark is ", mark)
#     print("Congratulations! Pass in", subject)
#     if mark >= 50 and mark < 60:
#         print("Remark: Good in", subject)
#     elif mark >= 60 and mark < 80:
#         print("Remark: Very Good in", subject)
# elif mark >= 80 and mark <= 100:
#     print("Remark: Outstanding in", subject)
# else:
#     print("Something went wrong")
# Print all letter except 'd' and 'f'

for letter in 'Education for all':
	if letter == 'd' or letter == 'f':
		continue 
	print("current letter: ", letter)
	