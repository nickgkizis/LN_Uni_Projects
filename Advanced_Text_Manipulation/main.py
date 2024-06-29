import re

##1##
filename="Sapir1921_chapter1.txt"
with open(filename, encoding="utf-8",
          mode="r") as file1, open("stopwordlist.txt",
                                   encoding="utf-8",
                                   mode="r") as file2:
                            
    text = file1.read()                                  #reading the text and the stopwords
    stopwords = file2.read()

#print(stopwords)
#print(text)
c_text = text.replace("\n", " ")                         #removing the newline character (\n)

##2##


def long_sent(s):
    sent_dict = {}
    splitted = re.split("\\?|!|\\.",s)                                        #splitting sentences at usual delimiters
    for sent in splitted:
        sents = sent.split()                                                 #spliting sentences into words
        sent_dict[sent] = len(sents)                                         #assigning a lenght to every sentence of the dictionary

    sent_sorted_dict = sorted(sent_dict.items(), key=lambda item: item[1])   #sorting the dictionary
    print("'The longest sentence in the text is:'\n")
    for x,v in list(sent_sorted_dict)[-1:]:                                  #printing the longest sentence after converting the 
      print ("'"+x+".'\n\n'This sentence is ("+str(v)+") words long.'","\n\n","#"*50,"\n") #dictionary into a list
long_sent(c_text)


##3##
def long_word(w):

    word_dict = {}
    w = w.lower()                                              #lowercase conversion
    w = re.sub("(\\$|&|%|!|\\?|\"|\\.|;|,|:|``|\\(|\\))", '', w) #punctuation removal
    w = re.sub("--", ' ', w)                                   #special character substitution
    splitted_words = w.split()                                 #spliting text into words
    for word in splitted_words:                                #creating a dictionary and assigning the word's lenght to each element
        word_dict[word] = len(word)
    #print(word_dict)

    for elem in word_dict.keys():                               #this for loop is removing the hyphenation and the dash
        for letter in elem:                                     #from the character counter, since i chose to include
            if letter == "-":                                   #compound and hyphenated words, i wanted to count only 
                word_dict[elem] -= 1                            #the actual characters.
            elif letter == "'":
                word_dict[elem] -= 1

    word_sorted_dict = sorted(word_dict.items(),
                                   key=lambda item: item[1])    #sorting by word length
    print("'The longest word in the text is:'\n")
    for x,v in list(word_sorted_dict)[-1:]:                     #converting dictionary to a list and printing the last element
      print ("'"+x+"'\n\n'This word is ("+str(v)+") characters long.'","\n\n","#"*50,"\n")

long_word(text)


##4##
def most_frequent(f):
    f = f.lower()                                               #uniforming the text
    f = re.sub("(\\$|&|%|!|\\?|\"|\\.|;|,|:|``|\\(|\\))", '', f)  #removing punctuation
    f = re.sub("--", ' ', f)                                    #handling the special character so we can process compount words
    word_s = f.split()                                          #spliting for every word
    dic = {}
    for x in word_s:
        if x not in stopwords:                                  #removing stopwords
            if not x in dic:                                    
                dic[x] = word_s.count(x)                        #every new dictionary element is assigned its frequency value 
    sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse = True)
                                                                #sorting, reversing and printing after converting the dictionary into a list
    print("'The ten most frequent words in the text, after removing stopwords, are:'\n")

    d=0
    for i,n in list(sorted_items)[:10]:
      d+=1
      print(str(d),"->","'"+i+"',("+str(n)+") occurences.")
    print("\n\n","#"*50,"\n")

most_frequent(text)

def named(n):
    n = re.sub("\\s+|\n"," ",n)                                             #cleaning whitespace
    n = re.sub("^[A-Z]+\\s+[A-Z]+\\:(\\s[A-Z]+){2}","",n)                     #cleaning the problematic title
    n = re.split("\?|\!|\.",n)                                             #splitting sentences at usual delimiters
    cleaned = []
    for sent in n:                                                          #apllying to every sentence
      sent = re.sub("(\\$|&|%|!|\\?|\"|\\.|;|,|:|``|\\(|\\))", '', sent)           #removing punctuation
      sent = re.sub("--", ' ', sent)                                        #handling the special character
      sent = re.sub("^[A-Z][a-z]+-[a-z]+|^[A-Z][a-z]+|^[A-Z]+",'', sent)    #removing the first word in each sentencef
      sent = sent.lower()                                                   #lastly uniforming into lowercase
      #print(sent)
      word_n = sent.split()                                                 #moving to words
      for x in word_n:                                            
        if x not in stopwords:                                              #removing stopwords
          cleaned.append(x)                                                 #adding the remaining wordds to the new list
    #print(cleaned)
    no_dup = [] 
    [no_dup.append(x) for x in cleaned if x not in no_dup]                  #removing duplicates, same way different syntax
    
    joined = " ".join(no_dup)                                               #joining the list back together
    joined = " "+joined                                                     #adding a space so i don't have to create a special regex
    #print (joined)                                                         #just for the first word.
    
    a_to_l = re.findall("\\s[a-l]\w+\\'\w+|\\s[a-l]\\w+\\-\\w+\\-\\w+|\\s[a-l]\w+\\-\\w+|\\s[a-l]\\w+",joined)                #capturing the two groups (a-l), (m-z)
    m_to_z = re.findall("\\s[m-z]\\w+\\'\\w+|\\s[m-z]\\w+\\-\\w+\\-\\w+|\\s[m-z]\\w+\\-\\w+|\\s[m-z]\\w+",joined)                #special regex for compount words

    print("'The named entities from 'a' to 'l',after removing stopwords and duplicates, are:'\n\n")
    print("[List size is ("+str(len(a_to_l))+ ") words long.]\n")
    print(sorted(a_to_l))
    print("\n\n","#"*50,"\n")
    print("'The named entities from 'm' to 'z',after removing stopwords and duplicates, are:'\n\n")
    print("[List size is ("+str(len(m_to_z))+") words long.]\n")
    print(sorted(m_to_z))
  
named(text)