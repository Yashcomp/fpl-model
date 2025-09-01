def build_custom_team(player_df, budget=1000):
    """
    Build team with 3 premium DEF starters + 1 backup + 1 fodder
    """
    team = []
    budget_remaining = budget
    
    # 1. Select 3 premium defenders
    defs = player_df[player_df['position'] == 'DEF'].nlargest(10, 'predicted_value_score')
    for _, defender in defs.head(3).iterrows():
        if defender['now_cost'] <= budget_remaining:
            team.append(defender)
            budget_remaining -= defender['now_cost']
    
    # 2. Select 1 backup defender
    backup_def = player_df[(player_df['position'] == 'DEF') & 
                          (~player_df['web_name'].isin([p['web_name'] for p in team]))].nlargest(1, 'predicted_value_score').iloc[0]
    if backup_def['now_cost'] <= budget_remaining:
        team.append(backup_def)
        budget_remaining -= backup_def['now_cost']
    
    # 3. Select 1 fodder defender
    fodder_def = player_df[(player_df['position'] == 'DEF') & 
                          (~player_df['web_name'].isin([p['web_name'] for p in team]))].nsmallest(1, 'now_cost').iloc[0]
    if fodder_def['now_cost'] <= budget_remaining:
        team.append(fodder_def)
        budget_remaining -= fodder_def['now_cost']
    
    # 4. Fill remaining spots with best value players
    remaining_spots = 15 - len(team)
    best_players = player_df[~player_df['web_name'].isin([p['web_name'] for p in team])].nlargest(remaining_spots + 10, 'predicted_value_score')
    
    for _, player in best_players.iterrows():
        if len(team) >= 15:
            break
        if player['now_cost'] <= budget_remaining:
            team.append(player)
            budget_remaining -= player['now_cost']
    
    return pd.DataFrame(team), budget_remaining