import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import re

##1##

with open("Sapir1921_chapter1.txt", encoding="utf-8",mode="r") as file1, open("Muller1861_chapter2.txt",encoding="utf-8",mode="r") as file2, open("stopwordlist.txt",encoding="utf-8",mode="r") as file3:

    text1 = file1.read()
    text2 = file2.read()
    stopwords = file3.read()      #reading all the files

#print(stopwords)
#print(text1)
#print(text2)

def most_frequent(f):           # using the code from the previous assignment

    f = f.lower()
    f = re.sub("(\\$|&|%|!|\\?|\"|\\.|;|,|:|``|\\(|\\))", '', f)
    f = re.sub("--", ' ', f)
    word_s = f.split()
    dic = {}
    for x in word_s:
      if x not in stopwords:
        if not x in dic:
          dic[x] = word_s.count(x)
    sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    head = "Word,Frequency,Length,Chapter\n"   #generating the CSV file format
    data = ""
    for i, n in list(sorted_items)[:10]:
      data = data + i + "," + str(n) + "," + str(len(i)) + "," + str(1) + "\n" # converting everything to a str(type) in order to concatenate

    fff = open("CSV_Format.csv", "w", encoding="utf-8")  #mode here is "w" write, generates a new file overwriting previous information if there is any
    fff.write(head + data)                            #creating the file and writing the first chapter's 10 most frequent words
    fff.close()

most_frequent(text1)

#running the loop again for the second text in order to extract the chapter number
def most_frequent(f):

    f = f.lower()
    f = re.sub("(\\$|&|%|!|\\?|\"|\\.|;|,|:|``|\\(|\\))", '', f)
    f = re.sub("--", ' ', f)
    word_s = f.split()
    dic = {}
    for x in word_s:
      if x not in stopwords:
        if not x in dic:
          dic[x] = word_s.count(x)
    sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    data = ""
    for i, n in list(sorted_items)[:10]:
      data = data + i + "," + str(n) + "," + str(len(i)) + "," + str(2) + "\n"

    fff = open("CSV_Format.csv", "a", encoding="utf-8") # the mode this time is "a" append, it will not overwrite the previous data, it only adds
    fff.write(data)
    fff.close()

most_frequent(text2)

##2##

df = pd.read_csv('CSV_Format.csv', delimiter=',')

#here i call every funtion individually since otherwise the generated graphs are mixed in one
def fig_1():
  sns.lineplot(x="Length", y="Frequency",data =df )
  plt.title("Correlation between word's lenght and its corresponding frequency")
  plt.savefig("len_freq_V1.png")
  plt.clf()

fig_1()


def fig_2():
  sns.scatterplot(x="Length",y="Frequency",hue="Chapter",legend=True,data=df)
  plt.title("Correlation between word's lenght and its corresponding frequency.")
  plt.legend(loc="upper left")
  plt.savefig("scatter_V1.png")
  plt.clf()

fig_2()

def fig_3():
  sns.barplot(x="Frequency",y="Word",hue="Chapter",data= df.sort_values(by="Frequency",ascending=False))
  plt.tight_layout()
  plt.savefig("freq_V1.png")
  plt.clf()

fig_3()

