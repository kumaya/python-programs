#!/usr/bin/env python2
from win_popup import balloon_tip
import requests
from BeautifulSoup import BeautifulSoup
import re
from time import sleep

SLEEP_INTERVAL = 30
URL = "http://static.cricinfo.com/rss/livescores.xml"


def get_response_from_url(url):
    r = requests.get(url)
    while not r.ok:
            r = requests.get(url)
    return r


def get_required_match_from_live_games():
    resp = get_response_from_url(URL)
    soup = BeautifulSoup(resp.text)
    data = soup.findAll("title")
    # Get Titles of All Match (Includes runs also) and Retain only Team Names.
    # Live games title information starts from data[1]
    for gamenum, game in enumerate(data[1:]):
        print gamenum+1, ":", re.sub(r'\s+', " ", re.sub('[^A-Za-z ]+', '', game.text))
    choice = input("Game number : ")
    # Guid Tag in the xml contains the json id from which website refreshes data.
    json_link = soup.findAll("guid")[choice-1].text
    json_link = re.search(r'\d+',json_link).group()
    live_feed = "http://www.espncricinfo.com/ci/engine/match/%s.json" % json_link
    return live_feed


def get_playing_team_names(liveFeed):
    # Get the playing team names and store it in teamId:teamName dict format
    resp = get_response_from_url(liveFeed)
    playing_teams = dict()
    for team in resp.json().get("team"):
        playing_teams[team.get("team_id")] = team.get("team_name")
    return playing_teams


def get_scores(innings, playingTeams):
    # Get team names from the team ids. Get score information .
    # Prepare the title and score info to display
    batting_team_id = innings.get("batting_team_id")
    batting_team_name = playingTeams[batting_team_id]
    
    bowling_team_id = innings.get("bowling_team_id")
    bowling_team_name = playingTeams.get(bowling_team_id)
    
    runs = innings.get("runs")
    overs = innings.get("overs")
    wickets = innings.get("wickets")
    runRate = innings.get("run_rate")
    target = innings.get('target', 'First Innings')
    title = "%s vs %s"%(batting_team_name, bowling_team_name)
    score = "%s/%s from %s overs \nRunRate : %s \nTarget: %s"%(runs,wickets,overs,runRate, target)
    return title, score


def notify_scores(liveFeed, playingTeams):
    while True:
        r = get_response_from_url(liveFeed)
        innings = r.json().get("live").get("innings")
        (title,score) = get_scores(innings, playingTeams)
        balloon_tip(title,score)
        sleep(SLEEP_INTERVAL)
