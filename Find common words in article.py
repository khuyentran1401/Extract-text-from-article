pip install newspaper3k

from newspaper import Article

url = 'https://humanparts.medium.com/im-not-weird-you-re-weird-b88bc9ed6621'

article = Article(url)

# Download article

article.download()

# Find the publish date

article.publish_date

article.parse()

text = article.text

article.top_image

# Take a look at the image

from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://miro.medium.com/focal/1200/632/50/37/1*7M8X6ZbcftelY-1BRRhc6Q.jpeg")

article.authors

article.nlp()

article.keywords

article.summary


# # NLTK for Text Processing

pip install nltk

import nltk

nltk.download()


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(text)

text = ' '.join(word for word in text)

# Tokenize words

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)

# Lowercase

tokenized_word = [word.lower() for word in tokenized_word]

# Remove stopwords

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)

filtered_word = []
for word in tokenized_word:
  if word not in stop_words:
    filtered_word.append(word)

# Stemming the word

from nltk.stem import PorterStemmer

ps = PorterStemmer()

stemmed_words = []
for w in filtered_word:
  stemmed_words.append(ps.stem(w))

#See how stemming works
for word in ['thinking', 'felt', 'asked','challenging','devoted']:
    print(ps.stem(word))

# Try with lemmatization and compare it with stemming

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

lem_words = []
for w in filtered_word:
  lem_words.append(lem.lemmatize(w,'v'))
 
for word in ['thinking', 'felt', 'asked','challenging','devoted']:
    print(lem.lemmatize(word,'v'))

from nltk.probability import FreqDist
fdist = FreqDist(lem_words)

most_common = fdist.most_common(20)
most_common

pip install matplotlib

import matplotlib.pyplot as plt

plt.figure(figsize=(20,5))
plt.plot([word[0] for word in most_common], [word[1] for word in most_common])
plt.xlabel('Words')
plt.ylabel('Frequency')


