import json
from flask import Flask, render_template, jsonify

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
    # comprehension to return user and the scores are sorted highest to lowest and cut at 24 entries
    valid_users = {name: sorted(scores, reverse=True)[:24] for name, scores in name_and_scores.items()}
    return valid_users

def to_dict(lsts):
    res_dict = {}
    for lst in lsts:
        keys = str(lst[::2])[2:-3]
        values = str(lst[1::2])[1:-2]
        # print(keys)
        # print(values)
        res_dict[keys] = values
    print(res_dict)
    return res_dict
 
def allowed_sum_totals(submissions):
    # comprehension to return user and sum of scores
    sums = {name: sum(submission) for name, submission in submissions.items()}
    return sums

  
    
def ranking(unordered):
    # using lambda function to select the value rather than key for sorting and reverse give highest first
    ordered = sorted(unordered.items(), key=lambda x: x[1], reverse=True)
    return ordered
    
def main():
    score_list = load_scores()
    relevant_data = remove_irrelevant(score_list)
    top_allowed_submissions = process_twentyfour_submissions(relevant_data)
    sum_totals = allowed_sum_totals(top_allowed_submissions)
    sum_rank_list = ranking(sum_totals)
    sum_rank = to_dict(sum_rank_list)
    print(sum_rank)

    # Use decorators for routing
    @app.route("/")
    def index():
        # Load scores to web page using sum_rank value
        return render_template("index.html", sum_rank=sum_rank)
    
main()