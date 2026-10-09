from game import WordleGame

if __name__ == "__main__":
    choice = input("Select word length (4, 5, 6) [default 5]: ").strip()
    length = 5
    if choice in ("4", "5", "6"):
        length = int(choice)
    WordleGame(length=length).run()
