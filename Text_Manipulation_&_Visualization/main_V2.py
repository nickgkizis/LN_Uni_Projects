import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import re

##1##

# Reading all the files
with open("Sapir1921_chapter1.txt", encoding="utf-8", mode="r") as file1, \
     open("Muller1861_chapter2.txt", encoding="utf-8", mode="r") as file2, \
     open("stopwordlist.txt", encoding="utf-8", mode="r") as file3:

    text1 = file1.read()
    text2 = file2.read()
    stopwords = set(file3.read().split())  # Convert stopwords to a set for faster lookup

def most_frequent(f, stopwords, chapter):
    f = f.lower()
    f = re.sub(r"(\$|&|%|!|\?|\"|\.|;|,|:|``|\(|\))", '', f)
    f = re.sub("--", ' ', f)
    word_s = f.split()
    dic = {}
    for x in word_s:
        if x not in stopwords:
            if x not in dic:
                dic[x] = word_s.count(x)
    sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    data = ""
    for i, n in sorted_items[:10]:
        data += f"{i},{n},{len(i)},{chapter}\n"
    return data

# Generating the CSV data
header = "Word,Frequency,Length,Chapter\n"
data = header
data += most_frequent(text1, stopwords, 1)
data += most_frequent(text2, stopwords, 2)

# Writing to the CSV file
with open("CSV_Format.csv", "w", encoding="utf-8") as fff:
    fff.write(data)

##2##

df = pd.read_csv('CSV_Format.csv', delimiter=',')

# Plotting functions
def fig_1():
    sns.lineplot(x="Length", y="Frequency", data=df)
    plt.title("Correlation between word's length and its corresponding frequency")
    plt.savefig("Len_Freq_V2.png")
    plt.clf()  # Clear the current figure

def fig_2():
    sns.scatterplot(x="Length", y="Frequency", hue="Chapter", legend=True, data=df)
    plt.title("Correlation between word's length and its corresponding frequency")
    plt.legend(loc="upper left")
    plt.savefig("Scatter_V2.png")
    plt.clf()  # Clear the current figure

def fig_3():
    sns.barplot(x="Frequency", y="Word", hue="Chapter", data=df.sort_values(by="Frequency", ascending=False))
    plt.tight_layout()
    plt.savefig("Freq_V2.png")
    plt.clf()  # Clear the current figure

fig_1()
fig_2()
fig_3()
