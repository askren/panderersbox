from flask import render_template, request, abort

import configuration
from panderer import app
from sqlalchemy import create_engine
import psycopg2
from panderer.get_app_info import get_scores
import candidates

engine=create_engine(configuration.get_engine_string())

con = psycopg2.connect(**configuration.get_conn_dict())


@app.route('/')
@app.route('/index')
@app.route('/input')
def panderer_input():
    return render_template("input.html",
	title = "Panderer's toolBox")

@app.route('/contact')
def panderer_contact():
    return render_template("contact.html",
	title = "Contact Information")

@app.route('/about')
def panderer_about():
    return render_template("about.html",
	title = "About")

@app.route('/output')
def panderer_output():
  #pull 'candidate_name' from input field and store it
  candidate = request.args.get('candidate')

  if candidate not in candidates.all_candidates:
      abort(404)

    #just select the average sentiment scores for the candidate that the user inputs
  comparison = request.args.get('comparison', 'same')
  if comparison != "same" and comparison != "opp":
      abort(400)

  last_name=candidate.title()

  full_name=candidates.all_candidates[candidate].full_name
  same_party=candidates.all_candidates[candidate].party
  opp_party=''
  compared_party=''

  if same_party=='Democrat':
      opp_party='Republican'
  elif same_party=='Republican':
      opp_party='Democrat'

  if comparison=='same':
      compared_party=same_party
  elif comparison=='opp':
      compared_party=opp_party

  acc,auc,comparison_data=get_scores(candidate, comparison,compared_party)

  return render_template("output.html", data=comparison_data, last_name=last_name, full_name=full_name, acc=acc, auc=auc, comparison_party=compared_party, candidate=candidate, comparison=comparison, title="Panderer's Output")

