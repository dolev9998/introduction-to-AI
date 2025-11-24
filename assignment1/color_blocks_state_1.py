goal_state: list[int]

def init_goal_for_search(goal_blocks):
    global goal_state
    goal_state = []
    goal_blocks_as_list = [x for x in goal_blocks.split(',')]
    for i in range (len(goal_blocks_as_list)):
        goal_state.append(int(goal_blocks_as_list[i]))

class color_blocks_state:
    # you can add global params
    visible_in_state: list[int]
    not_visible_in_state: list[int]
    _hash: int

    def __init__(self, blocks_str, **kwargs):
        self.visible_in_state = list()
        self.not_visible_in_state = list()
        for pair in blocks_str.split("),"):
            pair = pair.strip("()")
            a,b = pair.split(",")
            self.visible_in_state.append(a)
            self.not_visible_in_state.append(b)
        self._hash = hash((tuple(self.visible_in_state),tuple(self.not_visible_in_state)))
        pass

    @staticmethod
    def is_goal_state(_color_blocks_state: "color_blocks_state") :
        return goal_state == _color_blocks_state.visible_in_state
    
    @classmethod
    def _from_states(cls,visible_in_state,not_visible_in_state):
        new_coler_blocks_state = object.__new__(color_blocks_state)
        new_coler_blocks_state.visible_in_state = visible_in_state
        new_coler_blocks_state.not_visible_in_state = not_visible_in_state
        return new_coler_blocks_state
        

    def get_neighbors(self):
        n = len(self.visible_in_state)
        #spin
        for i in range(n):
            yield self._from_states(
                [self.visible_in_state[:i] + [self.not_visible_in_state[i]] + self.visible_in_state[i+1:]],
                [self.not_visible_in_state[:i] + [self.visible_in_state[i]] + self.not_visible_in_state[i+1:]])

        #flip
        for i in range(n):
            for j in range(i + 1, n):
                yield self._from_states(
                    [self.visible_in_state[:i] + self.visible_in_state[i:j+1][::-1] + self.visible_in_state[j+1:]]
                    [self.not_visible_in_state[:i] + self.not_visible_in_state[i:j+1][::-1] + self.not_visible_in_state[j+1:]]
                )

    # for debugging states
    def get_state_str(self):
        return str(self.state)

    def __eq__(self, other):
        return isinstance(other, color_blocks_state) and self.visible_in_state == other.visible_in_state and self.not_visible_in_state == other.not_visible_in_state
    def __hash__(self):
        return self._hash


    #you can add helper functions