from pyfiglet import Figlet
import random
import sys

def main():
    try:
        figlet = Figlet()
        arg1 = sys.argv[1]
        match arg1:
            case '-f':
                if sys.argv[2] in figlet.getFonts():
                    figlet.setFont(font=sys.argv[2])
                    text = input("Input text: ")
                    print("\n\n\n")
                    print(figlet.renderText(text))
            case '-l':
                fonts = figlet.getFonts()
                for i in range(len(fonts)):
                    print(fonts[i])
            case _:
                raise Exception
    
    except Exception as e:
        print("Invalid usage")
        print(f"DEBUG || {e}")
        sys.exit(-1)

main()