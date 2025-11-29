from color_blocks_state import color_blocks_state


allowed_pairs_dict = {} 
goal_bottom_val = None

def init_goal_for_heuristics(goal_blocks):
    global allowed_pairs_dict, goal_bottom_val
    
    allowed_pairs_dict = {}
    goal_bottom_val = None

    if goal_blocks is None or len(goal_blocks) == 0:
        return

    temp_list = goal_blocks.split(',')
    goal_ints = []
    for x in temp_list:
        goal_ints.append(int(x))
        
    if len(goal_ints) > 0:
        goal_bottom_val = goal_ints[-1]

    for i in range(len(goal_ints) - 1):
        color1 = goal_ints[i]
        color2 = goal_ints[i+1]
        
        if color1 not in allowed_pairs_dict:
            allowed_pairs_dict[color1] = set()
        allowed_pairs_dict[color1].add(color2)
        
        if color2 not in allowed_pairs_dict:
            allowed_pairs_dict[color2] = set()
        allowed_pairs_dict[color2].add(color1)


def base_heuristic(_state):
    total_penalty = 0
    current_state = _state.state
    
    for i in range(len(current_state) - 1):
        
        block_top = current_state[i]
        block_bottom = current_state[i+1]
        
        top_vis = block_top[0]
        top_hid = block_top[1]
        
        bot_vis = block_bottom[0]
        bot_hid = block_bottom[1]
        
        is_valid_pair = False
        if top_vis in allowed_pairs_dict:
            valid_neighbors = allowed_pairs_dict[top_vis]
            if bot_vis in valid_neighbors:
                is_valid_pair = True
            elif bot_hid in valid_neighbors:
                is_valid_pair = True
                
        if is_valid_pair == False:
            if top_hid in allowed_pairs_dict:
                valid_neighbors = allowed_pairs_dict[top_hid]
                if bot_vis in valid_neighbors:
                    is_valid_pair = True
                elif bot_hid in valid_neighbors:
                    is_valid_pair = True
        
        if is_valid_pair == False:
            total_penalty = total_penalty + 1
            
    return total_penalty


def advanced_heuristic(_state):
    h_value = base_heuristic(_state)

    current_tower = _state.state
    
    bottom_block = current_tower[-1]
    bottom_visible = bottom_block[0]
    
    if bottom_visible != goal_bottom_val:
        h_value = h_value + 1

    return h_value