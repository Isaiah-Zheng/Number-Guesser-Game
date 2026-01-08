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



def Game():
    print("Hello,this is Guess number game.")
    
    count = 0
    RanNum = 0
    time_limit = 0
    
    hint_det = 0
    hint_set = 1
    
    mode_det = Mode_choice()
    choice_process(mode_det)

    # we need to set the difficulty here

  
    start_time = time.time()
    
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
            print(f"the answer is {RanNum}")
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

        #（solved)the end , why we have the sudden error when time is up?

def Mode_choice():
    print("Please choose a mode")
    print("")
    print("Mode 1: the number is generate by the computer")
    print("Mode 2: the number is type by the other player")
    print("")
    while True:
        try:
            mode_choice = int(input())
            return mode_choice
        except:
            print("Error, please input a valid number")


def choice_process(mode_det):
    nonlocal time_limit,RanNum

    if mode_det == 1:
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
    
    elif mode_det == 2:
        dif = dificult_setting()
        if dif == 1:
            time_limit = 50
            while True:
                RanNum = int(input("Please input the number in the suitable range"))
                if 0 <= RanNum and RanNum <= 100:
                    break
                else:
                    print("Invalid! Please input again")
        elif dif == 2:
            time_limit = 40
            while True:
                RanNum = int(input("Please input the number in the suitable range"))
                if 0 <= RanNum and RanNum <= 150:
                    break
                else:
                    print("Invalid! Please input again")
        elif dif == 3:
            time_limit = 35
            while True:
                RanNum = int(input("Please input the number in the suitable range"))
                if 0 <= RanNum and RanNum <= 200:
                    break
                else:
                    print("Invalid! Please input again")
    else:
        return 1
    

Game()
            

