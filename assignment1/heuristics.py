from color_blocks_state import color_blocks_state

# you can add helper functions and params
pairSet = set()

def init_goal_for_heuristics(goal_blocks):
    pairSet = set()
    goal_blocks_as_list = [x for x in goal_blocks.split(',')]
    for i in range (len(goal_blocks_as_list) - 1):
        pairSet.add(tuple(sorted((goal_blocks_as_list[i],goal_blocks_as_list[i+1]))))

def base_heuristic(_color_blocks_state):
    retVal = 0
    pairs = [x for x in _color_blocks_state.split(',')]
    for pair in s.split("),"):
        pair = pair.strip("()")
        a,b = pair.split(",")
        pairs.append(int(a),int(b))
    for (a,b) , (c, d) in zip(pairs, pairs[1:]):
        if not (tuple(sorted(a,c)) in pairSet or tuple(sorted(a,d)) in pairSet or tuple(sorted(b,c)) in pairSet or tuple(sorted(b,d)) in pairSet):
            retVal += 1
    return retVal

def advanced_heuristic(_color_blocks_state):
    return 0

