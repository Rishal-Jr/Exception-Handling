try :
    num=int(input("Enter your number: "))
    print(num)
except ValueError as ex:
   print("Exception: ",ex)

print("I'm outside of the block")   
