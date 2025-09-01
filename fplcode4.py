# Prepare features for model
feature_columns = [
    'now_cost', 'selected_by_percent', 'form', 'points_per_game', 'minutes',
    'goals_scored', 'assists', 'clean_sheets', 'saves', 'bonus', 'bps', 'ict_index',
    'expected_goals', 'expected_assists', 'expected_goal_involvements',
    'minutes_per_million', 'goal_involvements', 'team_strength'
]

X = player_data[feature_columns].copy()
y = player_data['points_per_million']

# Convert remaining object columns to numeric
for col in X.select_dtypes(include=['object']).columns:
    X[col] = pd.to_numeric(X[col], errors='coerce').fillna(0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Model MAE: {mae:.4f}")

# Feature importance
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importance.head(10))