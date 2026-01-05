import random
import time

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
    start_time = time.time()
    time_limit = 20
    hint_det = 0
    hint_set = 1

    
    while True:
        hint_det = random.randint(0,5)
        if hint_det == hint_set:
            hint(RanNum)
        past_time = time.time() - start_time
        rest_time = int(time_limit - past_time)
        if past_time > time_limit:
            print("Time is up !")
            break
        else:
            print(f"You have {rest_time} seconds left")
        print("Please input your number")
        UserAns = int(input())
        count += 1
        if UserAns == RanNum:
            print("You are right!")
            print(f"Your count is {count}")
            break    
        else:
            Distance_Suggestion(UserAns,RanNum)
        
            

def Mode_2():
    print("Hello,this is Guess number game, mode 2")
    print("Please let other player to input a number")
    count = 0
    RanNum = int(input())
    start_time = time.time()
    time_limit = 20
    hint_det = 0
    hint_set = 1
    while True:
        hint_det = random.randint(0,5)
        if hint_det == hint_set:
            hint(RanNum)
        past_time = time.time() - start_time
        rest_time = int(time_limit - past_time)
        if past_time > time_limit:
            print("Time is up !")
            break
        else:
            print(f"You have {rest_time} seconds left")
        print("Please input your number")
        UserAns = int(input())
        count += 1
        if UserAns == RanNum:
            print("You are right!")
            print(f"Your count is {count}")
            break    
        else:
            Distance_Suggestion(UserAns,RanNum)
    

Mode_1()


def hint(num):
    a = random.randint(1,4)
    
    if a == 1:
        if num // 2 == 0:
            print("It is even")
        else:
            print("It is odd")

    elif a == 2:
        edge_1 = random.randint(1,30)
        edge_2 = random.randint(1,15)
        print(f"The answer is between [{num-edge_1},{num-edge_2}]")

    
    elif a == 3:
        edge_1 = random.randint(1,20)
        edge_2 = random.randint(1,10)
        print(f"The answer is between [{num-edge_1},{num-edge_2}]")

    elif a == 4:
        edge_1 = random.randint(1,15)
        edge_2 = random.randint(1,15)
        print(f"The answer is between [{num-edge_1},{num-edge_2}]")

    

            

    


