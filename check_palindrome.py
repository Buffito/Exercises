import string

def format_string(text):
    boolean_li = []
    text = text.lower().translate(str.maketrans('','',string.punctuation)).replace(' ','')
    j = len(text) - 1
    for i in range(int(len(text)/2)):
        if j >= 0:
            if text[i] == text[j]:
                boolean_li.append(True)
            j -= 1   
            

    if len(boolean_li) > 0:
        print("Word is a palindrome!")
    else:
        print("Word is not a palindrome!")   

def main():
    text = input("Give word to check if it is a palindrome ")
    format_string(text)

if __name__ == "__main__":
    main()    
    
#checks if user-given word is a palindrome after space and punctuation removal
