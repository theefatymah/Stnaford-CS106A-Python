import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    your_score = 0 
    
    # TODO: Write your code here!!! :)
    for i in range(NUM_ROUNDS):
        print(f"Round{i + 1}")
        computer_num = random.randint(1,100)
        your_num = random.randint(1,100)
        print(f"Your number is {your_num}")

        choice = input("Do you think your number is higher or lower than the computer number?")
        if choice == "higher" or choice == "Higher":
            if your_num > computer_num:
                print(f"You are right!The computer number was {computer_num}")
                your_score += 1 
            else:
                print(f"Aww,thats incoreect, The computer number was{computer_num}")
        elif choice == "lower" or choice == "Lower":
            if your_num < computer_num:
                print(f"You are right!The computer number was {computer_num}")
                your_score += 1
            else:
                print(f"Aww,thats incorect, The computer number was{computer_num}")
        else:
            print(f"invalid input! Please choos Higher or Lower")
    
    print(f"your total score is {your_score}")
    print(f"Thank you for playing game")  
    

if __name__ == "__main__":
    main()
