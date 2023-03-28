import numpy as np
import re
import nltk
import csv
import jieba
import pandas as pd
import contractions
import pandas as pd
import numpy as np
import nltk
import string
import fasttext
import contractions
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import pandas as pd
from pandas import DataFrame
import numpy as np
import nltk
import string
import fasttext
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import os

nltk.download('punkt')
nltk.download('stopwords')

df = DataFrame(pd.read_csv('EN-test.csv'))
#df.columns = ["outline"]


stop_words = set(stopwords.words('english'))

RS=[]
punc = string.punctuation

fd =open("engtoken.csv","w")
writer = csv.writer(fd)

for index, row in df.iterrows():
    result = []
    tokens = [ w for w in word_tokenize(str(row['outline'])) if not w.lower() in stop_words]
    for w in tokens:
        if w not in stop_words:
            result.append(w)
    RS.append(result)
    writer.writerow([result])
fd.close()


