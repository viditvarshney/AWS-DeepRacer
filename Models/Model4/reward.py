def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    progress = params['progress']
    

    if(is_left_of_center == True or all_wheels_on_track == True):
        reward = 5.0

    if(distance_from_center < track_width / 2):
        reward += 1.0

    TOTAL_NUM_STEPS = 500

    # Give additional reward if the car pass every 100 steps faster than expected 
    if ((steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100) :
        reward += 10.0

    SPEED_THRESHOLD = 3.0

    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward = 1.55 
    else:
        # High reward if the car stays on track and goes fast
        reward = 2.0



    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 30

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.7

    return float(reward)
