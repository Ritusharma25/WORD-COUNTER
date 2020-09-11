import requests
from bs4 import BeautifulSoup
import operator
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll("span", {'class': "a-size-medium a-color-base a-text-normal"}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
        clean_words(word_list)

def clean_words(word_list):
    cleaned_words = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+{}:\"|>?`\[];',./-="
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i]," ")
            if len(word) > 0:
                cleaned_words.append(word)
                print(cleaned_words)

start("https://www.amazon.in/s?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A15417300031%2Cn%3A4149418031%2Cn%3A4149470031&page=2&qid=1596569206&ref=lp_4149470031_pg_2")
