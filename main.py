from fastapi import FastAPI
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

app = FastAPI()

@app.get("/")
def home(): 
    return {"message" : "HoopTalk Python API"}

@app.get("/player/{player_name}")
def get_player_stats(player_name):
    nba_players = players.get_players()
    matching_players = [p for p in nba_players if p['full_name'].lower() == player_name.lower()]
    
    if not matching_players:
        return {"error": "Player not found"}
    
    player_id = matching_players[0]["id"]
    career = playercareerstats.PlayerCareerStats(player_id)
    data = career.get_dict()
    
    return data