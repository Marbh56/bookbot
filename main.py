def main():
    #Your main program code here
    print("The program has started")
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = count_letters(text)
    report = generate_report(count_letters(text))    
    
    print(f"{num_words} words found in the document")
    #print(num_letters)
    

def get_num_words(text):
    words = text.split()
    return len(words)
        
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def lower_case(text):
    return text.lower()

def count_letters(text):
    char_count_dictionary = {}
    
    text = lower_case(text)
    for letter in text:
        if letter.isalpha():
            if letter in char_count_dictionary:
                char_count_dictionary[letter] = char_count_dictionary[letter] + 1
            elif letter not in char_count_dictionary:
                char_count_dictionary[letter] = 1
    return char_count_dictionary

def generate_report(char_count_dictionary):
    char_count_list = list(char_count_dictionary.items())
    sorted_char_count_list = sorted(char_count_list, key=lambda x: x[1], reverse=True )
    print("-- Begin report ---")
    for char, count in sorted_char_count_list:
        print(f"the '{char}' character was found {count} times")
    print("--- End report ---")
    
if __name__ == "__main__":
    main()