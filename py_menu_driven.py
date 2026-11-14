# Author: Rachid Raghib
# File Name: py_menu_driven.py
# Description: Check various basic Python concepts and operations

from datetime import date,datetime
import math

def pause(text:str):
        print("\n",text)
        input()

def dictionary():
        nl="\n"
        dict_1={"Name":"Rachid Raghib",
                "Id":"01",
                "Major":"Computer Science",
                "GPA":"3.3",

                }
        #// display the entire dictionary
        print("\nOriginal Dictionary\n\n",dict_1)
        #// display By keys
        result=dict_1["Name"]
        print(nl,result)
        result=dict_1["Id"]
        print(nl,result)
        result=dict_1["Major"]
        print(nl,result)
        result=dict_1["GPA"]
        print(nl,result)
        pause("\nNow lets update the dictionary by adding key-value pair and then modifying ." +
              "\nPress Enter to continue...\n")
        dict_1["Email"]="rachidraghib@hotmail"
        dict_1["Phone Number"]="617-999-8091"
        print("\nUpdated Dictionary\n\n",dict_1)
        dict_1.update({"Phone Number":"617-999-9087"})
        print("\nUpdated Phone Number\n\n",dict_1)

        pause("Now let's add a pair (address and its value) and try to remove it"+
              "\nPress Enter to continue...")
        dict_1["Address"]="8 glen ave. Melrose MA 02176"
        print("Added Dictionary\n",dict_1)
       
        print("\nThe value of Address key: ")
        print(dict_1.pop("Address"))
        dict_1.popitem()
        print("\nRemoved Last pair\n\n",dict_1)
        pause("Press Enter to continue...")
        print(nl,dict_1.keys(),nl)
        print(dict_1.values(),nl)
        print(dict_1.items(),nl)
#####################################################################
def integer_factors():
     number = int(input("Please Enter any Integer : "))

     value = 1
     print("The Result of a Given {0} are:".format(number))

     while (value <= number):
           if(number % value == 0):
               print("{0}".format(value))
           value = value + 1
#####################################################################
def number_digits():
      const=num=int(input("\nEnter a number to display number of digit(s) it contains:  "))
      count=0
      while(num>0):
            num=num//10
            count=count+1
      print(f"\nThe number {const} has {count} digits")
#####################################################################             
def integer_1st_digit():
       number = int(input("Please Enter any Number: "))

       first_digit = number

       while (first_digit >= 10):
            first_digit = first_digit // 10

       print("The First Digit from a Given Number {0} = {1}".format(number, first_digit))
#####################################################################       
def show_matrix():
      matrix=[[1,2,3],[4,5,6],[7,8,9]]
      
      for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                  print(matrix[i][j],end=" ")
                  
            print() 
#####################################################################
def lower_upper_limits(lower:int,upper:int):
      if upper<lower: return 0
      else:
            result=upper+lower_upper_limits(lower,upper-1)
            return result
#####################################################################
def is_even(n:int):
       return n%2==0
#####################################################################
def range_sum(n:int):
     if (n<=0): return n
     else:
          result=n+range_sum(n-1)
          return result
#####################################################################         
def fibonacci(n=int):
     # base case:
     if (n==0): return 0
     if (n==1): return 1
     return fibonacci(n-1)+fibonacci(n-2)
     
#####################################################################   
def quadratic_equation():
     print("\nFinding the roots of Quadratic equation: ax^2+bx+c")
     a=int(input("Enter the value of (a): "))
     b=int(input("Enter the value of (b): "))
     c=int(input("Enter the value of (c): "))
     print("For alghoriths and looking back on algebra, we need to find the value of the\n ",
           "discriminant, d=b^2-4ac")
     delta=(b*b)-(4*a*c)
     if delta>0:
          root1=(-b+math.sqrt(delta))/(2*a)
          root2=(-b-math.sqrt(delta))/(2*a)
          print("There are two Distinct Real Roots: Root1=% .2f and Root2=% .2f"%(root1,root2))
     elif delta==0:
          root1=root2=(-b/(2*a))
          print("There are two Equal Real Roots: Root1=% .2f and Root2=% .2f"%(root1,root2))
     else:
          root1=root2=(-b/(2*a))
          imaginary=math.sqrt(-delta)/(2*a)
          print("There are two Imaginary Real Roots: Root1=% .2f+% .2f and Root2=% .2f-% .2f"
                %(root1,imaginary,root2,imaginary))
               
#####################################################################              
def divisors():
     num=int(input("Enter an integer "))
     print("the divisors of ",num," are:")
     for i in range(1,num+1):
          if num%i==0:
               print(i)
#####################################################################
def date_time():
    todays_date=date.today()
    print("Today's date: ",todays_date)
    today=datetime.now() 
    print(today)
    dt=today.strftime("%B %d, %Y %H:%M:%S")
    print(dt)
#####################################################################
def leap_year():
     year=int(input("Enter the year to check if it's leap year or not : "))
     print(year," is a leap year" if (year%400==0) or ((year%4==0) and (year%100!=0)) else " is not")
#####################################################################
def show_menu():
    today=datetime.now() 
    print(nl,today)
    print("\n\n# Author: Rachid Raghib",
          "\n# File Name: Basics.py",
          "\n# Description: \n")
    print("\n\t\t\t\t********** PYTHON PROGRAMS **********\n")
    print("0. Quit       \t\t 8. Sum [lower,upper]      \t\t16. Program\n")
    print("1. Date & Time\t\t 9. Print 3X3 Matrix       \t\t17. Program\n")
    print("2. Leap Year  \t\t10. Count Number Digits.   \t\t18. Program\n")
    print("3. Divisors   \t\t11. Integers Factors       \t\t19. Program\n")
    print("4. Quadratic  \t\t12. 1st digit of a number  \t\t20. Program\n")
    print("5. Fibonacci  \t\t13. Dictionary             \t\t21. Program\n")
    print("6. Sum [0,n]  \t\t14. Program                \t\t22. Program\n")
    print("7. Even/Odd   \t\t15. Program.               \t\t23. Program\n")
    print("\n(*: Debugging In Progrress)\n")
#####################################################################
def switch(choice):
    if choice==0:
        return print()
    elif choice==1:
        return date_time()
    elif choice==2:
        return leap_year()
    elif choice==3:
        return divisors()
    elif choice==4:
        return quadratic_equation()
    elif choice==5:
        n=int(input("\nEnter the range up to you wish the fibonacci serie for "))
        print("Fibonacci serie of ",n," is")
        for i in range(0,n+1):
             print(f"{fibonacci(i)}",end=" ")
        return print(f"Fibonacci({n})= ",fibonacci(n))
    elif choice==6:
            n=int(input("\nEnter the range up to you wish to sum for "))
            print("\nIntegers\n")
            for i in range(0,n+1):
                         print(f"{(i)}",end=" ")
            
            return print(f"\n\nThe sum of the range 1 to {n}= ",range_sum(n))
    elif choice==7:
                n=int(input("\nEnter the range up to you wish to sum for "))
                if (is_even(n)==True):
                    return print("IS EVEN")
                else:
                      return print("IS ODD")
    elif choice==8:
                    m=int(input("\nEnter the lower limit "))
                    n=int(input("\nEnter the upper limit "))
                    print(f"\nThe sum of the integers between {m} and {n} inclusive is ")
                    return print(lower_upper_limits(m,n))
            
    elif choice==9:
                    
                    return show_matrix()
    elif choice==10:
                        return number_digits()
    elif choice==11:
                        return integer_factors()
    elif choice==12:
                        return integer_1st_digit()
    elif choice==13:
                        return dictionary()
    elif choice==14:
                        return 
    elif choice==15:
                        return 
    elif choice==16:
                        return     
    
    
    
         
        
#####################################################################            
nl="\n"
show_menu()
choice=int(input("Enter your choice: "))
switch(choice)
