def select_optimal_team(player_df, budget=1000, max_players_per_team=3):
    """
    Select optimal FPL team using constraint optimization
    """
    # Create the problem
    prob = pulp.LpProblem("FPL_Team_Selection", pulp.LpMaximize)
    
    # Create decision variables
    player_ids = player_df.index.tolist()
    decisions = pulp.LpVariable.dicts("player", player_ids, cat='Binary')
    
    # Objective function: maximize total predicted points
    prob += pulp.lpSum([decisions[i] * player_df.loc[i, 'predicted_points'] for i in player_ids])
    
    # Constraints
    # Total players
    prob += pulp.lpSum(decisions[i] for i in player_ids) == 15
    
    # Position constraints
    prob += pulp.lpSum(decisions[i] for i in player_ids if player_df.loc[i, 'position'] == 'GKP') == 2
    prob += pulp.lpSum(decisions[i] for i in player_ids if player_df.loc[i, 'position'] == 'DEF') == 5
    prob += pulp.lpSum(decisions[i] for i in player_ids if player_df.loc[i, 'position'] == 'MID') == 5
    prob += pulp.lpSum(decisions[i] for i in player_ids if player_df.loc[i, 'position'] == 'FWD') == 3
    
    # Budget constraint
    prob += pulp.lpSum([decisions[i] * player_df.loc[i, 'now_cost'] for i in player_ids]) <= budget
    
    # Max 3 players per team
    teams = player_df['team_name'].unique()
    for team in teams:
        prob += pulp.lpSum(decisions[i] for i in player_ids if player_df.loc[i, 'team_name'] == team) <= max_players_per_team
    
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    # Get selected team
    selected_players = [i for i in player_ids if decisions[i].varValue == 1]
    return player_df.loc[selected_players]