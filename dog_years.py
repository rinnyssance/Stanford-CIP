# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    age = float(input("Enter an age in calendar years: "))
    total = (DOG_YEARS_MULTIPLIER * age)

    print(f"That's {total} in dog years!")
if __name__ == '__main__':
    main()
