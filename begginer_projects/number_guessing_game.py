import random

computer_choice = random.randint(1, 10)
attempts = 3

def get_choice():
    while True:
        try:
            user_choice = int(input('Enter a guess between (1-10): '))
            if 1 <= user_choice <= 10:
                return user_choice
            else:
                print('Number must be between 1 and 10')
        except ValueError:
            print('Please enter a valid number')

def check_win(user, computer):
    if user == computer:
        print('🎉 You win!')
        return True
    elif user > computer:
        print('Number too high')
    else:
        print('Number too low')
    return False

while attempts > 0:
    user_choice = get_choice()
    
    if check_win(user_choice, computer_choice):
        break

    attempts -= 1
    print(f'Attempts left: {attempts}')

if attempts == 0:
    print(f'😢 You lose! The number was {computer_choice}')
