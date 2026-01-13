import random
import time

def Game():
    print("Hello,this is Guess number game.")
    
    count = 0
    RanNum = 0
    time_limit = 0
    max_guessing = 0
    
    #hint_det = 0
    #hint_set = 1

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

  
    def Mode_choice():
        
        
        print("")
        print("Mode 1: the number is generate by the computer")
        print("Mode 2: the number is type by the other player")
        print("")
        while True:
            try:
                mode_choice = int(input("Please choose a mode"))
                if mode_choice == 1 or mode_choice ==2:
                    return mode_choice
                else:
                    print("Error, please input a valid number")
                    
            except:
                print("Error, please input a valid number")
                # why it doesn't show ?
    
    mode_det = Mode_choice()

    def dificult_setting():
        while True:

            print("")
            print("1.Easy: 50s, range(0,100),max guessing:8")
            print("2.Advanced: 40s, range(0,150),max guessing:10")
            print("3.Difficult: 35s range(0,200),max guessing:12")
            print("")
            try:
                det = int(input("Please choose the Difficulty you prefer >"))
                if det == 1 or det == 2 or det == 3:
                    return det
                else:
                    print(f"{det} is not included")
                
            except:
                print("Error, input a number please")
            
            #(solve)maybe we need to check the validation of input latter

            #(solved)why we need to choose again even if we input the valid 2 ?
        

            #（solved)the end , why we have the sudden error when time is up?
    
    def choice_process(mode_det):

    
        nonlocal time_limit,RanNum,max_guessing

        if mode_det == 1:
            dif = dificult_setting()
            if dif == 1:
                time_limit = 50
                RanNum = random.randint(1,100)
                max_guessing = 8
            elif dif == 2:
                time_limit = 40
                RanNum = random.randint(1,150)
                max_guessing = 10
            elif dif == 3:
                time_limit = 35
                RanNum = random.randint(1,200)
                max_guessing = 12
        
        elif mode_det == 2:
            dif = dificult_setting()
            if dif == 1:
                time_limit = 50
                max_guessing = 8
                while True:
                    RanNum = int(input("Please input the number in the suitable range"))
                    if 0 <= RanNum and RanNum <= 100:
                        break
                    else:
                        print("Invalid! Please input again")
            elif dif == 2:
                time_limit = 40
                max_guessing = 10
                while True:
                    RanNum = int(input("Please input the number in the suitable range"))
                    if 0 <= RanNum and RanNum <= 150:
                        break
                    else:
                        print("Invalid! Please input again")
            elif dif == 3:
                time_limit = 35
                max_guessing = 12
                while True:
                    RanNum = int(input("Please input the number in the suitable range"))
                    if 0 <= RanNum and RanNum <= 200:
                        break
                    else:
                        print("Invalid! Please input again")
        
    
    choice_process(mode_det)
    # we need to set the difficulty here

  
    start_time = time.time()

    def hint(num,max_guessing,count):
        
        emergency_index = max_guessing - count
        
        if emergency_index == 4:
            if num % 2 == 0:
                print("It is even")
            else:
                print("It is odd")

        elif emergency_index == 3:
            edge_1 = random.randint(10,20)
            edge_2 = random.randint(10,20)
            right_edge = num+edge_2
            left_edge = num-edge_1
            if left_edge < 0:
                left_edge = 0
            print(f"The answer is between [{left_edge},{right_edge}]")

        
        elif emergency_index == 2:
            edge_1 = random.randint(5,10)
            edge_2 = random.randint(5,10)
            right_edge = num+edge_2
            left_edge = num-edge_1
            if left_edge < 0:
                left_edge = 0
            print(f"The answer is between [{left_edge},{right_edge}]")
            

        elif emergency_index == 1:
            edge_1 = random.randint(0,5)
            edge_2 = random.randint(0,5)
            right_edge = num+edge_2
            left_edge = num-edge_1
            if left_edge < 0:
                left_edge = 0
            print(f"The answer is between [{left_edge},{right_edge}]")
            
    
    def guessing(RanNum):    
        
        nonlocal count

        hint_set = 1
        while True:
            
            try:
                # this is hint randomly generate part
                print("Please input your number")
                UserAns = int(input())
                
                if count > max_guessing:
                    print("Up to the max guessing, game over")
                    print(f"the answer is {RanNum}")
                    break
                hint_det = random.randint(0,1)
                if hint_det == hint_set and abs(UserAns - RanNum) >= 10:
                    hint(RanNum,max_guessing,count)
                
                # this is the time limitation part
                past_time = time.time() - start_time
                rest_time = int(time_limit - past_time)
                if past_time > time_limit:
                    print("Time is up !")
                    print(f"the answer is {RanNum}")
                    break
                else:
                    print(f"You have {rest_time} seconds left")
                
                
                count += 1
                if UserAns == RanNum:
                    print("You are right!")
                    print(f"Your attempt is {count}")
                    print(f"Used time {int(past_time)}")
                    break    
                else:
                    Distance_Suggestion(UserAns,RanNum)
            
            except ValueError:
                print("It is not a number !")
    
    guessing(RanNum)    
            

Game()
            

