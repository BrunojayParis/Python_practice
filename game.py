#Guess the secret world

secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
        print("nope!, try again")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("too many times! you're out!")
else:
    print("That's it!! well done!")   


 