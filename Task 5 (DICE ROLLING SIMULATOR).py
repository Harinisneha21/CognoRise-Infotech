import random

def roll_dice(num_sides, num_rolls):
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times:")
    for roll in range(num_rolls):
        result = random.randint(1, num_sides)
        print(f"Roll {roll + 1}: {result}")

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            num_rolls = int(input("Enter the number of rolls: "))
            if num_sides <= 0 or num_rolls <= 0:
                print("Please enter positive values for the number of sides and rolls.")
                continue
            roll_dice(num_sides, num_rolls)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        play_again = input("Do you want to roll the dice again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for using the Dice Rolling Simulator!")
            break

if __name__ == "__main__":
    main()
