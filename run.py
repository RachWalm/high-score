import json
from flask import Flask, render_template

app = Flask(__name__)

def load_scores():
    with open('data/scores.json') as score_file:
        return json.load(score_file)

def remove_irrelevant(all_scores):
    above_three = {}
    for score in all_scores:
        if len(score["submissions"]) >= 3:
            name = score["name"]
            subs = score["submissions"]
            results = []
            for sub in subs:
                result = sub["score"]
                results.append(result)
            above_three.update({name: results})
    print(len(above_three))
    return above_three

def process_twentyfour_submissions(name_and_scores):
    for name_and_score in name_and_scores:
        scores = name_and_score.value()
    
    

# @app.route("/")
# def index():
#     # Load scores from provided JSON file for 
#     return render_template("index.html")

def main():
    score_list = load_scores()
    relevant_data = remove_irrelevant(score_list)
    print(relevant_data)
    top_allowed_submissions = process_twentyfour_submissions(relevant_data)
    
main()