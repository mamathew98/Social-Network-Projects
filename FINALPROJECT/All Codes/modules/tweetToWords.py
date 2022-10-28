import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer


def tweetToWords(tweet):
    """Convert tweet text into sequence of words"""

    stemmer = SnowballStemmer("english")

    lemmatizer = WordNetLemmatizer()

    # remove all urls
    text = removeUrl(tweet)
    # remove non letters
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    # remove all single characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    # Remove single characters from the start
    text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
    # Substituting multiple spaces with single space
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # Removing prefixed 'b'
    text = re.sub(r'^b\s+', '', text)
    # convert to lowercase
    text = text.lower()
    nltk_tokenizer = RegexpTokenizer(r'\w+')
    words = nltk_tokenizer.tokenize(re.sub(r'\d+', '', text))
    words = [lemmatizer.lemmatize(word) for word in words
             if word not in set(stopwords.words('english')) and word.isalpha()]
    return ' '.join(words)


def removeUrl(text):
    pattern = r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((' \
              r'[^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,' \
              r'<>?«»“”‘’]))'
    match = re.findall(pattern, text)
    for m in match:
        url = m[0]
        text = text.replace(url, '')
    return text
