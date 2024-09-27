import json
from flask import Flask, render_template

app = Flask(__name__)

def load_scores():
    score_dict = {}
    with open('data/scores.json') as score_file:
        return json.load(score_file)

def process_above_three(scores):
    above_three = {}
    for score in scores:
        if len(score["submissions"]) >= 3:
            name = score["name"]
            submission = score["submissions"]
            above_three[name] = submission
            return above_three

# @app.route("/")
# def index():
#     # Load scores from provided JSON file for 
#     return render_template("index.html")

def main():
    score_list = load_scores()
    three_plus_submissions = process_above_three(score_list)
    
main()