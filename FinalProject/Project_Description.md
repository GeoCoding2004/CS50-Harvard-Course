# My life

## Video Demo:  <https://youtu.be/xCGHXPCHm7Y>
### Description:

### Layout.html
- This file is the basic form of all the pages in the website. It contains all the links: bootstrap, javascript script, and script to access the charts.. . It uses Jinja for the title of each page which can be changed for each page depending on the elements of the page.

- Also, this file contains the navigation bar which changes depending on the login status. If the user hasn't logged in yet, the navigation bar presents 2 links: the first one for the login page and the second one for the registration page. But if the user signs in, those 2 links will disappear and 6 links will appear: Home, Info, To-Do, Expenses, and Test, each one represents a different page of the website. As well as the logout link that clears the session and returns to the login page.

- Moreover, in the main part of the file, Jinja is used another time but that time for the body of each page.

- And finally, the layout file contains a div with an id of preloader and a script beneath it. This script makes the preloader visible on the screen when it's still loading. And when the loading process is finished, the preloader will disappear and the content of the page will appear.

### Register.html
- This file contains 3 input fields: username, password, and confirmation for the password. I included the "required" word for each input so the user cannot submit it until he has filled all the fields.

- When the user submits, we search using cursor.execute() the table for the users for data with the same username.
If the data is not none, then the user will be redirected to an error page with a message saying: "Username already taken. Please use another username".
Also, the confirmation is checked to see if it's the same as the password. If it isn't the same, an error page will appear with a message.

- Then if all the requirements are verified, a SQLite command will run and the username and password will be stored in the table for users. And the user will be redirected to the login page.

- And under the submit button, there is a link where if the user has already an account, he can go directly to the login page and sign in.



### login.html
- This file contains 2 input fields, one for the username and the other for the password.

- In app.py, with python, we get the input in the username field and the password field. And we check if there is no input. If there is no username or password, the user will be redirected to an error page with a specific message for each case.

- If the username and password fields are filled, a SQLite command will run searching for data with the username that the user wrote.
If there is no data, the error page will appear with a message.
And if the password doesn't match the password in the data, also the error page will appear with another message.

- If everything is correct, we set the variable session[user-id] to be the id of the user. And finally, the user is redirected to the home page.

### home.html
- This page contains only text that sums up all the features of the website.
Each feature with a unique color, and above them all a title welcoming you to my website "My Life".

### Info.html
- Because the height of the page is larger than the preloader height, I put a script to block the scroll option when the preloader is still loading.
After that, when the form is visible, the user can scroll again.

- Then, all the data from the input fields are stored in variables.
Then, we check the "info" table that contains all the data from the info page and we see if the table has data for the current user (with a user_id equal to the session[user_id]).

- If the user submits an empty form and he has no data before, he will be presented with an error page saying "no data provided".

- Else if the user fills the form, the data will be stored in the "info" table with a user_id equal to the session[user_id]

- And then, we count how many rows are there in the table.
And return the the latest data provided that has a user_id of the user

- Finally, the page "allinfo.html" is rendered with the data selected.

### Allinfo.html
- I use the data selected in info.html and I display it in a prewritten paragraph except for some words that are the data that the user has written in the info.html.

- Also, I put a div where the user can upload his image (With a special shape: rounded shape). And beneath it a button to select the file from his device.

- And when the user presses the button and selects the file, a function in javascript (script.js) is called: it changes the background of the div to the photo that the user chose.

- Because storing an image as a blob in a SQLite table is difficult, I chose to put the upload image thing in the allinfo page so when the user submits the image, it will directly be displayed on the page with no need to store any data.

### todo.html
- The to-do page is divided into 2 parts.

    #### 1-Create task:
    - The user types what the task is in an input field, and he chooses the date when the task has to be completed with a calendar. Then, he chooses the importance (or priority) of the task in a dropdown menu.

    - Then the information with the session[user_id] is stored using a SQLite command in a table specific for the tasks called "todo".

    - Then all the tasks from the table with the use_id equal to session[user_id] are selected so that all the tasks of the user are selected.

    - And finally, the page reloads and all the tasks are presented in a table with their date, and importance, as well as a "complete" button that when clicked, uses a SQLite command to delete the task from the table and then reload the page so that the task doesn't appear anymore on the screen.

    #### 2-Search task:
    - The search task part contains an input field where the user writes the task he wants to search and when the click the search button, a SQLite command will be executed.

    - This command will search the table for tasks that have the same name and also the same user_id as the session[user_id] because multiple users can write the same task.

    - This part contains also a search by priority and a search by date feature that work the same as the search by task feature. It searches the table for tasks with the same priority or with the same date as the user has written as well as the same user_id as the session[user_id]

    - And all the searched tasks will be displayed in a table with all their information: task, date, priority, as well as the complete button.

### Expenses.html
- This page contains a little paragraph talking about the importance of a good financial status. And it presents the 2 financial features of this website with 2 links each one redirecting the user to a different page.

    #### 1-budget.html:
    - The first page is the budget tracking system where the user has to fill in some information about his spending and earnings and he has to specify the month and year of this data.

    - When the user submits, a SQLite command is executed to search the table related to the budget (called budget) to see if there is data for this specific month and year. If the user has already submitted data for this date, he will be presented with an error page and a message.

    - If not, all the data will be stored in the table. And all the data in fields related to the income will be added to get the total income that will be displayed when the user submits. The same thing with the spending. And for the saving, the total income minus the total spending gives you the total savings.

    - If you want to search your earnings and spending on a specific date, you can fill the month and year fields in the search section.
    I used a link from Cloudflare to represent the spending in a doughnut chart. I divided each value of spending by the total spending and then multiplied it by 100 to get the percentage of each type of spending.

    - Also, to know the value in dollars of each spending I displayed each one in the specific color used in the chart.

    - And finally, I used a script to block the scrolling during the preload time.

    #### investement.html
    - The second page is the investment contribution system.

    - This page contains a bootstrap card with a photo of Jim Rohn and one of his quotes that mentions the importance of investment.

    - Also, there is a form that the user can fill out, and when he submits it, he will get how much the amount has to contribute each month with an inflation rate of about 2% to get the amount that he wanted to.

    - To get that amount, certain calculations are done. And the result is rendered on the page when the user submits


### iqtest.html
- The concept of this page is that the user is presented with some general questions which he has to answer to see the level of knowledge of the user.

- There are 8 multiple choice questions each one with 4 choices. And 2 text questions where the user has to write the answer.

- When the user clicks the submit button, a function in the script.js file "check()" is called .

- Firstly, this function changes the color of all the false answers of the multiple choice questions to red. And changes the color of all the correct answers to green.

- Then, I created a variable called correct in script.js that keeps track of the number of correct answers that the user has selected.
The function checks for each question the selected answer. If it's the correct answer, the correct variable is incremented by one. The same logic is applied to all the questions.

- And finally, I put a div with a hidden class in the iqtest.html file. I defined this "hidden" class in the styles.css file with a display of none so it doesn't appear before the user submits.

- And when the user submits, I changed the class of the div to be "shown" in the script.js file. I also defined this class in the styles.css file with a display of block which means that it will appear when the user submits.

- And this div contains a prewritten phrase to be displayed with the variable "correct" so the user can see how many answers he got correctly.

- Finally, I put a little script at the end of the iqtest.html file so that when the screen is still loading the user won't be able to scroll down until the screen loads completely.

### error.html
- When there is an error, the user is redirected to error.html page where there is a big "OOPS" and beneath it a message that changes depending on the case.
- And besides it a little character who's ice cream fell down. That represent the failure of accomplishing the action that we wanted to do.


# That's all for my project, THIS WAS CS50!!!!





