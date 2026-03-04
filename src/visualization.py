import matplotlib.pyplot as plt
from mplsoccer import Pitch

#function to plot the shots of the selected matches
def plot_event_shots(matches, shots):
    
    fig, ax = plt.subplots(figsize=(12, 8))
    pitch = Pitch(pitch_color='white', line_color='black')
    pitch.draw(ax=ax)
    
    for i in range(len(shots)):
    
        if shots.team_name.values[i] == matches.home_team.values[0]:
            if shots.shot_outcome_name.values[i] == 'Goal':
                pitch.scatter(120 - shots.location_x.values[i], 
                              80 -shots.location_y.values[i], 
                              ax=ax,
                              color='red',
                              marker='h', 
                              s= shots.shot_statsbomb_xg.values[i]*1000)
                plt.text(120 - shots.location_x.values[i],
                         80 -shots.location_y.values[i],
                         shots.player_name.values[i])

            else:
                pitch.scatter(120 -shots.location_x.values[i], 
                              80 - shots.location_y.values[i], 
                              ax=ax,
                              color='red',
                              marker='h', 
                              s= shots.shot_statsbomb_xg.values[i]*1000,
                              alpha=0.3) 

        elif shots.team_name.values[i] == matches.away_team.values[0]:
            if shots.shot_outcome_name.values[i] == 'Goal':
                pitch.scatter(shots.location_x.values[i],
                              shots.location_y.values[i],
                              ax=ax,
                              color='blue',
                              marker='h',
                              s= shots.shot_statsbomb_xg.values[i]*1000)
                plt.text(shots.location_x.values[i],
                        shots.location_y.values[i],
                        shots.player_name.values[i])

            else:
                pitch.scatter(shots.location_x.values[i],
                              shots.location_y.values[i],
                              ax=ax,
                              color='blue',
                              marker='h',
                              s= shots.shot_statsbomb_xg.values[i]*1000,
                              alpha=0.3)
                
    plt.text(15, 5, matches.home_team.values[0] + ' shots')
    plt.text(80, 5, matches.away_team.values[0] + ' shots')
    plt.title('{} \n {} - {} {} X {} {}'.format(matches.competition.values[0], 
                                                matches.match_date.values[0], 
                                                matches.home_team.values[0],
                                                matches.home_score.values[0],
                                                matches.away_score.values[0], 
                                                matches.away_team.values[0]),
    fontsize=16)
    plt.show()
    
#function to save the plot in the outputs/figures folder   
def save_plot(filename, output_dir='outputs/figures'):
    
    import os
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    print(f"✓ Plot saved to: {filepath}")
