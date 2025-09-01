# Fetch current player data from FPL API
async def get_fpl_data():
    async with aiohttp.ClientSession() as session:
        fpl_session = FPL(session)
        try:
            players = await fpl_session.get_players(include_summary=True) 
            players_list = []
            for player in players:
                players_list.append(player.__dict__)
            players_df = pd.DataFrame(players_list)
            return players_df
        except Exception as e:
            print(f"Error: {e}")
            return pd.DataFrame()

# Get team mapping
team_mapping = {
    1: 'Arsenal', 2: 'Aston Villa', 3: 'Burnley', 4: 'Bournemouth', 
    5: 'Brentford', 6: 'Brighton', 7: 'Chelsea', 8: 'Crystal Palace',
    9: 'Everton', 10: 'Fulham', 11: 'Leeds', 12: 'Liverpool',
    13: 'Man City', 14: 'Man Utd', 15: 'Newcastle', 16: "Nott'm Forest",
    17: 'Sunderland', 18: 'Spurs', 19: 'West Ham', 20: 'Wolves'
}

# Run the data fetch
player_data = asyncio.get_event_loop().run_until_complete(get_fpl_data())