from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s
from collections import defaultdict
from copy import deepcopy

sample = '''\
'''

H0, H1, H2, H3, H4, H5, H6 = 1, 2, 4, 6, 8, 10, 11
HALLWAY_POS = [H0, H1, H2, H3, H4, H5, H6]
A, B, C, D = 3, 5, 7, 9
# ROOM_POS = {'A': A, 'B': B, 'C': C, 'D': D}
EMPTY = '.'

class State():
    energy = defaultdict(int)

    def __init__(self, input):
        input = input.splitlines()
        input.pop(0)
        self.h = [ch for ch in input.pop(0)]
        self.rooms = []
        while True:
            room = [ch for ch in input.pop(0)]
            if all([c in ' #' for c in room]):
                break
            self.rooms.append(room)

    def __str__(self):
        res = []
        res.append('#############')
        res.append(''.join(self.h))
        for room in self.rooms:
            res.append(''.join(room))
        res.append('  #########  ')
        return '\n'.join(res)
    
    def room_is_free(self, name):
        free_count, name_count = 0, 0
        for room in self.rooms:
            if room[get_pos_by_name(name)] == '.':
                free_count += 1
            elif room[get_pos_by_name(name)] == name:
                name_count += 1
        return free_count > 0 and (free_count + name_count == len(self.rooms))

    def room_is_complete(self, name):
        res = True
        for room in self.rooms:
            res = res and room[get_pos_by_name(name)] == name
        return res

    def is_complete(self):
        return self.room_is_complete('A') and self.room_is_complete('B') and self.room_is_complete('C') and self.room_is_complete('D')
    
    def energy_value(self):
        return self.energy['A'] + 10 * self.energy['B'] + 100 * self.energy['C'] + 1000 * self.energy['D']
    
    def try_move_to_room(self):
        def get_free_pos(r_pos):
            res = -1
            for i, r in enumerate(self.rooms):
                if r[r_pos] == '.':
                    res = i
            return res
        res = False
        moved_amphipod = True
        while moved_amphipod:
            for name in ['A', 'B', 'C', 'D']:
                moved_amphipod = False
                if self.room_is_free(name):
                    room_pos = get_pos_by_name(name)
                    dist = 0
                    for d in [-1, 1]:
                        cur_pos = room_pos
                        free_pos = get_free_pos(room_pos)
                        while 0 < cur_pos < len(self.h) - 1:
                            cur_pos += d
                            if cur_pos in HALLWAY_POS:
                                if self.h[cur_pos] == name:
                                    dist += abs(cur_pos - room_pos)
                                    self.h[cur_pos] = '.'
                                    self.rooms[free_pos][room_pos] = name
                                    self.energy[name] += abs(cur_pos - room_pos) + free_pos + 1
                                    moved_amphipod = True
                                if self.h[cur_pos] != '.':
                                    break
                            else:
                                for i, room in enumerate(self.rooms):
                                    if room[cur_pos] == name:
                                        self.rooms[i][cur_pos] = '.'
                                        self.rooms[free_pos][room_pos] = name
                                        self.energy[name] += abs(cur_pos - room_pos) + i + 1 + free_pos + 1
                                        moved_amphipod = True
                                        break
                                    elif room[cur_pos] != '.':
                                        break
                            if moved_amphipod:
                                res = True
                                break
                        if moved_amphipod:
                            break
                    if moved_amphipod:
                        break
        return res

def get_pos_by_name(name):
    return globals()[name]

def copy_state(state):
    res = deepcopy(state)
    res.energy = defaultdict(int)
    for k, v in state.energy.items():
        res.energy[k] = v
    return res

@measure_s
def solve(input):
    res = 1e9
    states = [State(input)]
    while len(states) > 0:
        state = states.pop()
        for name in ['A', 'B', 'C', 'D']:
            if not state.room_is_complete(name):
                pos = get_pos_by_name(name)
                for i, room in enumerate(state.rooms):
                    if room[pos] != '.' and (room[pos] != name or not state.room_is_free(name)):
                        for d in [-1, 1]:
                            cur_pos = pos
                            while True:
                                cur_pos += d
                                if state.h[cur_pos] != '.':
                                    break
                                if cur_pos in HALLWAY_POS:
                                    new_state = copy_state(state)
                                    new_state.h[cur_pos] = state.rooms[i][pos]
                                    new_state.rooms[i][pos] = '.'
                                    new_state.energy[new_state.h[cur_pos]] += i + 1 + abs(cur_pos - pos)
                                    new_state.try_move_to_room()
                                    if new_state.is_complete(): 
                                        if new_state.energy_value() < res:
                                            res = new_state.energy_value()
                                    else:
                                        states.append(new_state)
                        break
    return res

if __name__ == '__main__':
    input = get_input()
    print(solve(input))
    input = input.splitlines()
    input.insert(3, '  #D#C#B#A#  ')
    input.insert(4, '  #D#B#A#C#  ')
    print(solve('\n'.join(input)))