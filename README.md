# Sentiment Classifcation
## Deployed on Flask Server
1.  Navigate where the python file ```commentSentimentServer.py``` is.
2.  Run ```python commentSentimentServer.py``` on terminal.
3.  API is deployed on ```http://127.0.0.1:5000/sentiments```.
4.  Test using postman.
5.  GET REQUEST JSON format:
    Negative Sentiment:

    {"text":"when I tried to register to go on doctors list I was told I am not in the catchment area but on the NHS website it can be possible to be out of area despite I am only living 1 mile away. The area is convenient for me as I attend the dental services. Is this service selective and biased."}

    {"text": "I have been ringing for 2 days trying to sort out my medication which was due 2 days ago and is predated and one member of staff has been repeatedly rude to me Refusing to listen to me I am now without medication i really need."}

    {"text": "It is very hard to get an appointment on the phone even if you call at 08:30"}

    Positve Sentiment:

    {"text": "I've been using this surgery for the past four years and found they have always done their best"}
    {"text": "I have always found the receptionist helpful, my experience of the doctors I have seen have been caring ,understanding & professional."}
    {"text": "We have had over 6 weeks of our three children being poorly with general childhood illness’. Each time we’ve asked to see a dr the receptionists have been helpful and accommodating and the Drs and Nurses we have seen have been thorough and reassuring. We really appreciate the service from your whole team. Thank you"}


6. Results will retun as JSON object ```{"Sentiment": "Positive}``` or ```{"Sentiment": "Negative}```