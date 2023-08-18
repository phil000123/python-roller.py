import random

def main():
    response = "y"
    
    while response == "y":
       
        roll = random.randint(1, 6)
        print_dice(roll)
        response = input("Do you want to roll the dice again? (y/n): ").lower()
    print("Goodbye!")

def print_dice(roll):
    dice_faces = [
        "+-------+",
        "|       |",
        f"|   {roll}   |",
        "|       |",
        "+-------+"
    ]
    
    for line in dice_faces:
        print(line)

if __name__ == "__main__":
    main()
