from random import randint

print("Welcome to Casino")
answer = randint(1,50)

playing = True

while playing:
    user_choice = int(input('Choose number (1 - 50):'))
    if user_choice == answer:
        print('Congtraturation!!')
        playing = False
    if user_choice < answer:
        print('up')
    if user_choice > answer:
        print('down')