# Day-01
name = input("enter your name") #input funtion used to take input 
input(f"Good morning, {name}!!!.\nHow are you ?") #take input
print("Your Learning Path:\n\t - Python Basics\n\t - Data Engineering\n\t - AI")
print("======================================================================")
print("""Variables
\t-make programs dynamic
\t-name to store a value
\t-stored in memory""")
print("==========================================================================")
print("Data type")
print("python automatically detect data types...")
print ("There are two kind of data types:\n\tnone(have no value)\n\tbuild-in or primitive or single valued data types\n\t user-defined or data structure or multi valued data types")
print("build-in data types\n\tinteger(int)\n\tfloat\n\tboolean")
a = 10 #int
b = 4.3 #float
c = "Great" #string
d = "565"  #str
f = False #boolean (used to handle logic and decision making)
g = True #boolean (case senstive)
h = None #(when nothing to assign yet)
print ("================================================================================")
print("more about functions and data types")
print("""three main type of functions
\tstandalone functions like print(), type(),len()
\t methods of class like upper(), replace().
operations (magic methods these are also  functions) + - * / > < == in or etc.
these functions are from standard library of python also we have different kind of third party lib like pandas numpy etc. third one is user defined""")
print("============================================")
print("standard library")
print("        |       ")
print(" we open and get build in module")
print("in these module we have standalone funtions")
print("also we have classes and for every data type we have class on that class we have several methods like for int class we have to_byte() or for str class we have replace() methods ")
print("===============================================================================")
print("methods and functions are different")
text = "hello"
num = 7
print(type(text)) # give data type name
print(type(num))
print(len(text)) #give the total length of the string (it is a fuction)
print(text.upper()) # captalize all the charecter of the string (it is method)
print(num.bit_length()) # give the total length in bit to save that int or float (it is method)  
print("===================================END=============================== ")