import tkinter as tk
import random

def guess_the_number():
    """Generates a random number and challenges the user to guess it (GUI version)."""
    
    def check_guess():
        nonlocal attempts
        try:
            guess = int(guess_entry.get())
            attempts += 1
            
            if guess < secret_number:
                result_label.config(text="Too low! Try again.")
            elif guess > secret_number:
                result_label.config(text="Too high! Try again.")
            else:
                result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
                guess_button.config(state=tk.DISABLED)  # Disable the button after correct guess
        except ValueError:
            result_label.config(text="Invalid input. Please enter a number.")
        
        guess_entry.delete(0, tk.END)  # Clear the entry field

    secret_number = random.randint(1, 100)
    attempts = 0

    window = tk.Tk()
    window.title("Guess the Number")
    
    instruction_label = tk.Label(window, text="I'm thinking of a number between 1 and 100.")
    instruction_label.pack(pady=10)

    guess_label = tk.Label(window, text="Enter your guess:")
    guess_label.pack()

    guess_entry = tk.Entry(window)
    guess_entry.pack(pady=5)

    guess_button = tk.Button(window, text="Check Guess", command=check_guess)
    guess_button.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

if __name__ == "__main__":
    guess_the_number()



    