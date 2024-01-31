from flask import Flask, request, jsonify
import pickle

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
model = load_model('commentSentiment.pkl')

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

@app.route("/sentiments", methods=["GET"])
def predict_sentiment():
    data = request.get_json()
    text = data["text"]
    
    if(len(text.replace(" ", ""))==0):
        return jsonify({"message": "No comments input!"})
    else:
        preprocessedData = lemmatizer(text)
        sentimentPrediction = model.predict([preprocessedData])
        sentimentPrediction = sentimentPrediction.tolist()

    if(sentimentPrediction[0] == -1):
        sentiment = "Negative"
    elif(sentimentPrediction[0] == 1):
        sentiment = "Positive"

    return jsonify({"Sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)


'''
Negative Sentiment:

  {"text":"when I tried to register to go on doctors list I was told I am not in the catchment area but on the NHS website it can be possible to be out of area despite I am only living 1 mile away. The area is convenient for me as I attend the dental services. Is this service selective and biased."}

  {"text": "I have been ringing for 2 days trying to sort out my medication which was due 2 days ago and is predated and one member of staff has been repeatedly rude to me Refusing to listen to me I am now without medication i really need."}

  {"text": "It is very hard to get an appointment on the phone even if you call at 08:30"}

Positve Sentiment:

{"text": "I've been using this surgery for the past four years and found they have always done their best"}
{"text": "I have always found the receptionist helpful, my experience of the doctors I have seen have been caring ,understanding & professional."}
{"text": "We have had over 6 weeks of our three children being poorly with general childhood illness’. Each time we’ve asked to see a dr the receptionists have been helpful and accommodating and the Drs and Nurses we have seen have been thorough and reassuring. We really appreciate the service from your whole team. Thank you"}



'''