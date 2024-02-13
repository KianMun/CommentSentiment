# Sentiment Classifcation
## Deployed on Flask Server
1.  Navigate where the python file ```keywordsServer.py``` is.
2.  Run ```python keywordsServer.py``` on terminal.
3.  API is deployed on ```http://127.0.0.1:5000/keywords```.
4.  Test using postman.
5.  GET REQUEST JSON format:
   
    ```Example 1:```

    {"text": "Yes its very hard to get an appointment but once I spoke to a doctor I was super impressed with the empathy and clinical expertise. I was not rushed through the appointment"}
    
    Top 10 Keywords Response:

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

    ```Example 2:```

    {"text": "I have always found the receptionist helpful, my experience of the doctors I have seen have been caring ,understanding & professional."}
    
    Top 10 Keywords Response:

    {
    "Top 10 Keywords": [
        "understanding",
        "found",
        "caring",
        "professional",
        "seen",
        "experience",
        "always",
        "helpful",
        "receptionist",
        "doctor"
        ]
    }

    ```Example 3: If comment too short, not enough keywords, will return "" ```

   {"text": "Unfortunately this practice never has appointment! They don’t support or help and just ignore"}

    
    Top 10 Keywords Response:
    
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

6. Model is deployed on Azure: ```https://keywordsserver.azurewebsites.net/keywords```