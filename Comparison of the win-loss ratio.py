import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df_Lakers = pd.read_csv('LA Lakers.csv')
df_Suns = pd.read_csv('Phoenix Suns.csv')
df_Warriors = pd.read_csv('Golden State Warriors.csv')

df_Suns = df_Suns.rename(columns={df_Suns.columns[0]: 'Season'})
dfs = [df_Lakers, df_Suns, df_Warriors]

for df in dfs:
    df['W/L ratio'] = df['W'] / (df['W'] + df['L'])
    df.set_index('Season', inplace=True)

df_combined = pd.DataFrame({
    'Golden State Warriors': df_Warriors['W/L ratio'],
    'LA Lakers': df_Lakers['W/L ratio'],
    'Phoenix Suns': df_Suns['W/L ratio']
})

fig, ax = plt.subplots(figsize=(20, 12))
gspec = gridspec.GridSpec(12, 20)

Warriors_graph = plt.subplot(gspec[0:3, 0:-4])
Suns_graph = plt.subplot(gspec[-4:-1, 0:-4])
combined_graph = plt.subplot(gspec[3:-4, 0:-4])
Lakers_graph = plt.subplot(gspec[1:-2, -4:])

df_Warriors = df_Warriors.iloc[::-1]
df_Suns = df_Suns.iloc[::-1]

team_colors = {'Golden State Warriors': 'blue', 'LA Lakers': 'purple', 'Phoenix Suns': 'orange'}

combined_graph.plot(df_combined)
Warriors_graph.plot(df_Warriors.index, df_Warriors['W/L ratio'], color=team_colors['Golden State Warriors'])
Suns_graph.plot(df_Suns.index, df_Suns['W/L ratio'], color=team_colors['Phoenix Suns'])
Lakers_graph.plot(df_Lakers['W/L ratio'], df_Lakers.index, color=team_colors['LA Lakers'])
Lakers_graph.yaxis.tick_right()
Warriors_graph.xaxis.tick_top()

for team, color in team_colors.items():
    df_combined[team].plot(ax=combined_graph, color=color, label=team)

combined_graph.legend()

for graph in [combined_graph, Warriors_graph, Suns_graph, Lakers_graph]:
    if graph == combined_graph:
        for index, item in enumerate(graph.get_xticklabels()):
            if index != 0 and index % 5 != 0:
                item.set_visible(False)
            else:
                item.set_rotation(45)
                if index == 0:  
                    item.set_text('')  

    elif graph != Lakers_graph:
        for index, item in enumerate(graph.get_xticklabels()):
            if index % 5 != 0:
                item.set_visible(False)
            else:
                item.set_rotation(45)
    else:
        for index, item in enumerate(graph.get_yticklabels()):
            if index != 0 and index % 5 != 0:
                item.set_visible(False)
        for item in graph.get_xticklabels():
            item.set_rotation(45)

combined_graph.set_xlabel('')

plt.show()
