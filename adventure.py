print("Welcome to my Adventure Game")
def start_adventure():
    story = "Adventure name is: "
    while True: 
        outcome_name = (input("Enter in your Adventure Name: "))    
        if outcome_name.isalpha():
            break
        else:  
            print("Adventure name must be a combination of Characters [a-z] and [A-Z] ")
    story += outcome_name
    story += "\n You will have to answer a series of riddles and you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n"
    print("\n You will have to answer a series of riddles you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n")
    story += "Your in a room with two locked doors and a computer. \n the computer has a message on it that reads: \n  I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me.\n 1) Fire \n 2) Water"
    
    life = 5
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
        
        elif final_choice == 2:
            bool = True
            life -= 1
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
                    story += "You pay the man the five coins and you get to the town. When you arrive you quickly realize that the town is quite a lot bigger than you realized. It goes as far as the eye can see with several shopping discticts and towns.\n"
                elif final_choice == 2:
                    bool2 = True
                    story += "What flies when its born, lies when its alive, and runs when its dead? \n1) Grain of sand\n 2) A fire\n 3) a fly \n 4) a snowflake." 
                else: 
                    print("\nyou must enter the number 1 or 2 try agian\n")
        else: 
            print("final choice must be 1 or 2 try again")


    story += "Start of story here\n"
    #Write story here
    return story
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


