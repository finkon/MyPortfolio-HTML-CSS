def addition ():
    num_1 = int(input ("Please enter your first number"))
    num_2 = int(input ("Please enter your second number"))
    num_3 = int(input ("Please enter your third number, enter 0 if you don't want to add anymore numbers"))
    num_4 = int(input ("Please enter your fourth number, enter 0 if you don't want to add anymore numbers"))
    num_5 = int(input ("Please enter your fifth number, enter 0 if you don't want to add anymore numbers"))

    sum_addition = num_1 + num_2 + num_3 + num_4 + num_5

    print ("The sum of these numbers is" + str (sum_addition))

    addition ()

##

def multiplication ():
    num_1 = int(input ("Please enter your first number"))
    num_2 = int(input ("Please enter your second number"))

    sum_multiplication = num_1 * num_2

    print ("The sum of these numbers is" + str (sum_multiplication))

    multiplication ()

##

def division ():
    num_1 = int(input ("Please enter your first number"))
    num_2 = int(input ("Please enter your second number"))
   

    sum_division = num_1 / num_2

    print ("The sum of these numbers is" + str (sum_division))

    division ()

##

def subtraction ():
    num_1 = int(input ("Please enter your first number"))
    num_2 = int(input ("Please enter your second number"))
    num_3 = int(input ("Please enter your third number, enter 0 if you don't want to subtract anymore numbers"))
    num_4 = int(input ("Please enter your fourth number, enter 0 if you don't want to subtract anymore numbers"))
    num_5 = int(input ("Please enter your fifth number, enter 0 if you don't want to subtract anymore numbers"))

    sum_subtraction = num_1 - num_2 - num_3 - num_4 - num_5

    print ("The sum of these numbers is" + str (sum_subtraction))

    subtraction()