from random import randint

def main():

    print("I'm going to try and guess your number!")

    high = 10
    low = 1

    while True:

        guess = randint(low,high)
        user = input("Is " + str(guess) + " your number? ")

        if user == str("yes"):
            print("That's the correct answer!")
            break

        elif user == str("no"):
            highlow = input("Is your number higher or lower than " + str(guess) + "? ")

        if highlow == str("higher"):
            low = guess + 1

        elif highlow == str("lower"):
            high = guess - 1

if __name__ == '__main__':
    main()
