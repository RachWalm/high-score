# High Score

## Planning

Initially I was missing the scores.json file mentioned in the pdf. This was requested and provided by Alice Eadle by email.

Task copied from request

Using the json data provided, build a web application that has the capability to:
- Load, process and store the json data in the system
- Calculate the leaderboard rankings based on the rules defined above
- Display the top leaderboard users on a webpage


The data that is required in the leaderboard copied from request

- Users are ranked by the sum of their best submission scores
- For each user, only scores from their best 24 submissions count
- A user must have at least 3 submissions to appear in the rankings

### Backend

This is a python technical test so python language must be used. Therefore, the data processing will be done on the back end based on python. I am familiar with Flask therefore will use Flask for data handling.

### FrontEnd

As a limited amount of time is available, it seems reasonable that a simple webpage will suffice. User accounts or confidentiality seems excessive as logically you want to display the top scores for everyone to see. Therefore, using just HTML and CSS initially. If interactivity is later decided upon (rather than just a display) JavaScript can be used. But this will be time dependent when calculated data is displayed.

### Storage

As the information in this example isn't going to be updated etc and is already stored in a JSON file in-memory storage should be sufficient and connecting to a database or an input is unnecessary.

### Design decisions

1. Docker containers and security for the app is not requested so assumed not required.
2. As it is a single page app I am not going to use a base.html to have a standardised format for the headings and footers etc.
3. The rules provided to calculate the leaderboard needed to be done in reverse order for efficiency of the code. Each step would lead to a new list so that the original data wasn't compromised.
- remove any users from the list that had less than 3 submissions which would provide a shorter list and the extraneous data about dates and the name of the challenge which is irrelevant for this challenge. This is unnecessary processing/storing of data not required in this challenge. 
- reorder the submissions so that it could be cut at 24 submissions and check which ones had more than 24 submissions




Didn't originally have the JSON file so started with the set up of the front end as didn't want to write algorithm for different named variables.


The original list had 500 entries (len(score_list)), but once the list had removed all submissions of less than 3 the new list only contained 246 entries, which would require less processing to do the other calculations.

Then had the idea to remove all the additional unused data (name and date from within submission).

pip install Flask

## Technologies used

- VSCode

### languages and frameworks

- python
- Flask