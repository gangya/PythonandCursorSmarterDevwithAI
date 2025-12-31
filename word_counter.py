# Program to count words in a text file
# 1. Ask the user for the path or the name of file
# 2. Open the file and read the text
#3. separatethe the text into words 
#4. count the number of words
#5. Display the most common words in text and  their frequency
from collections import Counter

def start_word_counter():
    file_path = input("Enter the path or name of the file: ")
    try:
        with open(file_path, 'r') as file:
         word_counter(file)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e} in start_word_counter function")

def word_counter(file):
    try:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"The number of words in the file is: {word_count}")
        #print(f"words are: {words}")
        most_common_words = Counter[str](words).most_common(5)
        print(f"The most common words in the file are: {most_common_words}")
        for i in most_common_words:
            #print(type(i))
            print(f"The word {i[0]} appears {i[1]} times")        
    except Exception as e:
        print(f"An error occurred: {e} in word_counter function")
    
if __name__ == "__main__":
    start_word_counter()