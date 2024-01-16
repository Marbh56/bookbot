def main():
    #Your main program code here
    print("The program has started")
    with open("books/Frankenstein") as f:
    
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))


if __name__ == "__main__":
    main()