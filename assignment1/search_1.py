from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq

def create_open_set():
    return ([], {}) 


def create_closed_set():
    return {}


def add_to_open(vn, open_set):
    priority_queue, states_dict = open_set
    heapq.heappush(priority_queue, vn)
    states_dict[vn.state.state] = vn

def open_not_empty(open_set):
    return bool(open_set[0])


def get_best(open_set):
    priority_queue, states_dict = open_set
    
    while priority_queue:
        best_node = heapq.heappop(priority_queue)
        state_tuple = best_node.state.state
        if state_tuple in states_dict and states_dict[state_tuple] == best_node:
            del states_dict[state_tuple]
            return best_node
            
    return None


def add_to_closed(vn, closed_set):
    closed_set[vn.state.state] = vn.g

#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    _ , states_dict = open_set
    state_tuple = vn.state.state
    
    if state_tuple in states_dict:
        exist_node = states_dict[state_tuple]    
        if vn.g < exist_node.g:
            return False
        else:
            return True
    
    return False


#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    state_tuple = vn.state.state
    
    if state_tuple in closed_set:
        exist_g_cost = closed_set[state_tuple]    
        if vn.g >= exist_g_cost:
            return True
        else:
            del closed_set[state_tuple]
            return False
    
    return False


# helps to debug sometimes..
def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




