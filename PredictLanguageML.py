from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy
import pandas as pd
import unidecode

#Formatting lst into proper manner
def formate_lst(lst):
    data = [word.replace("\t", " ") for word in lst]
    data = [word.split(" ") for word in data]
    data = [word[1] for word in data]
    data = [word.lower() for word in data]
    data = [unidecode.unidecode(word) for word in data]
    return data

#Formatting English data
english_data = pd.read_csv("EnglishData.csv")
english_data = list(english_data.English)

#Formatting French data
french_data = pd.read_csv("FrenchData.csv")
french_data = list(french_data.French)
french_data = formate_lst(french_data)

#Formatting Spanish data
spanish_data = pd.read_csv("SpanishData.csv")
spanish_data = list(spanish_data.Spanish)
spanish_data = formate_lst(spanish_data)

#Formatting Italian data
italian_data = pd.read_csv("ItalianData.csv")
italian_data = list(italian_data.Italian)
italian_data = formate_lst(italian_data)

#Formatting Portuguese data
portuguese_data = pd.read_csv("PortugueseData.csv")
portuguese_data = list(portuguese_data.Portuguese)
portuguese_data = formate_lst(portuguese_data)

#Formatting German data
german_data = pd.read_csv("GermanData.csv")
german_data = list(german_data.German)
german_data = formate_lst(german_data)

#Formatting Dutch data
dutch_data = pd.read_csv("DutchData.csv")
dutch_data = list(dutch_data.Dutch)
dutch_data = formate_lst(dutch_data)

#Formatting Polish data
polish_data = pd.read_csv("PolishData.csv")
polish_data = list(polish_data.Polish)
polish_data = formate_lst(polish_data)

#Formatting Czech data
czech_data = pd.read_csv("CzechData.csv")
czech_data = list(czech_data.Czech)
czech_data = formate_lst(czech_data)

#Formatting Romanian data
romanian_data = pd.read_csv("RomanianData.csv")
romanian_data = list(romanian_data.Romanian)
romanian_data = formate_lst(romanian_data)

#Formatting Norwegian data
norwegian_data = pd.read_csv("NorwegianData.csv")
norwegian_data = list(norwegian_data.Norwegian)
norwegian_data = formate_lst(norwegian_data)

#Formatting Swedish data
swedish_data = pd.read_csv("SwedishData.csv")
swedish_data = list(swedish_data.Swedish)
swedish_data = formate_lst(swedish_data)

#Formatting Danish data
danish_data = pd.read_csv("DanishData.csv")
danish_data = list(danish_data.Danish)
danish_data = formate_lst(danish_data)

#Formatting Finnish data
finnish_data = pd.read_csv("FinnishData.csv")
finnish_data = list(finnish_data.Finnish)
finnish_data = formate_lst(finnish_data)

#Transforming data into usable form
counter = CountVectorizer()
counter.fit(english_data + french_data + spanish_data + italian_data + portuguese_data + german_data + dutch_data + polish_data + czech_data + romanian_data + norwegian_data + swedish_data + danish_data + finnish_data)
training_counts = counter.transform(english_data + french_data + spanish_data + italian_data + portuguese_data + german_data + dutch_data + polish_data + czech_data + romanian_data + norwegian_data + swedish_data + danish_data + finnish_data)
training_labels = [0] * 1000 + [1] * 1000 + [2] * 1000 + [3] * 1000 + [4] * 1000 + [5] * 1000 + [6] * 1000 + [7] * 1000 + [8] * 1000 + [9] * 1000 + [10] * 1000 + [11] * 1000 + [12] * 1000 + [13] * 1000

#Trains data using a classifier
classifier = MultinomialNB()
classifier.fit(training_counts, training_labels)