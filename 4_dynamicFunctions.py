# def check_3_digits(number):
#     return number in range(100,1000)

# result = check_3_digits(68)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100, 1000):
#             return True                     #doesnt work
#         else:
#             pass

# result = check_3_digits([55,99,6000])
# print(type(result))

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100, 1000):
#             return True
#         else:
#             return False

# result = check_3_digits([355,499,600])
# print(result)


# def check_3_digits(list1):
#     three_digits_list = []                #empty list
#     for n in list1:
#         if n in range(100, 1000):
#             three_digits_list.append(n)     #this adds a three digit number to the empty list
#         else:
#             pass

#     return three_digits_list

# result = check_3_digits([555,99,600])              
# print(result)


cofee_prices = [('cappuccino',1.5),('espereso',1.2),('mocha',1.9)]

def most_expensive_coffee(list_of_prices):

    hightest_price = 0
    my_most_expensive_coffee = ''

    for coffee, price in list_of_prices:
        if price > hightest_price:
            hightest_price = price
            my_most_expensive_coffee = coffee
        else:
            pass

    return(my_most_expensive_coffee, hightest_price)

coffee, price = most_expensive_coffee(list_of_prices)

print(f'the most expensive coffee is {coffee}whos price is {price}')









# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.






# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.




