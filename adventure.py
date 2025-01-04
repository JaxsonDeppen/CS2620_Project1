print(" Welcome to my Adventure Game")
def start_adventure():
    story = "Adventure name is: "
    while True: 
        outcome_name = (input("Enter in your Adventure Name: "))    
        if outcome_name.isalpha():
            break
        else:  
            print("Adventure name must be a combination of Characters [a-z] and [A-Z] ")
    story += outcome_name
    story += "\n You are a mercenary you only have 10 silver coins leftover.\n You arent quite sure how you ended up here\n.You will have to answer a series of riddles and you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n"
    print("\n \n You are a mercenary you only have 10 silver coins leftover.\n You arent quite sure how you ended up here\nYou will have to answer a series of riddles you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n")
    story += "Your in a room with two locked doors and a computer. \n the computer has a message on it that reads: \n  I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me.\n 1) Fire \n 2) Water"
    print(story)
    life = 5
    coins = 10
    bool = False
    while bool is False:
        choice = input("Your in a room with two locked doors and a computer. \n the computer has a message on it that reads: \n  I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me.\n 1) Fire \n 2) Water")
        final_choice = convert_strtoint(choice)
        if final_choice == 1:
            bool = True
            story += f" \n You choose {final_choice} that was the correct choice go through door 1"
            print(f" \n You choose {final_choice} that was the correct choice go through door 1")
            story += "You go through door one and there is a ladder leading up. When you ascend the ladder you see lush green fields with a river running through it. The sun is starting to go down you have an hour or two of daylight left."
            print("You go through door one and there is a ladder leading up.\n When you ascend the ladder you see lush green fields with a river running through it.\n The sun is starting to go down you have an hour or two of daylight left.")
            bridge_toll(story,coins,life)
        elif final_choice == 2:
            bool = True
            life -= 1
            game_over(life,story)
            story += f" \nYou choose {final_choice} that was incorrect your life is now {life} go through door two "
            print(f" \nYou choose {final_choice} that was incorrect your life is now {life} go through door two ")
            story += "\nYou go through the second door and see an elevator that goes down. \n you go down this elevator and it seems to take forever even though it is moving rather quickly. \n Eventually it reaches the bottom and when you step out and you see a lake that goes as far as the eye can see. \n In front of you there is a dock and a small canoe with a man fishing on it.\n Out in the distance you can see lights and stilts which looks like a town on the water. \nYou approach the man fishing."
            print("\nYou go through the second door and see an elevator that goes down. \n you go down this elevator and it seems to take forever even though it is moving rather quickly. \n Eventually it reaches the bottom and when you step out and you see a lake that goes as far as the eye can see. \n In front of you there is a dock and a small canoe with a man fishing on it.\n Out in the distance you can see lights and stilts which looks like a town on the water. \nYou approach the man fishing.")
            story += "\nThe man says either answer my riddle of pay the 5 silver coins for the ferry. You check your pockets and discover that you indeed have 10 silver coins. What do you do? \n1) pay the 5 coins \n 2) take your chances with the riddle"
            bool2 = False
            while bool2 is False:
                choice = input("\nThe man says either answer my riddle of pay the 5 silver coins for the ferry. You check your pockets and discover that you indeed have 10 silver coins. What do you do? \n1) pay the 5 coins \n 2) take your chances with the riddle")
                final_choice = convert_strtoint(choice)
                if final_choice == 1:
                    bool2 = True
                    coins -= 5
                    story += f"\nYou pay the man the five coins your leftover coins are {coins} and you get to the town. \n"
                    print(f"\nYou pay the man the five coins your leftover coins are {coins} and you get to the town.\n")
                    under_ground_town(story,life, coins)
                elif final_choice == 2:
                    bool2 = True
                    story += "\nWhat flies when its born, lies when its alive, and runs when its dead? \n1) Grain of sand\n 2) A fire\n 3) a fly \n 4) a snowflake." 
                    bool3 = False
                    choice = input("\nWhat flies when its born, lies when its alive, and runs when its dead? \n1) Grain of sand\n 2) A fire\n 3) a fly \n 4) a snowflake.")
                   
                    final_choice = convert_strtoint(choice)
                    while bool3 is False:
                        if final_choice == 4:
                            bool3 = True
                            story += "\n Your choice was correct I will let you pass for free to the town.\n"
                            print("\n Your choice was correct I will let you pass for free to the town.\n")
                            under_ground_town(story,life, coins)
                        elif final_choice == 1 or final_choice == 2 or final_choice == 3:
                            bool3 = True
                            
                            life -= 1
                            game_over(life,story)
                            
                            story += f"\n Your choice was incorrect the answer was 4) snowflake life total is now {life} \n"
                            print(f"\n You choice was incorrect the answer was 4) snowflake life total is now {life} \n")
                            under_ground_town(story,life, coins)
                        else:
                            print("You must choose 1,2,3, or 4 try again")
                else: 
                    print("\nYou must enter the number 1 or 2 try agian\n")
        else: 
            print("\nFinal choice must be 1 or 2 try again\n")


def under_ground_town(story,life, coins):
    print(f"\nyou arrive at the town with {coins} coins left and {life} lives left\n")
    story += f"\nyou arrive at the town with {coins} coins left and {life} lives left\n"
    print("\nWhen you arrive you quickly realize that the town is quite a lot bigger than you realized. \nIt goes as far as the eye can see with several shopping discticts and towns.\n")
    story += "\nWhen you arrive you quickly realize that the town is quite a lot bigger than you realized. \nIt goes as far as the eye can see with several shopping discticts and towns.\n"
    print("\nYou go to the shopping districts to see if there are any jobs that you can take on for a little money.\n Hopefully you can scrounge enough together to get your equipment worked on\n")
    story += "\nYou go to the shopping districts to see if there are any jobs that you can take on for a little money.\n Hopefully you can scrounge enough together to get your equipment worked on\n"
    print("\nA fisherman approaches you and says '\nI havent seen you around here before you seem to be a mercenary from your looks.\n I keep going fishing but everytime I get attacked by this huge fish I have never seen before.\n' ")
    story += "\nA fisherman approaches you and says '\nI havent seen you around here before you seem to be a mercenary from your looks.\n I keep going fishing but everytime I get attacked by this huge fish I have never seen before.\n' "
    story += "\nWould you come with me if you kill the fish I will pay you 20 silver coins?\n 1) yes\n 2) no\n"
    choice = input(("\nWould you come with me if you kill the fish I will pay you 20 silver coins?\n 1) yes\n 2) no\n"))
    final_choice = convert_strtoint(choice)
    print(story)
    bool = False
    while bool is False:
        if final_choice == 1:
            bool = True
            print("\nOkay with that settled lets head out\n")
            story += "\nOkay with that settled lets head out\n"
            fishermans_quest(story,coins,life)

        elif final_choice == 2:
            bool = True
            print("Thats okay if you change your mind come back my offer stands")
            story += "Thats okay if you change your mind come back my offer stands"
            print(f"\n You enter a blacksmiths shop and ask how much it will cost to mend your gear he says 10 silver coins you have {coins} coins left\n")
            story += f"\n You enter a blacksmiths shop and ask how much it will cost to mend your gear he says 10 silver coins you have {coins} coins left\n"
            if coins >= 10:
                cave(story,coins,life)
            else:
                print("\nAs you do not have enough coins you go back to the fisherman and take on his job\n")
                story += "\nAs you do not have enough coins you go back to the fisherman and take on his job\n"
                fishermans_quest(story, coins, life)
        else:
            print("You must choose either 1 or 2 try again")


def fishermans_quest(story, coins,life):
    print("\nIt doesnt always attack me it doesnt seem to have a pattern but it happens enough that I am having a really hard time keeping afloat.\n")
    story += "\nIt doesnt always attack me it doesnt seem to have a pattern but it happens enough that I am having a really hard time keeping afloat.\n"
    print("\nAs the fisherman starts to fill you in all of the sudden you hear a deep voice that says. \n Answer my riddle correctly or I will kill you both.\n ")
    story += "\nAs the fisherman starts to fill you in all of the sudden you hear a deep voice that says. \n Answer my riddle correctly or I will kill you both.\n"
    choice = input("The more there is, the less you see. What am I?")
    if choice == "Darkness" or choice == "darkness":
        print("\nYou answered correctly I will leave the fisherman alone from now on.\n")
        story += "\nYou answered correctly I will leave the fisherman alone from now on.\n"
        print("\nThank you so much you were able to deal with the fish now I can do my job in peace.\n here is your ten coins.\n")
        coins += 10
        cave(story,coins,life)
    else:
        print("Game Over you have lost your life to the depths of the lake")
        story += "Game Over you have lost your life to the depths of the lake"
        save_story_block(story)
        menu()


def cave(story,coins,life):
    print("\n As you have enough coins your mend your gear and start to head out of town.\n on the other side of town is a cave entrance. \n You enter and wake for a remarkably long time not seeing anything or anyone.\n")
    story += "\n As you have enough coins your mend your gear and start to head out of town.\n on the other side of town is a cave entrance. \n You enter and wake for a remarkably long time not seeing anything or anyone.\n"
    print("\nOut of nowhere you hear a low growl you take your sword out and get prepared to defend yourself.\n It appears to be a pack of wolves they slowly surround you.\n The first strike comes and they all start to pick at you piece by piece.\n Defending yourself with everything you have you keep trying but eventually fall only taking one of the wolves out.\n")
    story += "\nOut of nowhere you hear a low growl you take your sword out and get prepared to defend yourself.\n It appears to be a pack of wolves they slowly surround you.\n The first strike comes and they all start to pick at you piece by piece.\n Defending yourself with everything you have you keep trying but eventually fall only taking one of the wolves out.\n"
    print("\nAs you feel your life fading away you see a blinding light and hear someone say if you can answer this riddle correctly I will save your life.\n")
    story += "\nAs you feel your life fading away you see a blinding light and hear someone say if you can answer this riddle correctly I will save your life.\n"
    bool2 = False
    
    while bool2 is False:
        choice = input(" If all Wibbles are Criggles, all Borkins are Kwumblins, no Hoggles are Borkins, and all Criggles are Borkins, is it true that all Borkins are Criggles? \n 1) yes \n 2) no")
        final_choice = convert_strtoint(choice)
        if final_choice == 2:
            bool2 = True
            print("\nYou start to see the light getting closer and closer and the wolves become scared and run away\n")
            story += "\nYou start to see the light getting closer and closer and the wolves become scared and run away\n"
            print("\nThe light proceeds to guide you outside of the cave and to safe passage.\n Congratulations you have beat this game thanks for playing!\n")
            story += "\nThe light proceeds to guide you outside of the cave and to safe passage.\n Congratulations you have beat this game thanks for playing!\n"
            save_story_block(story)
            menu()
        elif final_choice == 1:
            bool2 = True
            print("Game over you lose")
            save_story_block(story)
            menu()
        else:
            print("must answer 1 or 2 try again")
            
    

def bridge_toll(story,coins,life):
    print("\nYou approacha a bridge there are two men with spears gaurding the entrace.\n They tell you to pay ten coins to pass or leave now\n")
    story += "\nYou approacha a bridge there are two men with spears gaurding the entrace.\n They tell you to pay ten coins to pass or leave now\n"
    bool9 = False
    while bool9 is False:
        choice = input("Do you pay the ten silver coins? \n 1) yes \n 2) no")
        final_choice = convert_strtoint(choice)
        if final_choice == 1:
            bool9 = True
            coins -= 10
            print(f"\nYou know have {coins} coins left you pass over the bridge and start heading to the town\n")
            story += f"\nYou know have {coins} coins left you pass over the bridge and start heading to the town\n"
            town_mugging(story,coins,life)
        elif final_choice == 2:
            bool9 = True
            print("\nyou start travelling along the river hoping to find a way over or shelter for the night\n")
            story += "\nyou start travelling along the river hoping to find a way over or shelter for the night\n"
            print("\n travelling for a long time along the river and night starts to fall\n")
            story += "\n travelling for a long time along the river and night starts to fall\n"
            choice = input("\n 1) do you seek shelter \n 2) keep going")
            final_choice = convert_strtoint(choice)
            if final_choice == 1:
                print("\nyou find a tree and decide to sleep under that\n")
                story += "you find a tree and decide to sleep under that\n"
                print("\nThe tree starts to move and you quickly get up out of confusion and fear. \n This is an animal not just a tree \n It start to speak to you answer this riddle to win or die.\n")
                story += "\nThe tree starts to move and you quickly get up out of confusion and fear. \n This is an animal not just a tree \n It start to speak to you answer this riddle to win or die.\n"
                choice = input(" I am something people celebrate or resist. I change people’s thoughts and lives. I am obvious to some people but, to others, I am a mystery. What am I?")
                if choice == "age" or choice == "Age":
                    print("You win thanks for playing")
                    save_story_block(story)
                    menu()
                else:
                    print("you die try again later")
                    save_story_block(story)
                    menu()
            elif final_choice == 2:
                print("\nKeep moving in hopes that you find something better or a way to cross the river\n")
                story += "\nKeep moving in hopes that you find something better or a way to cross the river\n"
                print("\nAfter walking so long and not having any food you eventually collapse and pass out\n")
                story += "\nAfter walking so long and not having any food you eventually collapse and pass out\n"
                print("Game over")
                save_story_block(story)
                menu()
        else:
            print("must enter 1 or 2 try again")



def game_over(life, story):    
    if life <= 0:
        print("Game over you have answered incorrectly to many times. Saving outcome to txt file and returing to menu.")
        story += "\n Game Over\n"
        save_story_block(story)
        menu()
    else:
        return
        
def town_mugging(story,coins,life):
    print("\nYou enter the town and start walking towards the city sqaure.\n")
    story += "\nYou enter the town and start walking towards the city sqaure.\n"
    print("\nAs you walk you get cornered by three men with all armed with knifes\n")
    story += "\nAs you walk you get cornered by three men with all armed with knifes\n"
    choice = input("\n Answer my riddle correctly or we will kill you\n I can fly but have no wings. I can cry but I have no eyes. Wherever I go, darkness follows me. What am I?")
    if choice == "Clouds" or choice == "clouds" or choice == "cloud" or choice == "Cloud":
        print("You won thanks for playing")
        save_story_block(story)
        menu()
    else:
        print("you lose try again later")
        save_story_block(story)
        menu()

    
def save_story_block(story):
        with open('adventure_outcomes.txt', 'a') as file:
            file.writelines(story)
            file.close()
def read_outcomes():
    with open('adventure_outcomes.txt', 'r') as file:
        content = file.readlines()
        file.close()
        for line in content:
            print(line.strip())
def convert_strtoint(input):
    while True:
        try:
            val = int(input)
            return val
        except ValueError:
            print("You can only enter a whole number try again")     
def menu():
        user_input = input("would you like to \n 1 Start a new Adventure \n 2 Read previous outcomes \n 3 exit \n")
        val = convert_strtoint(user_input)
        return val
        
        
user_input = menu()
while user_input != 3:
    if user_input == 1:  
        story = start_adventure()
        #save_story_block(story)
    elif user_input == 2:
        read_outcomes()
    user_input = menu()
quit()


