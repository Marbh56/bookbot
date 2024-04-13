def main():
    book = "books/frankenstein.txt"
    def sort_on(dict):
        return(dict["num"])
    
    with open(book) as file:
        file_contents = file.read()
        words = file_contents.split()
        count = 0
        char_dict = {}
        alpha_dict = {}
        #Generatins a list or words 
        for word in words:
            word = word.lower()
            count += 1
            for letter in word:
                if letter not in char_dict:
                    char_dict[letter] = 1
                else:
                    char_dict[letter] += 1
        #Generating a dictionary of alphabetical character counts
        for letter in char_dict:
            if letter.isalpha():
                print(letter)
                print(char_dict[letter])
                alpha_dict[letter] = char_dict[letter]
        #Generate a list of dictionaries
        alpha_list = []
        for letter in alpha_dict:
            l = {"name":letter, "num":alpha_dict[letter]}
            alpha_list.append(l)
        alpha_list.sort(key=sort_on,reverse=True)


        print(f"--- Begin report of {book} ---")
        print(count)
        print("")
        for i in range(0,len(alpha_list)):
            print(f"The '{alpha_list[i]["name"]}' character was found {alpha_list[i]["num"]} times")
        print("--- End report ---")
        
        

      
main()