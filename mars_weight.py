def main():
    # Create your variables
    mars = 0.378

    # Ask for the weight on Earth
    weight = float(input("Enter a weight on Earth: "))

    # Calculate Mars weight
    result = round(weight * mars, 2)

    # Print result
    print("The equivalent weight on Mars:", result)

if __name__ == "__main__":
    main()
