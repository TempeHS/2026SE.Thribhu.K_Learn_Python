import emoji

def main():    
    print(f"Output: {emoji.emojize(input("Input your emoji: "), language='alias')}")

main()