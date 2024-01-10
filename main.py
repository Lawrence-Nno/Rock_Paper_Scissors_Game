def rock_paper_scissors_game():
    """
    This python script runs the popular 'rock paper scissors' text based game on the console
    :return: A String, the end results
    """

    # The random module
    import random

    # The 3 options in the game
    options = ['rock', 'scissors', 'paper']

    # The Ascii art of the 3 options in the game
    art = [
        """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
        """,
        """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
        """,
        """
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
        """
    ]

    # A while loop to ensure a valid option was chosen before proceeding
    while True:
        try:
            choose = int(input("What do you choose? Type '0' for Rock, '1' for Scissors and '2' for Paper\n"))
        except ValueError:
            print("You must choose either 0, 1 or 2")
        else:
            # An if statement to ensure 0, 1 or 2 is chosen
            if choose > 2 or choose < 0:
                print("You must choose either 0, 1 or 2")
            else:
                break

    human_choice = (options[choose])
    computer_choice = random.choice(options)
    print(f"Human's Choice = {human_choice}")
    print(art[choose])
    print(f"Computer's Choice = {computer_choice}")
    print(art[options.index(computer_choice)])

    # if statements to ensure the accurate result is displayed
    if human_choice == 'rock' and computer_choice == 'scissors':
        print("You win")
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print("You win")
    elif human_choice == 'paper' and computer_choice == 'rock':
        print("You win")
    elif human_choice == computer_choice:
        print("It's a draw")
    else:
        print("You lose")


if __name__ == '__main__':
    rock_paper_scissors_game()
