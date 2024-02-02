from flask import Flask, request, jsonify
import pickle
import pandas as pd

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize

app = Flask(__name__)

def load_model(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

#Load the model
model = load_model('tfidfVec.pkl')

#Lemmatize function for text preprocesing
def lemmatizer(text):
    lemmatizer = WordNetLemmatizer()
    stopWords = stopwords.words('english')
    #Tokenize
    tokens = word_tokenize(text)
    #Lemmatize
    lemmaToken = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stopWords]
    #Remove punctuations
    lemmaToken = [token for token in lemmaToken if token not in string.punctuation]

    lemmaText = ' '.join(lemmaToken)
    return lemmaText

def keywords_df(preprocessedData, model):
    tfidf_vecs = model.transform([preprocessedData]).toarray()
    df_columns = model.get_feature_names_out()
    df = pd.DataFrame(data=tfidf_vecs, columns=df_columns)
    return df

    

@app.route("/keywords", methods=["GET"])
def summarizeComment():
    data = request.get_json()
    text = data["text"]

    if(len(text.replace(" ", ""))==0):
        return jsonify({"message": "No comments input!"})
    else:
        preprocessedData = lemmatizer(text)
        df_keywords = keywords_df(preprocessedData, model)
        keywords_dict = df_keywords.max().nlargest(10).to_dict()
        keywords_lst = list(keywords_dict.keys())
        keywords = [i if not i.startswith("00") else "" for i in keywords_lst]
        
        
    return jsonify({"Top 10 Keywords": keywords})

if __name__ == "__main__":
    app.run(debug=True)

'''
Text sent:
{"text": "Yes its very hard to get an appointment but once I spoke to a doctor I was super impressed with the empathy and clinical expertise. I was not rushed through the appointment"}

Top 10 Keywords Response
{
    "Top 10 Keywords": [
        "expertise",
        "super",
        "clinical",
        "yes",
        "rushed",
        "empathy",
        "impressed",
        "hard",
        "spoke",
        "appointment"
    ]
}

Text sent:
{"text": "Unfortunately this practice never has appointment! Always ask to call same day for appointment and thought been on time to call never received the appointment. This is frustrating and disappointing. Although I have lots of health issue but fed up to call them. The staff specifically nurses and receptionist are so rude! They don’t support or help and just ignore"}

Top 10 Keywords Response
{
    "Top 10 Keywords": [
        "call",
        "specifically",
        "ignore",
        "fed",
        "never",
        "disappointing",
        "appointment",
        "frustrating",
        "although",
        "unfortunately"
    ]
}

#If text too short, not enough keywords, will return ""

Text sent:
{"text": "Unfortunately this practice never has appointment! They don’t support or help and just ignore"}

Top 10 Keywords Response
{
    "Top 10 Keywords": [
        "ignore",
        "unfortunately",
        "support",
        "never",
        "help",
        "practice",
        "appointment",
        "",
        "",
        ""
    ]
}
'''