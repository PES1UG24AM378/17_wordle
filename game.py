import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        valid_words = [w for w in WORDS if len(w) == length]
        if not valid_words:
            self.target = "a" * length
        else:
            self.target = random.choice(valid_words)
        self.history = []

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")
        guesses = 0
        while guesses < 6:
            guess = input("> ").strip().lower()
            if guess == "q":
                return
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue
                
            guesses += 1
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            
            # Print history
            for g, f in self.history:
                print(f"{g}: {' '.join(f)}")
            
            if guess == self.target:
                print("Solved!")
                self._print_summary()
                return
                
        print("The word was:", self.target)
        self._print_summary()

    def _print_summary(self):
        print("\nSession Summary:")
        for g, f in self.history:
            print(f"{g}: {' '.join(f)}")
