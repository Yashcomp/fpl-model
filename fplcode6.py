async def complete_pipeline():
    """
    Complete pipeline from data fetch to team selection
    """
    # Fetch data
    player_data = await get_fpl_data()
    player_data['team_name'] = player_data['team'].map(team_mapping)
    player_data['position'] = player_data['element_type'].map(position_map)
    
    # Feature engineering
    player_data['value_score'] = player_data['form'] / (player_data['now_cost'] / 10)
    
    # Team selection
    optimal_team, budget_remaining = build_custom_team(player_data)
    starting_xi = optimal_team.nlargest(11, 'value_score')
    bench = optimal_team.nsmallest(4, 'value_score')
    
    # Display
    display_team(starting_xi, bench, budget_remaining)
    return optimal_team

# Run the complete pipeline
# final_team = asyncio.get_event_loop().run_until_complete(complete_pipeline())