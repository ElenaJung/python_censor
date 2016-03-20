def censor(text,word):
    whole_word = ""
    whole_string = ""
    last_letter = 0
    for letter in text:
        last_letter = last_letter + 1
        if letter == " ":
            if whole_string == "" and whole_word != word:
                whole_string = whole_word
            else:
                if whole_word != word:
                    whole_string = whole_string + " " + whole_word
            whole_word = ""
        else:
            whole_word = whole_word + letter
            if whole_word == word:
                if whole_string != "":
                    whole_string = whole_string + " "
                for i in range(len(word)):
                    if whole_string == "":
                        whole_string = "*"
                    else:
                        whole_string = whole_string + "*"
            elif last_letter == len(text):
                whole_string = whole_string + " " + whole_word
    return whole_string

text = raw_input("Type a sentence:")
word = raw_input("Type the word you want to censor:")
print censor(text, word)
