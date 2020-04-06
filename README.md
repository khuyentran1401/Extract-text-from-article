# About this project
This project extracts the text from an article using Python Article Library and uses NLTK (Natural Language Processing Toolkit) to preprocess the text and extract the most common words in the article

# Tools
* Newspaper3k: tool to scrape article
* NLTK: tool to process text

# Steps
* Scrape articles with newspaper3k
```javascript
from newspaper import Article

url = 'https://mystudentvoices.com/it-took-me-2-years-to-get-1000-followers-life-lessons-ive-learned-throughout-the-journey-9bc44f2959f0'
article = Article(url)

article.download()
```
* Find the publish date
```javascript
article.publish_date
```
* Extract image
* Find the author
* Find the keywords
* Find the summary
* Preprocessing with NLTK
  * Tokenize text
  * Lowercase and remove stopwords
* Visualization the frequency of words with Matplotlib
![image](https://github.com/khuyentran1401/Extract-text-from-article/blob/master/images/Screenshot%202020-04-05%2021.39.00.png)



# Tutorial blog
Find the Medium article for this repository [here](https://medium.com/@khuyentran1476/find-common-words-in-article-with-python-module-newspaper-and-nltk-8c7d6c75733)

