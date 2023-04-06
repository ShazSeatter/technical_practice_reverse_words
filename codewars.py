def spin_words(sentence):
    words = sentence.split()
    # print(sentenceArr)
    # ['Hello', 'my', 'name', 'is', 'Timothy']

    for word in range(len(words)):
        if len(words[word]) >= 5: #this if statement returns the words with 5 or more letters in it \
                # next I have to reverse those words and then put the sentence back together 
            words[word]=words[word][::-1] # this has reversed the words 
    reversed_string = ' '.join(words)
    print(reversed_string)
    return reversed_string

# the function needs a conditional statement to check if a word containers greater or equal to 5 letters 
# if its true then the word gets reversed 


assert spin_words('Hello my name is Timothy') == 'olleH my name is yhtomiT'