from cricinfo.parse_cricinfo_json import get_playing_team_names, get_required_match_from_live_games, notify_scores

liveFeed=get_required_match_from_live_games()
playingTeams = get_playing_team_names(liveFeed)
notify_scores(liveFeed, playingTeams)
