#DEVPSU Project 4
#NAME: Bruce Gashirabake
text = input("Enter your message: ")
words = text.split()
result = []
vowels="aeiouAEIOU"
for word in words:
    if word[0] in vowels:
        word=word+ "yay"
        result.append(word)
    else:
        while word[0] not in vowels:
            word = word[1:] + word[0]
        word += "ay"
        result.append(word)
final_message = " ".join(result)
print(final_message[0] + final_message[1:])