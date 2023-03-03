from random import randint


def generate_six_random_number():
    win_numbers = []
    while len(win_numbers) < 6:
        win_number = randint(1, 49)
        if win_number not in win_numbers:
            win_numbers.append(win_number)
    return win_numbers


def add_your_number():
    your_numbers = []
    while len(your_numbers) < 6:
        your_number = input("Write your number: ")
        if your_number not in your_numbers:
            your_numbers.append(your_number)
            print('Succesful added number')
        else:
            print('Your number are in your numbers')
    return your_numbers

price = 3
saldo = 0
how_many_times = 0

start = input('Do you wanna start a lotto (Yes, No): ')
computer = generate_six_random_number()
print(computer)
while start != "No":
    how_many_times += 1
    player = add_your_number()
    saldo += price
    correct_number = 
    if correct_number == 6:
        print(f'You win milion. You played {how_many_times} times and spent {saldo}')
        
    else:
        print(f'You have {correct_number} correct numbers.')
        start = input("Do you wanna play again (Yes, No) ? \n")

















