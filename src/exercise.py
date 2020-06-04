from random import randint

def main():

    print("I'm going to try and guess your number!")

    high = 10
    low = 1
    #Creating variables for high and low values

    while True:
    #Creating while loop to keep the process running until answer is correct

        try:

            guess = randint(low, high)
            #Generates a random integer between the high and low variables

            user = input("Is " + str(guess) + " your number? ")
            #Asks for user input for number

            if user == "yes":
            #Checks if the computers guess was correct
                print("I guessed your number!")
                break
                #Breaks from loop, ends the process

            elif user == "no":
            #Checks if the computers guess was incorrect
                highlow = input("Is your number higher or lower than " + str(guess) + "? ")
                #Created a variable asking for input to find whether the number is higher or lower than the guess

            if highlow == "higher":
                low = guess + 1
            #If the number is higher, the low variable changes from 1 to the value of the guess + 1 to narrow down guesses

            elif highlow == "lower":
                high = guess - 1
            #If the number is lower, the high variable changes from 10 to the value of the guess - 1 to narrow down guesses

        except:
            print("If the guessed number is correct type 'yes'.")
            print("If the guessed number is incorrect type 'no'")
            print("If your number is higher than the guessed number type 'higher'")
            print("If your number is lower than the guessed number type 'lower'")
        #Error handling in case user input is incorrect

if __name__ == '__main__':
    main()
