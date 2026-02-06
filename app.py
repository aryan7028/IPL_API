import pandas as pd
import numpy as np
from flask import Flask,jsonify,request
import ipl

app = Flask(__name__)

@app.route('/')

def home():

    return "Hello Aryan"

@app.route("/api/teams")

def teams():
   
   """Gives name of all teams which have played in ipl """

   teams=ipl.teams_api()
   

   return jsonify(teams)

# second api(required input of team1 and team2)
@app.route('/api/teamvteam')
           
def teamvteam():
    """Gives track recore of 2 teams"""

    team1=request.args.get('team1')
    team2=request.args.get('team2')

    response = ipl.team_vs_team(team1,team2)

    return jsonify(response)

# third api(Which display team record)

@app.route('/api/team-record')

def team_record():
    
    """Function to display team record"""

    team = request.args.get('team')

    response= ipl.team_record(team_name=team)

    return jsonify(response)


# 4th api which display record of a batsman

@app.route('/api/batsman-record')

def batter_record():

    batsaman = request.args.get('batsman')

    data = ipl.batter_record(batsman=batsaman)

    return jsonify(data)

































           
app.run(debug=True)