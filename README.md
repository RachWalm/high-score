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

1. Docker containers, user accounts and security for the app is not requested so assumed not required. I am aware of Docker and know it would make it easier to run from machine to machine, but I haven't ever used it to build an image etc. with the restricted timescale this won't be included in the project.
2. As it is a single page app I am not going to use a base.html to have a standardised format for the headings and footers etc across the site.
3. The rules provided to calculate the leaderboard needed to be done in reverse order for efficiency of the code. Each step would lead to a new list so that the original data wasn't compromised, with the new list being smaller and simpler than the previous so the processing reduces.
Therefore the processing needs to be done per function:
- remove any users from the list that had less than 3 submissions which would provide a shorter list. This reduced the amount of data that we are processing in future steps. 
- reorder the "submissions" with largest first so that it could be cut at 24 submissions. Check which ones had more than 24 submissions from the original data so that testing can look at those.
- sum the submissions keeping them attached to the person who submitted.
- display it on an HTML page using decorators for routing.

##  Development process

Didn't originally have the JSON file so started with the set up of the front end as didn't want to write algorithm for different named variables.

Set up flask and the routing to produce a HTML page with "hello world!". The function to do this finally became:

```py
# Use decorators for routing
    @app.route("/")
    def index():
        # Load scores to web page using sum_rank value
        return render_template("index.html", sum_rank=sum_rank)
```

Then I got the data and wanted to get that processed as the top priority, as it was more important to get the data processed than have a pretty website with nothing on it. I could use a website I know that outputs python visibly if I ran out of time.

### Questions and responses

#### Questions

1. The task is to provide the SUM of the best submission scores. Without background knowledge of the submissions it seems to me that the data of the sum may not be the best representation (it depends what is intended to be achieved). With the sum coming from between 3 and 24 submissions and no indication of how many submissions it could be misleading data. It could be 3 large submission or 24 tiny submissions. Would an average or indication of number of submission be valuable data for this leaderboard. In a real-life situation I would ask the aim of the board to ensure that the displayed data was valuable, not just what was asked for.
2. For submission can I provide links? Is a github repository link with a README.md adequate for the text of the code and a description of the code/my reasoning/choices? Does the submitted website need to be deployed or just able to run locally? What would be the ideal format for submission? And second best if I can't achieve that?
3. I would assume that priorities would be: firstly functionality and usability, then ease of use, then things like responsiveness and how it looks. Do you have a different order or priorities?

#### Responses

1. That is a good question that I am happy you asked. If you want to include some weighting or some visual hint to help with that problem and make it clearer in the UI, definitely do so. Or equally if you just provide a description of what else you would do, that is also perfectly valid.
2. To be honest this is actually part of the test, to see if people consider it. So yes, a Git repository (gihtub link or equivalent) that contains all someone needs to understand and assess your work is enough. 
3. In terms of deploying it, you don’t need to do that but also feel free to do so if you wish and you think it would add a benefit. -  Like above, putting some thought into how you would do it  (or some notes in the repository with options/ideas) so we can discuss it in the interview would be good.
For that one, what I am looking for is people making a decision on priorities and what is worth doing vs not, then being able to justifying either in some documentation or in the interview later.

#### Set up

A github repository was set up and will be committed to regularly.

Once I had the python connected to a web page as that was the intended display method the data was the priority.

#### Data

The data was looked at and the important factors are:

The original list had 500 entries (len(score_list)).

The data contained some entries that had less than 3 submissions and some greater than 24 so these could be used to test the functionality for those rules. The highest and lowest score could be used to test the calculation.

This means that the functionality to filter out the less than 3 submissions and remove the lowest submission for the over 24 submissions would be necessary (although would have been coded even if not - as other data sets might have them).

#### Get data into run.py

The data was save in VSCode file system /data/scores.json

To allow it to be used for processing:

```py
# Gets all the data from the JSON file
def load_scores():
    with open('data/scores.json') as score_file:
        return json.load(score_file)
```

#### Process the data

Wrote a "main()" app which had a variable to store the returned value from each function. Although we are summing the values as stated in the rules it seemed sensible to make each function modular so the function could be used for other things such as averages or top submission by writing the relevant code and inputting the variable from the stage of the program that was appropriate.

This would also mean if there was plenty of time left over I could do some of the outputs that I thought might be valuable - average / weighting rather than sum are often used.

As per design the first step was to remove the many with under 3 submissions so that we are processing less data. The original list had 500 entries, but once the list had removed all submissions of less than 3 the new list only contained 246 entries, which would require less processing to do the other calculations.

Then had the idea to remove all the additional unused data (name and date from within submission). This would again reduce the size of the data and limit processing and functions having to work round the data that wasn't going to be displayed.

```py
# removes data with less than 3 submissions and irrelevant information on submission name and date
def remove_irrelevant(all_scores):
    # variable to output data
    above_three = {}
    # iterates through data
    for score in all_scores:
        # doesn't process anything with less three submissions to remove all less than three submissions
        if len(score["submissions"]) >= 3:
            # variables
            name = score["name"]
            subs = score["submissions"]
            results = []
            # collects submission scores
            for sub in subs:
                result = sub["score"]
                results.append(result)
                # for development to determine people with more than 24 submissions (remove in deployed)
                # if len(results) >24:
                #     print(name)
            # creates a dictionary with only relevant data and more than 3 submissions
            above_three.update({name: results})
    return above_three
```

As the process of producing this code is of interest to the reader I have left in the code I used to delve through the data and consider the data that had submissions greater than 24 so would require only top submissions being used in the calculation but it is commented out. This allowed me to anticipate what difference the future function would make to the data.

Next function was to have narrow down the data to just taking the top 24 submissions. 

```py
def process_twentyfour_submissions(name_and_scores):
    # comprehension to return user and the scores are sorted highest to lowest and cut at 24 entries
    valid_users = {name: sorted(scores, reverse=True)[:24] for name, scores in name_and_scores.items()}
    return valid_users
```

This used comprehension. The input by this point was the person and all the scores. I realised afterwards when looking back at the data that it could be confusing that I had used the word "name" in variables to signify the person which was the key for some of the nested data. If I had noticed this earlier I would have changed it.

The function takes each {key: value} pair as name_and_scores.items() and considers the key = name and the value = score. It then outputs name: and a processed set of numbers which is sorted with highest first (sorted reverse = True). It then cuts it at using indexes [:24] which as it is sorted drops the lowest values.

The next function needs to calculate the sum of integers in the value section. So iterates over the scores and adds them together.

Allowed_sum_total() function turned it into a list. A dictionary would be much easier to organise and display.

```py
def allowed_sum_totals(submissions):
    # comprehension to return user and sum of scores
    sums = {name: sum(submission) for name, submission in submissions.items()}
    return sums
```

Now it needed to be ranked.

```py
def ranking(unordered):
    # using lambda function to select the value rather than key for sorting and reverse give highest first
    ordered = sorted(unordered.items(), key=lambda x: x[1], reverse=True)
    return ordered
```

I wanted the data as a dictionary so converted to a dictionary and removed the extra punctuation.

```py
def to_dict(lsts):
    #create empty dictionary
    result_dict = {}
    for lst in lsts:
        # for that individual entry take key, turn to string and remove extra punctuation
        keys = str(lst[::2])[2:-3]
        # for that individual entry take value, turn to string and remove extra punctuation
        values = str(lst[1::2])[1:-2]
        # add to dictionary to be output
        result_dict[keys] = values
    return result_dict
```

Flask allows you to pass data to the website so the result was passed to index.html using the decorator routing.

#### Website

The HTML was then written using a for loop to generate the table with the data in it.

The CSS was added to make the site more user appealing and readable.

#### Testing

- Checked that when the users that had less than 3 submissions function had run that it had changed from a dictionary of length 500 to a length of 246.

- Manually calculated the top ranked user with a calculator and got a total score once the lowest submissions (30 total submissions) had been removed found a summed score of 4025 which matched what was displayed on the website.

- Manually calculated the lowest ranked user (3 submissions) summed score of 73 which matched what was displayed on the website. 



Doesn't take account if they are the same score.

pip install Flask

## Technologies used

- VSCode

### languages and frameworks

- python
- Flask
- HTML
- CSS