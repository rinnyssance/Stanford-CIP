def main():
    # Create your variables
    MERCURY = .376
    MARS = 0.378
    VENUS = .889
    JUPITER = 2.36
    SATURN = 1.081
    URANUS = .815
    NEPTUNE = 1.14


    # Ask for the weight on Earth
    weight = float(input("Enter a weight on Earth: "))

    # Calculate Mars weight
    mercury_result = round(weight * MERCURY, 2)
    mars_result = round(weight * MARS, 2)
    venus_result = round(weight * VENUS, 2)
    jupiter_result = round(weight * JUPITER, 2)
    saturn_result = round(weight * SATURN, 2)
    uranus_result = round(weight * URANUS)
    neptune_result = round (weight * NEPTUNE)

    # Print result
    print("The equivalent weight on Mercury: ", mercury_result)
    print("The equivalent weight on Mars:", mars_result)
    print("The equivalent weight on Venus:", venus_result)
    print("The equivalent weight on Juputer:", juputer_result)
    print("The equivalent weight on Saturn:", saturn_result)
    print("The equivalent weight on Uranus:", uranus_result)
    print("The equivalent weight on Neptune:", neptune_result)
    
if __name__ == "__main__":
    main()
