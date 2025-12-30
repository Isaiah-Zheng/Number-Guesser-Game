import random 

def Distance_Suggestion(UserAns,RanNum):     
    Dstans = abs(UserAns-RanNum)
    if Dstans < 5:
        print("Very close")
    elif Dstans < 10:
        print("Close")
    elif Dstans < 20:
        print("Far")
    elif Dstans < 40:
        print("Very far")

def Mode_1():
    print("Hello,this is Guess number game, mode 1")
    count = 0
    RanNum = random.randint(1,100)
    while True:
        print("Please input your number")
        UserAns = int(input())
        count += 1
        if UserAns == RanNum:
            print("You are right!")
            print(f"Your count is {count}")
            break    
        else:
            if UserAns > RanNum:
                print("It is too big")
            else:
                print("It is too small")
            continue

def Mode_2():
    print("Hello,this is Guess number game, mode 2")
    print("Please let other player to input a number")
    count = 0
    Num = int(input())
    #why here is the problem.
    while True:
        print("Please input your number")
        UserAns = int(input())
        count += 1
        if UserAns == Num:
            print("You are right!")
            print(f"Your count is {count}")
            break    
        else:
            if UserAns > Num:
                print("It is too big")
            else:
                print("It is too small")
            continue







