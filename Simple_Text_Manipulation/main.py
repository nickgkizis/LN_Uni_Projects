## 0 ##
#reading the text and the stopwords
#removing the newline character (\n)
filename = "text.txt"
with open(filename, encoding="utf-8",
          mode="r") as file1:
                            
    text = file1.read()                          
               

### 1 ###
#splitting by using full stop as a delimiter
#getting the length of the list

def sentence(x):
    sentences = x.split(". ")  
    print("This text contains: \n(" , len(sentences), ") sentences.")  

print("\n## 1 ##\n")
sentence(text)
print("\n## /1 ##\n")


### 2 ###
#cleaning the punctuation
#splitting at the space
#getting the final length of the list

def word(y):
    y = y.replace(",", "").replace(".", "")  
    words = y.split()  
    print("This text contains:\n(", len(words),") words.")  

print("\n## 2 ##\n")
word(text)
print("\n## /2 ##\n")


### 3 ##
def count_sentences(text_0):
    x_count = []
    y_count = []
    sentences = text_0.split(". ")

    #count the spaces and add one to find the ammount of words
    #"repairing" the sentence by adding back the full stop
    for sentence in sentences:  
        if not "." in sentence:  
            sentence = sentence + "."
    #update count
    #update sentence+count
        x_count.append(sentence.count(" ") + 1)  
        y_count.append(sentence + "->" +
                       str(sentence.count(" ") + 1))  
    #sorting by the counter
    x_count = sorted(x_count, reverse=True)
    y_count = sorted(
        y_count,
        reverse=True,
        key=lambda x: int("".join([i for i in x
                                   if i.isdigit()])))  
    #removing the count part
    list_final = []
    for x in y_count:
        left_text = x.partition("-")[0]  
        list_final.append(left_text)

    #Getting the text and the counter separatelly
    for i in range(
            len(x_count)):  
        print("'" + list_final[i] + "'\n", 'Contains (', x_count[i],
              ') words.\n')

print("\n## 3 ##\n")
count_sentences(text)
print("## /3 ##\n")


### 4 ###

def top_five(text):
    #clean punctuation
    #make a list of the words
    text = text.replace(",", "").replace(".", "")  
    words = text.split()  
     #remove duplicate words
    unique_words = [] 
    [unique_words.append(x) for x in words if x not in unique_words]
    #sort by word length (short->long)
    unique_words.sort(key=len)  
    #reverse (long->short)
    unique_words.reverse()  
    #create a list with the five longest
    five_longest = []  
    for word in unique_words[0:5]:
        five_longest.append(word)
        #sort alphabetically
    five_sorted = sorted(five_longest)  
    print("Five longest words in this text ordered alphabetically are:")
    for word in five_sorted:
        print(word)

    

print("\n## 4 ##\n")
top_five(text)
print("\n## /4 ##\n")