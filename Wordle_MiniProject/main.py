import random
import string


def main():

    with open("words.txt") as f:
        words = [line.strip() for line in f]
        word = random.choice(words).upper()
    # print(word)

    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    reset = '\033[0m'
    print(f"{red}red means the letter is Wrong{reset}")
    print(f"{yellow}yellow means the letter is Misplaced{reset}")
    print(f"{green}green means the letter is Right{reset}")
    print("\nGUESS THE WORD\nYOU GOT 5 ATTEMPTS")

    def check_word(target, text):
        wrong = False

        for t in text:
            if t.isdigit() or t.isspace() or (t in string.punctuation):
                wrong = True
                break

        if len(text) != 5:
            print("Enter a proper word")

        elif wrong:
            print("Enter a proper word")

        else:
            w = ""
            for t in range(5):
                if target[t] == text[t]:
                    w += f"{green}{text[t]}{reset}"
                elif text[t] in target:
                    w += f"{yellow}{text[t]}{reset}"
                else:
                    w += f"{red}{text[t]}{reset}"
            print(w)

    found = False
    for i in range(5):
        guess = str(input("\nEnter the Word : "))
        check_word(word, guess.upper())
        if word == guess.upper():
            print(f"You guessed it in {i + 1} attempt")
            found = True
            exit()

    if not found:
        print(f"\nThe word is {green}{word}{reset}\nTry Again...")


if __name__ == "__main__":
    main()
