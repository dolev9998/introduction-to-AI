from color_blocks_state import color_blocks_state


pairSet = set()

def init_goal_for_heuristics(goal_blocks):
    global pairSet
    pairSet = set()
    goal_blocks_as_list = [int(x) for x in goal_blocks.split(',')]
    for i in range (len(goal_blocks_as_list) - 1):
        pairSet.add(tuple(sorted((goal_blocks_as_list[i],goal_blocks_as_list[i+1]))))

def base_heuristic(_color_blocks_state: color_blocks_state):
    retVal = 0
    for (a,b) , (c, d) in zip(zip(_color_blocks_state.visible_in_state, _color_blocks_state.visible_in_state[1:]),
                               zip(_color_blocks_state.not_visible_in_state, _color_blocks_state.not_visible_in_state[1:])):
        if not (tuple(sorted((a,c))) in pairSet or tuple(sorted((a,d))) in pairSet or tuple(sorted((b,c))) in pairSet or tuple(sorted((b,d))) in pairSet):
            retVal += 1
    return retVal

def advanced_heuristic(_color_blocks_state):
    return 0

