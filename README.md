Weather as You Go (WaYG) is a Team project that decides to weather app called WaYG.  this app is a single-page app, which makes use of Open Weather API. This API contains the weather information of different locations and weather forecasts.  It is proposed that the app will have a simple user interface whereby a GCP serverless computing service known as Cloud Run will be used to deploy it.  For this project we will be using Google resources such as the Dialogflow ES API, the app will be utilising a microservice architecture.  Dialogflow is being chosen for this purpose as it has most of the machine learning done.  
The project will be divided into four parts namely: Frontend; Backend; Chatbot and Google cloud hosting. This app will be using a Chatbot named (?????).

Project Schedule/ execution
For the project, a GitHub account will be created for the project.  The team will be divided into 3 groups working on the different components of the project. This is how the project will be executed for the duration of the project phase:

Week 1
    • Finalizing the project proposal and submitting the group project.
    • Creating the GitHub account for the project
Week 2
    • Working on the Frontend components of the project
    • The front-end component is aimed at enabling the user to access weather information of a particular location, they will see the temperature, humidity and wind speed/ direction of that particular location.  React will be mainly utilized for this task.
    • Working on FAQs of the app/ chatbot

Week 3
    • Working on the Back-end components of the project
    • The back end uses the get request, which uses the frontend files that the user sees. This back end has a single route.
    • Defining intents for the chatbot i.e., the likely questions and answers for the users
    • 

Week 4
During week 4 the app deployment will take place.  The deployment will take place on the GCP storage bucket (static website feature) since our app is a single-page application. 
Chatbot 
For the chatbot Open Weather API will be used, this will be integrated into Dialogflow through a webhook.  This will enable users to ask the chatbot for weather information.  The chatbot will be able to send email reports to the user in excel or text formats. 

Problem Identified 
With the constant weather changes people need reliable sources of weather to stay updated.
