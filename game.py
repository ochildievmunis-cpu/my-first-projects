import random
print("Я загадал число от 1 до 100!")
secret = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secret and attempts < 7:
    guess = int(input("Угадай число: "))
    attempts = attempts + 1
    if guess > secret:
        print("Меньше!")
    elif guess < secret:
        print("Больше!")
    else:
        print("Поздравляю, ты угадал число!")
    diff = abs(guess - secret)
    if diff <= 5:
        print("Горячо!")
    else:
        print("Холодно!")
