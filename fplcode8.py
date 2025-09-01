def display_team(starting_xi, bench, budget_remaining):
    """
    Clean display of the selected team
    """
    print("FINAL FPL SQUAD")
    print("=" * 40)
    print(f"Budget Remaining: £{budget_remaining/10:.1f}m\n")
    
    print("STARTING XI")
    print("=" * 25)
    
    for position in ['GKP', 'DEF', 'MID', 'FWD']:
        players = starting_xi[starting_xi['position'] == position]
        if not players.empty:
            print(f"\n{position}:")
            for _, player in players.iterrows():
                print(f"  {player['web_name']} ({player['team_name']}) - £{player['now_cost']/10:.1f}m")
    
    print("\nBENCH")
    print("=" * 25)
    for i, (_, player) in enumerate(bench.iterrows(), 1):
        print(f"{i}. {player['web_name']} ({player['team_name']}) - £{player['now_cost']/10:.1f}m - {player['position']}")
    
    print(f"\nTotal Cost: £{(1000 - budget_remaining)/10:.1f}m")
    print(f"Players: {len(starting_xi) + len(bench)}")

# Usage example
# optimal_team, remaining_budget = build_custom_team(player_data)
# starting_xi = optimal_team.nlargest(11, 'predicted_value_score')
# bench = optimal_team.nsmallest(4, 'predicted_value_score')
# display_team(starting_xi, bench, remaining_budget)