def count_words(text):
    """
    Function to count the number of words in the given text.
    
    Parameters:
    text (str): The input text.
    
    Returns:
    int: The number of words in the input text.
    """
    words = text.split()  # Splitting text into words by whitespace
    return len(words)

def get_user_input():
    """
    Function to prompt the user for input and handle any errors.
    
    Returns:
    str: The user input (sentence or paragraph).
    """
    while True:
        try:
            user_input = input("Please enter a sentence or paragraph: ").strip()
            if not user_input:
                raise ValueError("Input cannot be empty. Please enter a valid text.")
            return user_input
        except ValueError as e:
            print(e)

def main():
    """
    Main function to handle user input, count words, and display the result.
    """
    try:
        # Prompting the user for input
        user_input = get_user_input()
        
        # Counting the number of words
        word_count = count_words(user_input)
        
        # Displaying the word count
        print("Word count:", word_count)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
