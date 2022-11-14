![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

![Bootstrap](https://img.shields.io/badge/Bootstrapap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)


![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white)

![Google Cloud]("https://img.shields.io/badge/Google Cloud-4285F4?style=flat-square&logo=Google Cloud&logoColor=white")

![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=flat-square&logo=jQuery&logoColor=white)

![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white)

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white)


 

 

# Weather as You Go 

![Live-Demo](https://WeatherAsYouGo.danielzion.repl.co)

Weather as You Go (WaYG) is a Team project. This App was intended to be a single-page app, which makes use of Open Weather API. This API contains the weather information of different locations and weather forecasts such as temperature, humidity, wind speed etc.
 

## Description

- This webapp was built to to provide both realtime and forecast weather informations. Users all over the world can view the weather informations by inputting the locations. With its responsive design, users can access the webapp via their laptops, desktops, mobile devices, etc without any display issues.


- Google Cloud Services will be used to host the web app. Initially we thought of using Google Cloud Storage to host the Static Web App, but finally decided to go with GCP serverless computing service known as Cloud Run, since a lot of functionalities are to be implemented, in the backend.

- **Technology Used**: This webapp makes use of Python Flask. Flask is a light-weight Python web framework, this greatly influenced our decision in choosing it. Since we agreed that the app will be utilising a microservice architecture. This makes it possible for us to only included relevant functionalities tha we need. It is reassuringly secure and exceedingly scalable.

- Another Google Cloud resource called Dialogflow ES API is used, . Dialogflow is being chosen for this purpose as it has most of the machine learning algorithm inbuilt. We simply have to train the WeatherBot to respond to intents.
 

## Tech Stack
- The project has been divided into four parts namely: Frontend; Backend; Chatbot and Google Cloud Hosting. A Chatbot named "WeatherBot" will be integrated to the Web App/
 

**Client:** Javascript, HTML, CSS, Bootstrap and jQuery.

 

**Server:** Python language, Flask framework, Dialogflow Es and Google Cloud Run.

 

 

## Features

 

`Weather Location Search` Enables users to search for weather info based on location.

 

`Weather Forecast` Enables users to get weather info for a given number of days.

 

`WeatherBot` A Web App Chatbot which helps users navigate easily and also get weather info instead of using the web page.

## Project Schedule/ execution For the project
A GitHub account will be created for the project. The team will be divided into 3 groups working on the different components of the project. This is how the project will be executed for the duration of the project phase:

### Week 1 
- Finalizing the project proposal and submitting the group project.
-  Creating the GitHub account for the project 

### Week 2 
- Working on the Frontend components of the project 
- The front-end component is aimed at enabling the user to access weather information of a particular location, they will see the temperature, humidity and wind speed/ direction of that particular location. React will be mainly utilized for this task. 
- Working on FAQs of the app/ chatbot

 

### Week 3 
- Working on the Back-end components of the project 
- The back end uses the get request, which uses the frontend files that the user sees. This back end has a single route. 
- Defining intents for the chatbot i.e., the likely questions and answers for the users •

 

### Week 4
- During week 4 the app deployment will take place. The deployment will take place on the GCP storage bucket (static website feature) since our app is a single-page application. Chatbot For the chatbot Open Weather API will be used, this will be integrated into Dialogflow through a webhook. This will enable users to ask the chatbot for weather information. The chatbot will be able to send email reports to the user in excel or text formats.



## How to Run Locally

  In your Command line interface:

  

  1. Clone the repository to your local machine :

  ```bash

    git clone 

  ```

  

  2. Enter into the directory :     

  

  3. Fetch for remote updates :      
  

  4. Pull any recent changes from the main branch:  
  

  5. Install a vrtual environment package :        

  

  6. Create a virtual environment : 

  

  7. Activate the virtual environment :   

  

  8. Install dependencies :  

 

  9. Make migrations:       

 

  10. Migrate all models :    

  

  11. Start Local Server:     

  

## How to Contribute

  1. Create a new branch to make your changes: `git checkout -b <your-branch-name>`  and make the required changes.

  

  2. Stage the file:  `git add <your-changed-file>`

  

  3. Commit your file: `git commit -m "<your-message>"`

  

     Also, make sure your commit message is detailed with what you changed and where you changed it.

  

  4. Push your local changes:  `git push origin <your-branch-name>` 

  

     If an error occurs here, it means that someone has made changes to the original file while you were working.

    

     Simply run : `git pull origin main`  to sync your local file with the current main file and run `git push origin <your-branch-name>` again.

    

  5. Visit the remote url on Github to create a pull request.

  

  6. Wait for the team leader to accept your pull request.

 

## License

 

[MIT](https://choosealicense.com/licenses/mit/)


 

## 🚀 About Us 
- We are students of [Google Africa Developers Scholarship](https://training.zuri.team) 2022. We are currently working as Climate Team 6 on a Weather Station App. With our exquisite team of experienced Developers, we hope to deliver a world class web app. We hope our project helps you in your coding journey :v::blush::crossed_fingers:
