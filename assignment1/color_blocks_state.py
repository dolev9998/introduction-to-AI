goal_string = []

def init_goal_for_search(goal_blocks):
    goal_string = []
    goal_blocks_as_list = [x for x in goal_blocks.split(',')]
    for i in range (len(goal_blocks_as_list)):
        goal_string.append(goal_blocks_as_list[i])

class color_blocks_state:
    # you can add global params

    def __init__(self, blocks_str, **kwargs):
        # you can use the init function for several purposes
        pass

    @staticmethod
    def is_goal_state(_color_blocks_state):
        visible_in_state = []
        for pair in _color_blocks_state.split("),"):
            pair = pair.strip("()")
            a, b = pair.split(",")
            visible_in_state.append(a)
        return visible_in_state == goal_string

    def get_neighbors(self):
        pass

        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want
        # def __eq__(self, other):
        # you can change the body of the function if you want

    # for debugging states
    def get_state_str(self):
        return str(self.state)

    def __eq__(self, other):
        pass
    def __hash__(self):
        pass


    #you can add helper functions