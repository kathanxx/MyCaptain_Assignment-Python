"""WAP to find area of circle by taking in radius as input from user""" 

radius=int(input("Enter radius of circle : "))
area= 3.14*radius*radius
print("Area of circle = ",area)

""" write a program to accept a filename from the user and print the extension of that. """

i= "y"
while i == "y":
    file=input("Enter filename : ")
    file=file.lower()
    s = file.split(".")
    extention = s[-1]
    extention_dictionary = {
    "py" : "Python",
    "c" : "C",
    "cpp" : "C++",
    "txt" : "Text",
    "java" : "Java",
    "html" : "HTML",
    "js" : "JavaScript",
    }
    print("It is a " + extention_dictionary[extention]+" file")
    i= input("Do you want to continue ? y/n \n")
    i=i.lower()
print("Hope to see you soon !")
