# Clean and prepare the data
position_map = {1: 'GKP', 2: 'DEF', 3: 'MID', 4: 'FWD'}
player_data['team_name'] = player_data['team'].map(team_mapping)
player_data['position'] = player_data['element_type'].map(position_map)

# Convert string columns to numeric
numeric_columns = ['selected_by_percent', 'form', 'ict_index', 'expected_goals', 
                   'expected_assists', 'expected_goal_involvements']
for col in numeric_columns:
    player_data[col] = pd.to_numeric(player_data[col], errors='coerce').fillna(0)

# Create advanced features
player_data['points_per_million'] = player_data['points_per_game'] / (player_data['now_cost'] / 10)
player_data['minutes_per_million'] = player_data['minutes'] / (player_data['now_cost'] / 10)
player_data['goal_involvements'] = player_data['goals_scored'] + player_data['assists']
player_data['expected_goal_involvements'] = player_data['expected_goals'] + player_data['expected_assists']
player_data['value_flag'] = (player_data['points_per_million'] > player_data['points_per_million'].median()).astype(int)