secret_number = 42
def guess_number():
    print(
        """
        This is an interactive guessing game!
        You have to enter a number between 1 and 99 to find out the secret number.
        Type 'exit' to end the game.
        Good luck!

        """
    )
    count = 0
    while 1:
        print("What's your guess between 1 and 99?")
        num = input(">>")
        while not num.isnumeric():
            print("Try with numeric input")
            num = input(">>")
        count += 1
        if int(num) == secret_number and count == 1 and secret_number == 42:
            print(f"The answer to the ultimate question of life, the universe and everything is 42. Congratulations! You got it on your first try!")
            break
        if int(num) == secret_number and count == 1:
            print(f" Congratulations! You got it on your first try!")
            break
        if int(num) == secret_number:
            print(f"You won in {count} attempts!")
            break
        if int(num) < secret_number:
            print("Too low!")
        if int(num) > secret_number:
            print("Too high!")
        

if __name__ == "__main__":
    guess_number()