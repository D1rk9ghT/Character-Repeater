def generate_character_string(character, count):
    """
    Generate a string containing the specified character repeated a given number of times.
    
    :param character: Character to repeat.
    :param count: Number of times to repeat the character.
    :return: String with the character repeated.
    """
    return character * count

def main():
    # Get user input for the number of repetitions
    try:
        count = int(input("Enter the number of times to repeat 'A': "))
        if count < 0:
            raise ValueError("The number must be a non-negative integer.")
        
        # Generate the string with 'A' repeated `count` times
        result = generate_character_string('A', count)
        
        # Print the result
        print(result)
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")

if __name__ == "__main__":
    main()
