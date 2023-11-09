def song_recommender(song, artist):


    ################################## IMPORT LIBRARIES ##################################    
    import streamlit as st
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    import pandas as pd   
    import pickle
    import random
    from random import randint
    from pandas import json_normalize
    ################################## IMPORT NECESSARY FILES ##################################
    top100 = pd.read_csv('../SongRecommenderJupyter/top.csv')
    spot = pd.read_csv('../SongRecommenderJupyter/spotify_songs_clusters.csv')
    secrets_file = open("../secrets.txt","r")
    string = secrets_file.read()
    secrets_dict={}
    
    for line in string.split('\n'):     
        if len(line) > 0:
            secrets_dict[line.split(':')[0]]=line.split(':')[1]
    
    #InitializeSpotiPy with user credentials
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=secrets_dict['cid'],
                                                           client_secret=secrets_dict['csecret']))
    
    
    
    ################################## TAKE SONG AND ARTIST NAME ##################################
      
    song = song.lower()
    artist = artist.lower()

    ################################## IF SONG IN TOP 100 ##################################
    if song in list(top100['track']):
        num = random.randint(0,len(top100))
        st.text(f"HOT HOT HOT!, we also recommend: '%s', by %s." %(top100['track'][num],top100['artist'][num]))    
        
    
    ################################## IF NOT IN TOP 100 ##################################
    elif song not in list(top100['track']):
    
    
    
    ################################## CONNECT TO API ##################################
    
                
                    
            
        ################################## SEARCH FOR SONG ##################################
        
        
        
        results = sp.search(q= artist + song, limit=10)
        
        
        
        
        ################################## EXTRACT & TRANSFORM FEATURES ##################################

        
        ######### Loading the model and scalers from the file using pickle ########

        KM = pickle.load(open('../SongRecommenderJupyter/models_scalers/kmeans.pkl','rb'))
        scaler = pickle.load(open('../SongRecommenderJupyter/models_scalers/scaler.pkl','rb'))        
        
        
        #EXTRACT
        mini_df = pd.DataFrame({'features': sp.audio_features(results['tracks']['items'][0]['uri'])})
        
        
        #NORMALISE
        features = json_normalize(mini_df['features']).drop(columns= ['key', 'uri', 'duration_ms','mode', 'time_signature', 'type', 'id', 'track_href', 'analysis_url'], axis=1)
        
        
        #SCALE
        features_scaled = scaler.transform(features)
        
        
        
        ################################## FIND CLUSTER ##################################
        
               
        
        #DETERMINE CLUSTER NUMBER
        
        
        clusternum = KM.predict(features_scaled)[0]
        
        #FIND RANDOM SONG IN FILTERED DATAFRAME BY CLUSTER NUMBER 
        clusdf = spot[spot['cluster'] == clusternum].reset_index(drop = True).iloc[randint(0,len(spot[spot['cluster'] == clusternum])-1)]
        
        
        
        
        ################################## OUTPUT THE SONG ##################################
        
        
        #SEARCH FOR SONG IN SPOTIFY
        outresults = sp.search(q= clusdf[0] + clusdf[1], limit=10)
        
        
        
        #RECOMMEND SONG, ARTIST, AND PROVIDE LINK
        st.write("We recommend '%s', by %s."  %(outresults['tracks']['items'][0]['name'], outresults['tracks']['items'][0]['album']['artists'][0]['name']))
        st.write("Follow: %s to listen to the song" %(outresults['tracks']['items'][0]['external_urls']['spotify']))
     