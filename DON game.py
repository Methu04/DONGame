#importing modules
import sub.func
import random
import datetime
#initializing variables
User_name=""
life_score=0
attempt=20
count=1
value_list=[]
enemy=0
selected_number=0
#opening the file and editing the file name
current_date=datetime.datetime.now().strftime("%Y_%m_%d")
current_time=datetime.datetime.now().strftime("%H_%M_%S")
game_id=random.randrange(0000,9999)
file_name=f"{current_date}_{current_time}_{game_id}"
fo=open(f"{file_name}.txt","w")
#taking user inputs
User_name=input("Player name: ")
fo.write(f"Player name: {User_name}\n")
#taking the range for starting life score 
life_score=random.randrange(1,50)
#creating a loop to run the process until the count is less than or equal to attempt
while(count<=attempt):
    print("Attempt:",count)
    fo.write(f"Attempt:{count}\n")
    print(User_name,"'s life score is: ",life_score)
    fo.write(f"{User_name}'s life score is: {life_score}\n")
    #if count is between 1 and 5 , enemies should be within the range 15 and 100
    if 1<= count <=5:
        value_list=[random.randrange(15,101)for enemy in range(5)]
        for enemy in value_list:
            print(enemy,end=" ")
        print()
        #map is used to convert each element in value_list to a string, making sure that both sides of the in comparison are of the same type 
        value_range=[str(enemy) for enemy in value_list]
        for enemy in value_list:
            fo.write(f"{enemy} ")
        fo.write("\n")
        
    #if count is between 6 and 10 , enemies should be within the range 250 and 2000
    else:
        if 6<= count <=10 :
            value_list=[random.randrange(250,2001)for enemy in range(5)]
            for enemy in value_list:
                print(enemy,end=" ")
            print()
            value_range=[str(enemy) for enemy in value_list]
            for enemy in value_list:
                fo.write(f"{enemy} ")
            fo.write("\n")
        #if count is between 11 and 15 , enemies should be within the range 3000 and 10000
        else:
            if 11<= count <=15:
                value_list=[random.randrange(3000,10001)for enemy in range(5)]
                for enemy in value_list:
                    print(enemy,end=" ")
                print()
                value_range=[str(enemy) for enemy in value_list]
                for enemy in value_list:
                    fo.write(f"{enemy} ")
                fo.write("\n")
            #if count is between 16 and 20 , enemies should be within the range 20000 and 100000
            else:
                 if 16<= count <=20:
                     value_list=[random.randrange(20000,100001)for enemy in range(5)]
                     for enemy in value_list:
                         print(enemy,end=" ")
                     print()
                     value_range=[str(enemy) for enemy in value_list]
                     for enemy in value_list:
                         fo.write(f"{enemy} ")
                     fo.write("\n")
                     
    selected_number=input("Select a number to fight: ")
    fo.write(f"Select a number to fight: {selected_number}\n")
    #for invalid user input
    
    if selected_number not in value_range:
        print("No such enemy\n")
        fo.write("No such enemy\n\n")
        count=count+1
        break
    else:
        if(selected_number==""):
            print("No such enemy\n")
            fo.write("No such enemy\n\n")
            count=count+1
            break
            
    selected_number=int(selected_number)
    #displaying whether the user won or lost
    if(selected_number<=life_score):
            print(User_name,"killed",selected_number,"\n")
            fo.write(f"{User_name} killed {selected_number}\n\n")
            life_score=selected_number+life_score
    else:
        print(selected_number,"killed",User_name,"\n")
        fo.write(f"{selected_number} killed {User_name}\n\n")
        count=count+1
        break
    #increasing the count so that the loop can continue
    count=count+1
#displaying the game status
sub.func.gamestatus_final(User_name,count,life_score,attempt)
fo.write("Game status".center(17,"*"))
fo.write(f"\nPlayer name: {User_name}\n")
fo.write(f"Total attempts: {count-1}\n")
fo.write(f"Final score: {life_score}\n")
if(count-1==attempt):
    fo.write(f"{User_name}saved letter kind\n")
else:
    fo.write(f"{User_name} was defeated!!!\n")

#closing the text file
fo.close()
