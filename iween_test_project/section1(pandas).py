import pandas as pd

df = pd.read_csv('../ipl_dataset.csv')
print(df)


# total_matches
total_matches = df['id'].nunique()
print("Total number of matches:", total_matches)


column_names = df.columns.tolist()
print("Column names:", column_names)

print(df.head())  #head

print(df.describe())  #describe


#Which player has won the most “Player of the Match” awards in games decided on the final ball?
close_matches = df[(df['win_by_runs'] == 1) | (df['win_by_wickets'] == 1)]
top_player = close_matches['player_of_the_match'].value_counts().idxmax()
print("Top player in close finishes:", top_player)


#Which team has the highest number of wins where the victory margin was greater than 50 runs? 
big_wins = df[df['win_by_runs'] > 50]
top_team = big_wins['winner'].value_counts().idxmax()
print("Team with most big wins (>50 runs):", top_team)


# Which of the two umpires (umpire1 or umpire2) has officiated more matches involving the Kolkata Knight Riders?
kkr_matches = df[(df['team1'] == 'Kolkata Knight Riders') | (df['team2'] == 'Kolkata Knight Riders')]
umpire1_count = kkr_matches['umpire1'].value_counts()
umpire2_count = kkr_matches['umpire2'].value_counts()
combined = (umpire1_count + umpire2_count).sort_values(ascending=False)
top_umpire = combined.idxmax()
print("Umpire with KKR matches:", top_umpire)

# How many times has the team that won the toss also set a target and won the match? 
bat_and_win = df[(df['toss_decision'] == 'bat') & (df['toss_winner'] == df['winner'])]
print("Toss winners who chose to bat and won:", bat_and_win.shape[0])







