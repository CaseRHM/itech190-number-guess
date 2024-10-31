import random 

def main():
    attempts = 0
    secret_number = random.randrange(100)
    print("I have chosen a number between 1 and 100. Can you guess it?")
    while True:
        guess = input("please guess a number between 1 and 100: ")
        attempts += 1

        #non numberic condition check
        if guess.isalpha():
             break

        if int(guess) == secret_number:
            print("congrates! secret num was {} & took {} attempts".format(secret_number , attempts))
            break
        #if else statement to decide to print the guees too hig
        #or guess too low message
        if int(guess) < secret_number:
            print("Too low")
            continue
        else:
            print("Too high")
            continue


if __name__ == "__main__":
    main()