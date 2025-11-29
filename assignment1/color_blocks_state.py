GOAL_VISIBLE = []

def init_goal_for_search(goal_blocks):
    global GOAL_VISIBLE
    GOAL_VISIBLE = []
    
    if goal_blocks:
        split_values = goal_blocks.split(',')
        for val in split_values:
            GOAL_VISIBLE.append(int(val))

class color_blocks_state:

    def __init__(self, blocks_data, is_parsed=False):
        if is_parsed:
            self.state = blocks_data
        else:

            clean_str = blocks_data.replace('(', '').replace(')', '')
            
            if len(clean_str) == 0:
                self.state = ()
            else:
                str_parts = clean_str.split(',')
                nums = []
                for s in str_parts:
                    nums.append(int(s))
                
                pairs = []
                for i in range(0, len(nums), 2):
                    visible = nums[i]
                    hidden = nums[i+1]
                    pairs.append((visible, hidden))
                
                self.state = tuple(pairs)

    @staticmethod
    def is_goal_state(_state):
        current_blocks = _state.state
        
        if len(current_blocks) != len(GOAL_VISIBLE):
            return False
            
        for i in range(len(current_blocks)):
            if current_blocks[i][0] != GOAL_VISIBLE[i]:
                return False
                
        return True

    def get_neighbors(self):
        neighbors_list = []
        current_tuple = self.state
        n = len(current_tuple)
        # convert to list so we can modify it temporarily
        temp_list = list(current_tuple)

        for i in range(n):
            original_block = temp_list[i]
            v = original_block[0]
            h = original_block[1]
            flipped_block = (h, v)
            
            temp_list[i] = flipped_block

            new_state = color_blocks_state(tuple(temp_list), is_parsed=True)
            neighbors_list.append((new_state, 1))

            temp_list[i] = original_block


        for i in range(n - 1):

            top_part = current_tuple[:i]

            bottom_part = current_tuple[i:]
            
            reversed_bottom = bottom_part[::-1]
            new_tuple = top_part + reversed_bottom
            
            new_state = color_blocks_state(new_tuple, is_parsed=True)
            neighbors_list.append((new_state, 1))

        return neighbors_list

    def get_state_str(self):
        return str(self.state)

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state == other.state