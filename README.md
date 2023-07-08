#  COUNTRY QUIZ WEB APPLICATION WITH DJANGO FRAMEWORK & REST API

## Django framework is a powerful and flexible toolkit for building Web Applications and REST API's are most widely used to perform CRUD operations for the given web application.


### Requirements:
- python 3.10
- django 3.8.1


### Installation:

After you have cloned the repository, you should create a virtual environment, so you have a clean python installation. You can do this by running the command.

**`python -m venv env`**

After this, it is necessary to activate the virtual environment, you can get more information about this here
You can install all the required dependencies by running

**`pip install -r requirements.txt`**


### Country API Information:

In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods 
There are typically 4 methods namely - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources. In our case, we use a single method GET to extract country information.

### Use:
A RESTful API with all countries with capitals in the world.
https://countriesnow.space/api/v0.1/countries/capital


### you can install python using pip:
**`pip install python==3.10`**


### You can install django using pip:
**`pip install django==3.8.1`**

#### First, we have to start up Django's development server.
**`python manage.py runserver`**

### URLs & Models

We have two major resources like countrylist (to get the country list from the given REST API) , and check-capital/ to validate the given capital with API values. Hence we will use the following URLS - /check-capital/ is the checking the capital and /countrylist/ collections of country elements, respectively.

#### Only authenticated users can use the API services, for that reason if we try this:
**http://127.0.0.1:8000/countrylist/**

### Checkout the CountryQuiz page
CountryQuiz is a fun and educational web application that tests your knowledge of world capitals. In this quiz, a country name is displayed, and your task is to enter the corresponding capital city for that country. 

- Execute the `python manage.py runserver` command to start the server, which is responsible for running the application. Subsequently, the display will appear as follows.

![image](https://github.com/3Siri/Country_Capital_Quiz/assets/138786856/4e1ac549-0926-4822-bb32-4682fc68f0b1)

- In this process, we choose the desired country and manually input its corresponding capital.

![image](https://github.com/3Siri/Country_Capital_Quiz/assets/138786856/e4ff4c9c-7001-43bc-a521-d368fd426a1b)

- In the case of a correct answer, the application display will appear as follows

![image](https://github.com/3Siri/Country_Capital_Quiz/assets/138786856/c3d804d2-b5a4-40b4-a06c-df2ea430b03a)

- In the case user enters an incorrect capital, message will display as per below.

![image](https://github.com/3Siri/Country_Capital_Quiz/assets/138786856/4ad6fb6a-a1f3-4c2c-9bd7-a88fdd80e219)

- The result will display as follows.

![image](https://github.com/3Siri/Country_Capital_Quiz/assets/138786856/84f03adf-f98e-4204-86c5-064778eb4ac3)
