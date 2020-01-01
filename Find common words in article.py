#!/usr/bin/env python
# coding: utf-8

# # Python Article Libary

# In[1]:


pip install newspaper3k


# In[2]:


from newspaper import Article


# In[3]:


url = 'https://humanparts.medium.com/im-not-weird-you-re-weird-b88bc9ed6621'


# In[4]:


article = Article(url)


# Download article

# In[5]:


article.download()


# Find the publish date

# In[6]:


article.publish_date


# In[7]:


article.parse()


# In[8]:


text = article.text


# In[9]:


article.top_image


# Take a look at the image

# In[10]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://miro.medium.com/focal/1200/632/50/37/1*7M8X6ZbcftelY-1BRRhc6Q.jpeg")


# In[11]:


article.authors


# In[12]:


article.nlp()


# In[13]:


article.keywords


# In[14]:


article.summary


# # NLTK for Text Processing

# In[15]:


pip install nltk


# In[16]:


import nltk


# In[17]:


nltk.download()


# Remove punctuation

# In[18]:


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(text)

text = ' '.join(word for word in text)


# Tokenize words

# In[19]:


from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)


# Lowercase

# In[20]:


tokenized_word = [word.lower() for word in tokenized_word]


# Remove stopwords

# In[21]:


from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)


# In[22]:


filtered_word = []
for word in tokenized_word:
  if word not in stop_words:
    filtered_word.append(word)
    


# Stemming the word

# In[23]:


from nltk.stem import PorterStemmer

ps = PorterStemmer()

stemmed_words = []
for w in filtered_word:
  stemmed_words.append(ps.stem(w))

#See how stemming works
for word in ['thinking', 'felt', 'asked','challenging','devoted']:
    print(ps.stem(word))


# Try with lemmatization and compare it with stemming

# In[24]:


from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()


# In[25]:


lem_words = []
for w in filtered_word:
  lem_words.append(lem.lemmatize(w,'v'))
  


# In[26]:


for word in ['thinking', 'felt', 'asked','challenging','devoted']:
    print(lem.lemmatize(word,'v'))


# In[27]:


from nltk.probability import FreqDist
fdist = FreqDist(lem_words)


# In[28]:


most_common = fdist.most_common(20)
most_common


# In[29]:


pip install matplotlib


# In[30]:


import matplotlib.pyplot as plt


# In[31]:


plt.figure(figsize=(20,5))
plt.plot([word[0] for word in most_common], [word[1] for word in most_common])
plt.xlabel('Words')
plt.ylabel('Frequency')


# In[ ]:




