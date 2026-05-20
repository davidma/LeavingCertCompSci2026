##======================================================================================
## My version of an answer for Question16_B
## LC Comp Sci 2026
##======================================================================================

## Initialise variables to keep track
total_score = 0
high_score = 0
high_word = ''

## Initial value - Yes, we want to play
play_again = 'Y'

print() ## Blank line

## keep looping as long as the answer is 'Y' or 'y'
while(play_again.upper() == 'Y'):

    word = input("Enter a word: ")

    ## We only allow [A-Za-z] words - no numbers or symbols
    if (not word.isalpha()):
        print("Invalid word.")

        ## Skip to the next iteration of the loop (ask again)
        continue

    ## Uppercase the word
    word = word.upper()

    ## Start scoring
    score = 0

    ## Vowels are worth 1 point each
    for letter in "AEIOU":
        score += (word.count(letter) * 1)

    ## Some letters are worth 5 points each
    for letter in "VWXYZ":
        score += (word.count(letter) * 5)

    ## All remaining letters are worth 3 points each
    for letter in "BCDFGHJKLMNPQRST":
        score += (word.count(letter) * 3)

    ## Add this score to the total
    total_score += score

    ## Print current rounds results, and current total
    print(f"Word: {word}, Score: {score}, Total score: {total_score}")

    ## Check if this was a new high scoring word
    ## If so, record it...
    if(score > high_score):
        high_score = score
        high_word = word

    ## finally, check if we want to play again
    play_again = input("Play again? [Y/N]: ")


# Final output - total score and the high scoring word

print()
print(f"Your total score was: {total_score}")
print(f"The highest scoring word was {high_word}, {high_score} points")
