import random

def main():
    sides = input("How many sides does your dice have? ")
    number = random.randint(1, int(sides))

    print(f"Your roll is {number}")
if __name__ == '__main__':
    main()
