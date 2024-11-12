def gamestatus_final(z,x,y,d):
        print("Game status".center(17,"*"))
        #fo.write("Game status".center(17,"*"))
        print("Player name: ",z)
        #fo.write(f"\nPlayer name: {User_name}\n")
        print("Total attempts: ",x-1)
        #fo.write(f"Total attempts: {x}\n")
        print("Final score: ",y)
        #fo.write(f"Final score: {y}\n")
        if(x-1==d):
                print(z,"saved letter kind")
                #fo.write(f"{User_name}saved letter kind\n")
        else:
                print(z,"was defeated!!!")
                #fo.write(f"{User_name} was defeated!!!\n")
