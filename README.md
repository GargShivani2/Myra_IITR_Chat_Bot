# Myra_IITR_Messenger_Chat_Bot

Myra is my Chat Bot name. I have trained it for the queries inside my college campus IIT Roorkee. But it can trained for anything.
It uses Naive Bayes classifier to predict answers using natural language programing and it deployed on heroku.
You can see the demo on messenger (facebook page name Myra@IITRChatBot).

train.py --> contains the code for training the model

myra.py --> contains the code for predicting the answers

data5.csv --> contains the question-answer set.
You can put up to 200 different classes (5 different questions for each class)
Note : It is recommended you create the data5.csv in ubuntu and use(in windows you may face some problem, rest of the project will work fine in windows)

resmap.py --> contains the answers to the questions mentioned in data5.csv
You can append the answers to this file in the same order as in the data5.csv file

Note : You can train Myra to be used for some specific purposes like queries related to Railway bookings etc. The program is not hard-coded but the domain of answers is limited.

Cheers! Your Chatbot is ready
