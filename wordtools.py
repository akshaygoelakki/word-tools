import string
#import string to use functions like punctuation,rstrip,lstrip
print("enter 1 for text input")
#using text 
print("enter 2 for text file input")
#using text file
word_count={}
#dictionary to store words 
text_type_input=int(input())

if text_type_input==1:
    text_to_count_words=input()
elif text_type_input==2:
    filename=input()
    try:
        text_to_count_words=open(filename,"r")
    except:
        print("filenot found,please recheck")
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
else:
    print("enter valid input")
for lines in text_to_count_words:
    lines=lines.rstrip()
    lines=lines.lstrip()
    words = lines.split()
    #rstrip Remove spaces to the right of the string
    #lstrip Remove spaces to the left of the string
    #Split a string into a list where each word is a list item
    for char in words:
        char = char.translate(str.maketrans('', '', string.punctuation))
        #translate()	Returns a translated string
        #maketrans()	Returns a translation table to be used in translations
        if char in word_count:
            word_count[char]+=1
        else:
            word_count[char] = 1
while True:
    print("\nChoose what you want :\n1:show me as i have entered text.\n2: show in alphabetical order\n3: show ordered by count of words.\n4: show me total word count.\n5: show me total number of characters.\n6:Thanks and GoodBye !\n")
    
    #The format() method formats the specified value(s) and insert them inside the string's placeholder.
    #The placeholder is defined using curly brackets: {}
    #The format() method returns the formatted string.
    a = input(">>")
    if a == "1":
      print("words ordered as appeared in text")
      for i in word_count:
            print("{0:15}".format(i),word_count[i])
    if a == "2":
        print("words in alphabatically order")
        for key in sorted(word_count.keys()) :
          print(str("{0:15}{1}".format(key,str(word_count[key]))))
    if a=="3":
        print("words ordered by count")
        sorted_wordList = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_wordList:
          print(("{0:20}{1}".format(i[0],i[1])))
    if a=="4":
        c=0
        for i in word_count.values():
            c+=i
        print("total words are:",c)
    if a=="5":
        c=0
        for i in word_count:
            c+=len(i)
        print("total characters are:",c)
    if a=="6":
        print("GoodBye!")
        
