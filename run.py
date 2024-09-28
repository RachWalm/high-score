import json
from flask import Flask, render_template

app = Flask(__name__)

# Gets all the data from the JSON file
def load_scores():
    with open('data/scores.json') as score_file:
        return json.load(score_file)

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
                # put in during development so that I could determine which people had more than 24 scores
                # if len(results) >24:
                #     print(name)
            # creates a dictionary with only relevant data and more than 3 submissions
            above_three.update({name: results})
    return above_three

def process_twentyfour_submissions(name_and_scores):
    valid_users = {name: sorted(scores, reverse=True)[:24] for name, scores in name_and_scores.items()}
    scores_only = valid_users.values()
    
   
    
# Use decorators for routing
# @app.route("/")
# def index():
#     # Load scores from provided JSON file for 
#     return render_template("index.html")

def main():
    score_list = load_scores()
    relevant_data = remove_irrelevant(score_list)
    top_allowed_submissions = process_twentyfour_submissions(relevant_data)
    
main()