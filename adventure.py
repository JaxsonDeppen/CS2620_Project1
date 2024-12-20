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
    story += "\n You will have to answer a series of riddles you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n"
    print("\n You will have to answer a series of riddles you have 5 lives. If you answer wrong you will lose one life. Answer carefully \n")
    choice = input("Your in a room and you see a computer in front of you. On the computer you see a riddle. The riddle reads you are in a room with three light switches.\n they control three incandesant light bulbs in another room. \n You can only go over to the room with the bulbs one time you cannot go back and forth. You have to find out what light switch controls what bulb. What do you do? \n 1) Call a friend \n 2) turn one light bulb on and go to room \n 3) turn one light bulb on for 1/2 minutes then turn it off. Proceed to turn a second light on and leave it on.")
    final_choice = convert_strtoint(choice)
    print(f"You choose {final_choice}")
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


