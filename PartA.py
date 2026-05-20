##======================================================================================
## My version of an answer for Question16_A
## LC Comp Sci 2026
##======================================================================================

def calculate_readability_score(text):

    # Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)

    # Initialise the word counters
    word_count = len(words) # Number of words in the list
    short_word_count = 0

    # Initialise the number of sentences
    # Part iii: Added "!" count
    sentence_count = text.count(".") + text.count("!")

    # Part v: count the short words
    for word in words:
        if (len(word) <= 2):
            short_word_count += 1

    print("Short Words:", short_word_count)

    # Calculate the reability score

    # Part vi: comment out original score maths, replace with new version
    # Need to be careful here with brackets to represent the formula correctly

    # score = word_count * sentence_count
    score = 0.4 * ( (word_count / sentence_count) + (100 * ( (word_count - short_word_count) / word_count)))

    score = round(score, 2) # Round the score to 2 d.p.

    # Part vii: complex words counting

    complex_word_count = 0

    for word in words:
        vowel_count=0

        # interate though the vowels, count the number of occurances
        for vowel in "aeiou":
            vowel_count += word.count(vowel)

        # reduce by one if the word ends with 'e'
        if(word[:-1] == 'e'):
            vowel_count -= 1

        if (vowel_count >= 3):
            complex_word_count += 1

    print("Complex Words:", complex_word_count)

    return score

text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

print() ## blank line

# Calculate the score for text1
score1 = calculate_readability_score(text1)
# Part i: print the score
print("Readability Score 1:", score1)

print() ## blank line

# Part ii: repeat the output for text2 and score2
score2 = calculate_readability_score(text2)
print("Readability Score 2:", score2)

# Part iv: compare the scores, output result

print() ## blank line

if (score1 < score2):
    print("The first text is easier to read")
elif (score1 > score2):
    print("The second text is easier to read")
else:
    print("Both scores are the same")

print() ## blank line
