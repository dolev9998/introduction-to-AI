from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq

def create_open_set():
    heap = []
    lookup = {}
    return (heap, lookup)


def create_closed_set():
    return {}


def add_to_open(vn, open_set):
    heap, lookup = open_set
    heapq.heappush(heap, vn)
    lookup[vn.state.state] = vn


def open_not_empty(open_set):
    heap, _ = open_set
    if len(heap) > 0:
        return True
    return False


def get_best(open_set):
    heap, lookup = open_set
    
    while len(heap) > 0:
        best_node = heapq.heappop(heap)
        state_key = best_node.state.state
      
        if state_key in lookup and lookup[state_key] == best_node:
            del lookup[state_key]
            return best_node
            
    return None


def add_to_closed(vn, closed_set):
    closed_set[vn.state.state] = vn.g


def duplicate_in_open(vn, open_set):
    _, lookup = open_set
    state_key = vn.state.state
    
    if state_key in lookup:
        existing_node = lookup[state_key]
        
      
        if vn.g < existing_node.g:
            return False
        else:
            return True
            
    return False


def duplicate_in_closed(vn, closed_set):
    state_key = vn.state.state
    
    if state_key in closed_set:
        existing_g = closed_set[state_key]
        
        if vn.g >= existing_g:
            return True
        else:
            del closed_set[state_key]
            return False
            
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.get_state_str())


def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):
        
        current = get_best(open_set)

        if current is None:
            break

        if color_blocks_state.is_goal_state(current.state):
            path = []
            temp = current
            while temp is not None:
                path.append(temp)
                temp = temp.prev
            
            path.reverse()
            return path

        add_to_closed(current, closed_set)
        neighbors = current.get_neighbors()
        for neighbor_state, cost in neighbors:
            
            new_g = current.g + cost
            new_h = heuristic(neighbor_state)
            neighbor_node = search_node(neighbor_state, new_g, new_h, current)
            in_open = duplicate_in_open(neighbor_node, open_set)
            in_closed = duplicate_in_closed(neighbor_node, closed_set)
            
            if not in_open and not in_closed:
                add_to_open(neighbor_node, open_set)

    return None