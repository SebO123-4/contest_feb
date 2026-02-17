alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
        print(line) # instead of print, you should start decoding
        #count vowels
        #index the alphabet via the vowel count to get letter
        #collect all letter
with open("secret.txt") as f:
    for line in f:
        count = 0


        for char in line.lower():
            if char in vowel:
                count += 1


        if count < len(alphabet):
            message += alphabet[count]
        else:

            message += alphabet[count % len(alphabet)]

print("Decoded message:", message)

