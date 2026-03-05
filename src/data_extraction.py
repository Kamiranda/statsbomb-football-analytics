import pandas as pd
import json
import sys
from data_processing import coordinates

#function to read the json file and create a dataframe with the information of the matches
def info_json(path):
    
    with open(path + '/competitions.json') as f:
        competitions = json.load(f)
        
    competition_id = []
    competition_name = []
    
    for competition in competitions:
        
        if competition['competition_id'] not in competition_id:
            competition_id.append(competition['competition_id'])  
              
        if competition['competition_name'] not in competition_name:
            competition_name.append(competition['competition_name'])
            
    df_competition = pd.DataFrame()
    df_competition['id'] = competition_id
    df_competition['Competition'] = competition_name
    df_competition.set_index('id', inplace=True)
    
    print('*'*38)
    print(df_competition, '\n')
    id_competition = int(input('Which competition do you want to analyze:'))
    
    season_id = []
    season_name = []

    for season in competitions:
        
        #filter the seasons of the selected competition
        if season['competition_id'] == id_competition:
            
            if season['season_id'] not in season_id:
                season_id.append(season['season_id'])
                
            if season['season_name'] not in season_name:
                season_name.append(season['season_name'])
                
    df_season = pd.DataFrame()
    df_season['id'] = season_id
    df_season['Season'] = season_name
    df_season.set_index('id', inplace=True)
    
    print('*'*38)
    print(df_season, '\n')
    id_season = int(input('Which season do you want to analyze: '))
    
    with open(path + '/matches/' + str(id_competition) + '/'+ str(id_season) + '.json', encoding='utf-8') as f:
        matches = json.load(f)
        
    df = pd.json_normalize(matches)
    
    columns = ['home_team.home_team_name','away_team.away_team_name','home_score','away_score', 
               'match_id','match_date','competition.competition_name','competition_stage.name']
    
    df = df[columns].copy()
    df.columns = ['home_team', 'away_team', 'home_score', 'away_score', 'match_id', 'match_date', 
                  'competition','stage']
    df.set_index('match_id', inplace=True)
    df.sort_values('match_date', inplace=True)
    
    print('*'*38)
    print(df, '\n')
    id_match = int(input('Which match do you want to analyze: '))
    df = df[df.index == id_match]
    
    return df

#function to read the json file and create a dataframe with the information of the events
def event_data(path, match_id, event=True):
   file_name = '/events/'+ str(match_id) + '.json'
   with open(path + file_name, encoding='utf-8') as f:
      data = json.load(f)
      
   df = pd.json_normalize(data, sep='_')
   df = coordinates(df)
   
   if event == True:
      print(df.type_name.unique(), '\n')
      event = input('Which event do you want to analyze: ')
      df = df[df.type_name == event]
      
   return df