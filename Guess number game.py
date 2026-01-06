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
    else:
        print("Very very far")

def Mode_1():
    print("Hello,this is Guess number game, mode 1")
    count = 0
    start_time = time.time()
    hint_det = 0
    hint_set = 1

    # we need to set the difficulty here

    dif = dificult_setting()
    if dif == 1:
        time_limit = 50
        RanNum = random.randint(1,100)
    elif dif == 2:
        time_limit = 40
        RanNum = random.randint(1,150)
    elif dif == 3:
        time_limit = 35
        RanNum = random.randint(1,200)


    
    while True:
        
        # this is hint randomly generate part
        hint_det = random.randint(0,5)
        if hint_det == hint_set:
            hint(RanNum)
        
        # this is the time limitation part
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
    




def hint(num):
    a = random.randint(1,4)
    
    if a == 1:
        if num // 2 == 0:
            print("It is even")
        else:
            print("It is odd")

    elif a == 2:
        edge_1 = random.randint(10,30)
        edge_2 = random.randint(10,15)
        print(f"The answer is between [{num-edge_1},{num+edge_2}]")

    
    elif a == 3:
        edge_1 = random.randint(10,20)
        edge_2 = random.randint(5,10)
        print(f"The answer is between [{num-edge_1},{num+edge_2}]")

    elif a == 4:
        edge_1 = random.randint(10,15)
        edge_2 = random.randint(10,15)
        print(f"The answer is between [{num-edge_1},{num+edge_2}]")


def dificult_setting():
    while True:

        print("")
        print("1.Easy: 50s, range(0,100)")
        print("2.Advanced: 40s, range(0,150)")
        print("3.Difficult: 35s range(0,200)")
        print("")
        try:
            det = int(input("Please choose the Difficulty you prefer >"))
            break
        except:
            print("Error, input a number please")
        
        #(solve)maybe we need to check the validation of input latter

        #(solved)why we need to choose again even if we input the valid 2 ?
    return det

#the end , why we have the sudden error when time is up?
Mode_1()

            

    


