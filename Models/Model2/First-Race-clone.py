def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']
    
    if((track_width/2) - distance_from_center <= 0.4 and all_wheels_on_track == True and is_left_of_center == True ):
        reward = 1.0
    else:
        reward = 1e-3
    

    
    return float(reward)