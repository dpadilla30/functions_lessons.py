#functions are ways to wrap your code
#into reusable units
#I only define the function ONCE
# whatever I pass inside the parentheses
#is called a parameter
#a parameter is a placeholder for future information
# def sayHello(name,age,card):
#     print(f"say hello {name}")
#     print("Hello Governor")
#     print("welcome back")
#     print(f"welcome back {name}")
#     print(f"your age is {age}")
#     print(f"what are the 16 card digits {card}")

#once you define a function
#you must call or invoke a function
# when I pass information into the
#the called function, its called an argument
     
# sayHello("padilla",34,1234567890123456)

# sayHello("sanches",24,1098826134136245)

# sayHello("gasca",18,123978298793729898)


# def determinEligibility(age):
#     #if your age is over 18, you can vote
#     #otherwise you cant
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("you have to wait")
#     determinEligibility(12)
#     determinEligibility(18)
#     determinEligibility(19)


# def willyougraduate(gpa,credits,SAT):
#     #gpa :number float variable
#     #credits: number variable
#     #passed SAT :boolean
#     if (gpa == 3.0) and (credits>=28) and (SAT == True):
#         return("you passed, goodluck in college")
#     elif(gpa <3.0) or (credits <20) or (SAT != True):
#         print("back to the drawing board")
#     else:
#         print("talk to your counselor")

#     willyougraduate(2.8,15,True)
#     willyougraduate(4.8,20,True)
#     willyougraduate(1.8,2,False)



#return = statement used to end a function
    #and send a result back to the caller

# def add (x,y):
#     z = x+y
#     return z

# def subtract (x,y):
#     z = x-y
#     return z

# def multiply (x,y):
#     z = x*y
#     return z

# def divide (x,y):
#     z = x/y
#     return z


# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "" + last

full_name = create_name("spongebob","squarepants")
print(full_name)