try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    result=num1/num2
    print("Result is: ",result)
    print("Result is: ",result1)
except ZeroDivisionError:
    print("Dividing by zero is not allowed")
except ValueError:
    print("Please enter a numerical value")
except NameError as ex:
    print("Exception: ",ex)

except:
    print("Some error occured")
finally:
    print("I will exicute no matter what happens")


    

   



