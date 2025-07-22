while True:
    print("Please give a number")
    try:
        num = int(input())
        break
    except:
        print("Invalid input type!")
        
print("Your num :",num)

