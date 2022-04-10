# %% Text to Sentences using NLTK this is A FUNcTION TO put text into the df
''' NLTK text to sentences'''
def txt2sentence(txt):
    '''file to sentence using NLTK'''
    import nltk
    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(txt)
    df=pd.DataFrame(sentences)
    return df


    


# %% load packages
import nltk
''' if needed, download punkt'''
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import os
import pandas as pd
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification


# %% Set up working folder and test its existence
# For better examples: https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html

folder='C:\\Users\\LJone\\Fin510\\EDGAR'
exist=os.path.exists(folder)
print(exist)
print(folder)

# %% Load the text file to a string variable
file=open(folder+"\\10k_txt",encoding="latin-1")
text=file.read()

print(text[0:500])

# %% Tokenize 
df_sentence = txt2sentence(text)

df_sentence.to_csv(folder+"\\tsla7a_processed.csv")

sentences = sent_tokenize(text, language="english")

def txt2sentence(txt):
    import nltk
    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text, language="english")
    df=pd.DataFrame(sentences)
    return df

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
inputs = tokenizer(sentences, return_tensors="pt", padding=True)
outputs = finbert(**inputs)[0]

labels = {0:'neutral', 1:'positive',2:'negative'}
for idx, sent in enumerate(sentences):
    print(sent, '----', labels[np.argmax(outputs.detach().numpy()[idx])])


