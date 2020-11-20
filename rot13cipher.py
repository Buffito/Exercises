import string

def decipher(text):
    temp = [] 
    min = 65
    max = 90
    deciphered_text = ''
    for c in text:
        if c.isalnum():
            temp.append(ord(c) + 13)
        else:
            temp.append(ord(c))

    x = 0

    for c in temp:
        if c > max:
            x = c - max
            c = x + min - 1

        deciphered_text = deciphered_text + chr(c)

    print(deciphered_text)
   

def main():
    text = input("Give text to decipher ")
    text = text.upper()
    decipher(text)

if __name__ == "__main__":
    main()    
    
