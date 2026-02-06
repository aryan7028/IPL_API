import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)
ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"
balls = pd.read_csv(ipl_ball)
df=balls.merge(matches,on='ID',how='inner')

# All teams played till in ipl

def teams_api():
    all_teams=list(set(list(matches['Team1']) + list(matches['Team2'])))

    teams_dict = {
        'teams':all_teams
    }

    return teams_dict

# teamvsteam api:
def team_vs_team(team1, team2):
    all_teams=list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team1 in all_teams and team2 in all_teams:


        temp=matches[(matches['Team1'] == team1 )&( matches['Team2'] == team2) |(matches['Team1'] == team2 )&( matches['Team2'] == team1)]

        total_matches_played = temp.shape[0]

        matches_won_by_t1=temp[temp['WinningTeam']==team1].shape[0]
        matches_won_by_t2=temp[temp['WinningTeam']==team2].shape[0]
        draws = total_matches_played-(matches_won_by_t1+matches_won_by_t2)

        response = {
            'total matches':total_matches_played,
            'matches won by team1':matches_won_by_t1,
            'matches won by team2':matches_won_by_t2,
            'number of draws':draws,
        }

        return response
    
    else:

        return {'message':'Enter validate name'}
    
# 3rd api which displays record of a team:

def team_record(team_name):
    all_teams=list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team_name in all_teams:



        temp=matches[(matches['Team1']==team_name) | (matches['Team2']==team_name)]
        number_of_matches_played = temp.shape[0]
        number_of_matches_won = temp[temp['WinningTeam']==team_name].shape[0]
        number_of_lost = number_of_matches_played-number_of_matches_won
        win_percentage=(number_of_matches_won/number_of_matches_played)*100
        num_toss_wins = temp[temp['TossWinner'] == team_name].shape[0]
        mostly_matches_won_by =temp[temp['WinningTeam']==team_name]['WonBy'].value_counts().sort_values(ascending=False).index[0]
        stadium_on_which_most_matches_played=temp.groupby('Venue')['ID'].count().sort_values(ascending=False).index[0]


        response = {
            'Number of Matches Played':number_of_matches_played,
            'Number of Matches Won':number_of_matches_won,
            'Number of Matches lost':number_of_lost,
            'Win Percentage of Team':win_percentage,
            'Number of toss wins':num_toss_wins,
            'Mostly Matches Won By':mostly_matches_won_by,
            'Mostly Matches Played in Stadium':stadium_on_which_most_matches_played



        }

        return response
    
    else:

        message = {'message':'Enter a valid team name'}

        return message




# 4th api which display record of boller


def batter_record(batsman):


    

    df=balls.merge(matches,on='ID',how='inner')
    batter_data=df[df['batter'] == batsman]
    num_times_player_of_match=matches[matches['Player_of_Match']==batsman].shape[0]
    batsman_total_runs = batter_data['batsman_run'].sum()
    num_sixes=batter_data[batter_data['batsman_run']==6].shape[0]
    num_fours=batter_data[batter_data['batsman_run']==4].shape[0]
    played_from_teams=list(batter_data['BattingTeam'].unique())
    strike_rate = (batsman_total_runs/batter_data.shape[0])*100

    data ={

        "Number of Times Player of Match":num_times_player_of_match,
        'Total Runs':int(batsman_total_runs),
        'Number of sixes':int(num_sixes),
        'Number of fours':int(num_fours),
        'Played From Teams':played_from_teams,
        'Strike Rate':round(float(strike_rate),4)}
    
    return data