# -*- coding: utf-8 -*-
import numpy as np


class zone:
    def __init__(self, name, orbs, hub, cell_min=0, cell_req=[], visited=False):
        self.name = name
        self.orbs = orbs
        self.hub = hub
        self.cell_min = cell_min
        self.visited = visited
        self.cell_req = cell_req

class power_cell:
    def __init__(self, name, zone, orbs_req=0, cell_min=0, prev_cell=[]):
        self.name = name
        self.zone = zone
        self.orbs_req = orbs_req
        self.cell_min = cell_min
        self.prev_cell = prev_cell

def check_clear(cell_list, req_cells=[], area_name=''):
    if area_name != '':
        for cell in cell_list:
            if cell.zone.name == area_name:
                return False
    for r in req_cells:
        for cell in cell_list:
            if cell.name == r:
                return False
    return True

def find_zind(cell, zone_list):
    for i in range(len(zone_list)):
        if zone_list[i].name == cell.zone.name:
            return i

def find_min_cells():
    while True:
        uinp = input('Skip secret ending? [y/n]: ')
        if uinp == 'y':
            break
        elif uinp == 'n':
            return 101
        else:
            print('Pick either \'y\' or \'n\', please')

    while True:
        uinp = input('Skip Lava Tube? [y/n]: ')
        if uinp == 'y':
            break
        elif uinp == 'n':
            return 72
        else:
            print('Pick either \'y\' or \'n\', please')

    while True:
        uinp = input('Skip Rock Village boulder? [y/n]: ')
        if uinp == 'y':
            break
        elif uinp == 'n':
            return 45
        else:
            print('Pick either \'y\' or \'n\', please')

    while True:
        uinp = input('Skip Fire Canyon? [y/n]: ')
        if uinp == 'y':
            return 4
        elif uinp == 'n':
            return 20
        else:
            print('Pick either \'y\' or \'n\', please')

def main():
    gr = zone(name='Geyser Rock', orbs=50, hub=0)
    sv = zone(name='Sandover Village', orbs=50, hub=1)
    sb = zone(name='Sentinal Beach', orbs=150, hub=1)
    fj = zone(name='Forbidden Jungle', orbs=150, hub=1)
    mi = zone(name='Misty Island', orbs=150, hub=1, cell_req=['Catch 200 pounds of fish'])
    fc = zone(name='Fire Canyon', orbs=50, hub=1, cell_min=20)
    rv = zone(name='Rock Village', orbs=50, hub=2)
    pb = zone(name='Precursor Basin', orbs=200, hub=2)
    lpc = zone(name='Lost Precursor City', orbs=200, hub=2)
    bs = zone(name='Boggy Swamp', orbs=200, hub=2)
    mp = zone(name='Mountain Pass', orbs=50, hub=2, cell_min=45)
    vc = zone(name='Volcanic Crater', orbs=50, hub=3)
    sm = zone(name='Snowy Mountain', orbs=200, hub=3)
    sc = zone(name='Spider Cave', orbs=200, hub=3)
    lt = zone(name='Lava Tube', orbs=50, hub=3, cell_min=72)
    gmc = zone(name='Gol and Maia\'s Citadel', orbs=200, hub=4)

    all_zones = [gr, sv, sb, fj, mi, fc, rv, pb, lpc, bs, mp, vc, sm, sc, lt, gmc]

    casual_cells = [
        power_cell(name='Find the cell on the path', zone=gr),
        power_cell(name='Open the precursor door', zone=gr),
        power_cell(name='Climb up the cliff', zone=gr, prev_cell=['Open the precursor door']),
        power_cell(name='Free the 7 scout flies', zone=gr),

        power_cell(name='Bring 90 orbs to the mayor', zone=sv, orbs_req=90),
        power_cell(name='Bring 90 orbs to your uncle', zone=sv, orbs_req=90),
        power_cell(name='Herd the yakows into the pen', zone=sv),
        power_cell(name='Bring 120 orbs to the oracle', zone=sv, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=sv, orbs_req=120),
        power_cell(name='Free the 7 scout flies', zone=sv),

        power_cell(name='Unblock the eco harvesters', zone=sb),
        power_cell(name='Push the flut flut egg off the cliff', zone=sb),
        power_cell(name='Get the power cell from the pelican', zone=sb),
        power_cell(name='Chase the seagulls', zone=sb),
        power_cell(name='Launch up to the cannon tower', zone=sb, prev_cell=['Find the blue vent switch']),
        power_cell(name='Explore the beach', zone=sb),
        power_cell(name='Climb the sentinel', zone=sb),
        power_cell(name='Free the 7 scout flies', zone=sb),

        power_cell(name='Connect the eco beams', zone=fj),
        power_cell(name='Get to the top of the temple', zone=fj),
        power_cell(name='Find the blue vent switch', zone=fj, prev_cell=['Get to the top of the temple']),
        power_cell(name='Defeat the dark eco plant', zone=fj, prev_cell=['Find the blue vent switch']),
        power_cell(name='Catch 200 pounds of fish', zone=fj),
        power_cell(name='Follow the canyon to the sea', zone=fj),
        power_cell(name='Open the locked temple door', zone=fj),
        power_cell(name='Free the 7 scout flies', zone=fj),

        power_cell(name='Catch the sculptor\'s muse', zone=mi),
        power_cell(name='Climb the lurker ship', zone=mi),
        power_cell(name='Stop the cannon', zone=mi),
        power_cell(name='Return to the dark eco pool', zone=mi),
        power_cell(name='Destroy the balloon lurkers', zone=mi),
        power_cell(name='Use the zoomer to reach the power cell', zone=mi),
        power_cell(name='Use the blue eco to reach the power cell', zone=mi),
        power_cell(name='Free the 7 scout flies', zone=mi),

        power_cell(name='Reach the end of Fire Canyon', zone=fc),
        power_cell(name='Free the 7 scout flies', zone=fc),

        power_cell(name='Bring 90 orbs to the gambler', zone=rv, orbs_req=90),
        power_cell(name='Bring 90 orbs to the geologist', zone=rv, orbs_req=90),
        power_cell(name='Bring 90 orbs to the warrior', zone=rv, orbs_req=90),
        power_cell(name='Bring 120 orbs to the oracle', zone=rv, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=rv, orbs_req=120),
        power_cell(name='Free the 7 scout flies', zone=rv),

        power_cell(name='Herd the moles into their hole', zone=pb),
        power_cell(name='Catch the flying lurkers', zone=pb),
        power_cell(name='Beat record time on the gorge', zone=pb),
        power_cell(name='Get the power cell over the lake', zone=pb),
        power_cell(name='Cure the dark eco infected plants', zone=pb),
        power_cell(name='Navigate the precursor rings', zone=pb),
        power_cell(name='Navigate the precursor rings', zone=pb),
        power_cell(name='Free the 7 scout flies', zone=pb),

        power_cell(name='Follow the colored pipes', zone=lpc),
        power_cell(name='Reach the center of the complex', zone=lpc),
        power_cell(name='Match the platform colors', zone=lpc),
        power_cell(name='Quickly cross the dangerous pool', zone=lpc),
        power_cell(name='Raise the chamber', zone=lpc),
        power_cell(name='Reach the bottom of the city', zone=lpc, prev_cell=['Reach the center of the complex']),
        power_cell(name='Climb the slide tube', zone=lpc, prev_cell=['Reach the bottom of the city']),
        power_cell(name='Free the 7 scout flies', zone=lpc),

        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Defeat the lurker ambush', zone=bs),
        power_cell(name='Ride the flut flut', zone=bs, prev_cell=['Push the flut flut egg off the cliff']),
        power_cell(name='Protect Farthy\'s snacks', zone=bs),
        power_cell(name='Free the 7 scout flies', zone=bs),

        power_cell(name='Defeat Klaww', zone=mp),
        power_cell(name='Reach the end of the mountain pass', zone=mp, prev_cell=['Defeat Klaww']),
        power_cell(name='Find the hidden power cell', zone=mp, prev_cell=['Find the yellow vent switch', 'Defeat Klaww']),
        power_cell(name='Free the 7 scout flies', zone=mp, prev_cell=['Defeat Klaww', 'Reach the end of the mountain pass']),

        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 120 orbs to the oracle', zone=vc, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=vc, orbs_req=120),
        power_cell(name='Find the hidden power cell', zone=vc),
        power_cell(name='Free the 7 scout flies', zone=vc),

        power_cell(name='Find the yellow vent switch', zone=sm),
        power_cell(name='Stop the 3 lurker glacier troops', zone=sm),
        power_cell(name='Deactivate the precursor blockers', zone=sm),
        power_cell(name='Open the lurker fort gate', zone=sm, prev_cell=['Push the flut flut egg off the cliff']),
        power_cell(name='Get through the lurker fort', zone=sm, prev_cell=['Open the lurker fort gate']),
        power_cell(name='Survive the lurker infested cave', zone=sm),
        power_cell(name='Open the frozen crate', zone=sm, prev_cell=['Find the yellow vent switch']),
        power_cell(name='Free the 7 scout flies', zone=sm),

        power_cell(name='Use your goggles to shoot the gnawing lurkers', zone=sc),
        power_cell(name='Destroy the dark eco crystals', zone=sc),
        power_cell(name='Explore the dark cave', zone=sc),
        power_cell(name='Climb the giant robot', zone=sc),
        power_cell(name='Launch up to the poles', zone=sc),
        power_cell(name='Navigate through the spider tunnel', zone=sc),
        power_cell(name='Climb the precursor platforms', zone=sc),
        power_cell(name='Free the 7 scout flies', zone=sc),

        power_cell(name='Cross the lava tube', zone=lt),
        power_cell(name='Free the 7 scout flies', zone=lt, prev_cell=['Cross the lava tube']),

        power_cell(name='Free the red eco sage', zone=gmc),
        power_cell(name='Free the yellow eco sage', zone=gmc),
        power_cell(name='Free the blue eco sage', zone=gmc),
        power_cell(name='Free the green eco sage', zone=gmc, prev_cell=['Free the red eco sage', 'Free the yellow eco sage', 'Free the blue eco sage']),
        power_cell(name='Free the 7 scout flies', zone=gmc, prev_cell=['Free the red eco sage', 'Free the yellow eco sage', 'Free the blue eco sage'])
        ]

    sr_cells = [
        power_cell(name='Find the cell on the path', zone=gr),
        power_cell(name='Open the precursor door', zone=gr),
        power_cell(name='Climb up the cliff', zone=gr),
        power_cell(name='Free the 7 scout flies', zone=gr),

        power_cell(name='Bring 90 orbs to the mayor', zone=sv, orbs_req=90),
        power_cell(name='Bring 90 orbs to your uncle', zone=sv, orbs_req=90),
        power_cell(name='Herd the yakows into the pen', zone=sv),
        power_cell(name='Bring 120 orbs to the oracle', zone=sv, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=sv, orbs_req=120),
        power_cell(name='Free the 7 scout flies', zone=sv),

        power_cell(name='Unblock the eco harvesters', zone=sb),
        power_cell(name='Push the flut flut egg off the cliff', zone=sb),
        power_cell(name='Get the power cell from the pelican', zone=sb),
        power_cell(name='Chase the seagulls', zone=sb),
        power_cell(name='Launch up to the cannon tower', zone=sb),
        power_cell(name='Explore the beach', zone=sb),
        power_cell(name='Climb the sentinel', zone=sb),
        power_cell(name='Free the 7 scout flies', zone=sb),

        power_cell(name='Connect the eco beams', zone=fj),
        power_cell(name='Get to the top of the temple', zone=fj),
        power_cell(name='Find the blue vent switch', zone=fj, prev_cell=['Get to the top of the temple']),
        power_cell(name='Defeat the dark eco plant', zone=fj, prev_cell=['Find the blue vent switch']),
        power_cell(name='Catch 200 pounds of fish', zone=fj),
        power_cell(name='Follow the canyon to the sea', zone=fj),
        power_cell(name='Open the locked temple door', zone=fj),
        power_cell(name='Free the 7 scout flies', zone=fj),

        power_cell(name='Catch the sculptor\'s muse', zone=mi),
        power_cell(name='Climb the lurker ship', zone=mi),
        power_cell(name='Stop the cannon', zone=mi),
        power_cell(name='Return to the dark eco pool', zone=mi),
        power_cell(name='Destroy the balloon lurkers', zone=mi),
        power_cell(name='Use the zoomer to reach the power cell', zone=mi),
        power_cell(name='Use the blue eco to reach the power cell', zone=mi),
        power_cell(name='Free the 7 scout flies', zone=mi),

        power_cell(name='Reach the end of Fire Canyon', zone=fc),
        power_cell(name='Free the 7 scout flies', zone=fc),

        power_cell(name='Bring 90 orbs to the gambler', zone=rv, orbs_req=90),
        power_cell(name='Bring 90 orbs to the geologist', zone=rv, orbs_req=90),
        power_cell(name='Bring 90 orbs to the warrior', zone=rv, orbs_req=90),
        power_cell(name='Bring 120 orbs to the oracle', zone=rv, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=rv, orbs_req=120),
        power_cell(name='Free the 7 scout flies', zone=rv),

        power_cell(name='Herd the moles into their hole', zone=pb),
        power_cell(name='Catch the flying lurkers', zone=pb),
        power_cell(name='Beat record time on the gorge', zone=pb),
        power_cell(name='Get the power cell over the lake', zone=pb),
        power_cell(name='Cure the dark eco infected plants', zone=pb),
        power_cell(name='Navigate the precursor rings', zone=pb),
        power_cell(name='Navigate the precursor rings', zone=pb),
        power_cell(name='Free the 7 scout flies', zone=pb),

        power_cell(name='Follow the colored pipes', zone=lpc),
        power_cell(name='Reach the center of the complex', zone=lpc),
        power_cell(name='Match the platform colors', zone=lpc),
        power_cell(name='Quickly cross the dangerous pool', zone=lpc),
        power_cell(name='Raise the chamber', zone=lpc),
        power_cell(name='Reach the bottom of the city', zone=lpc, prev_cell=['Reach the center of the complex']),
        power_cell(name='Climb the slide tube', zone=lpc, prev_cell=['Reach the bottom of the city']),
        power_cell(name='Free the 7 scout flies', zone=lpc),

        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Break a tether to the zeppelin', zone=bs),
        power_cell(name='Defeat the lurker ambush', zone=bs),
        power_cell(name='Ride the flut flut', zone=bs),
        power_cell(name='Protect Farthy\'s snacks', zone=bs),
        power_cell(name='Free the 7 scout flies', zone=bs),

        power_cell(name='Defeat Klaww', zone=mp),
        power_cell(name='Reach the end of the mountain pass', zone=mp),
        power_cell(name='Find the hidden power cell', zone=mp),
        power_cell(name='Free the 7 scout flies', zone=mp),

        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 90 orbs to the miners', zone=vc, orbs_req=90),
        power_cell(name='Bring 120 orbs to the oracle', zone=vc, orbs_req=120),
        power_cell(name='Bring 120 orbs to the oracle', zone=vc, orbs_req=120),
        power_cell(name='Find the hidden power cell', zone=vc),
        power_cell(name='Free the 7 scout flies', zone=vc),

        power_cell(name='Find the yellow vent switch', zone=sm),
        power_cell(name='Stop the 3 lurker glacier troops', zone=sm),
        power_cell(name='Deactivate the precursor blockers', zone=sm),
        power_cell(name='Open the lurker fort gate', zone=sm),
        power_cell(name='Get through the lurker fort', zone=sm, prev_cell=['Open the lurker fort gate']),
        power_cell(name='Survive the lurker infested cave', zone=sm),
        power_cell(name='Open the frozen crate', zone=sm, prev_cell=['Push the flut flut egg off the cliff']),
        power_cell(name='Free the 7 scout flies', zone=sm),

        power_cell(name='Use your goggles to shoot the gnawing lurkers', zone=sc),
        power_cell(name='Destroy the dark eco crystals', zone=sc),
        power_cell(name='Explore the dark cave', zone=sc),
        power_cell(name='Climb the giant robot', zone=sc),
        power_cell(name='Launch up to the poles', zone=sc),
        power_cell(name='Navigate through the spider tunnel', zone=sc),
        power_cell(name='Climb the precursor platforms', zone=sc),
        power_cell(name='Free the 7 scout flies', zone=sc),

        power_cell(name='Cross the lava tube', zone=lt),
        power_cell(name='Free the 7 scout flies', zone=lt),

        power_cell(name='Free the red eco sage', zone=gmc),
        power_cell(name='Free the yellow eco sage', zone=gmc),
        power_cell(name='Free the blue eco sage', zone=gmc),
        power_cell(name='Free the green eco sage', zone=gmc),
        power_cell(name='Free the 7 scout flies', zone=gmc)
        ]

    while True:
        uinp = input('What type of run? Select \'speedrun\' or \'casual\': ')
        if uinp == 'speedrun':
            run_type = 'speedrun'
            break
        elif uinp == 'casual':
            run_type = 'casual'
            break
        else:
            print('Invalid input! Select again.')

    min_cells = find_min_cells()
    orbs_used = 0
    cum_orbs = 0  # hehe
    if run_type == 'speedrun':
        rem_cells = sr_cells.copy()
    elif run_type == 'casual':
        rem_cells = casual_cells.copy()
    rem_cell_names = []
    for i in range(len(rem_cells)):
        rem_cell_names.append(rem_cells[i].name)

    rng = np.random.default_rng()
    hub_access = 0

    for n in range(min_cells):

        # Randomly Pick a cell
        while True:
            nc = rng.integers(len(rem_cells))
            next_cell = rem_cells[nc]
            zind = find_zind(next_cell, all_zones)

            # Check if the next cell is in a new area
            add_orbs = False
            if not all_zones[zind].visited:
                add_orbs = True

            # Perform logic checks
            if next_cell.zone.hub <= hub_access:
                if next_cell.zone.cell_min <= n:
                    if check_clear(rem_cells, req_cells=next_cell.zone.cell_req):
                        if check_clear(rem_cells, req_cells=next_cell.prev_cell):
                            if orbs_used+next_cell.orbs_req <= cum_orbs+(add_orbs*all_zones[zind].orbs):
                                break  # Stop selecting cells if all current logic conditions are met

        # Update orb count
        orbs_used += next_cell.orbs_req
        if not all_zones[zind].visited:
            all_zones[zind].visited = True
            cum_orbs += all_zones[zind].orbs

        # Output to user
        print('{:}:  {:} in {:}\n'.format(n+1, next_cell.name, next_cell.zone.name))

        # Update list
        rem_cells.pop(nc)
        rem_cell_names.pop(nc)

        # Update hub access level
        gr_clear_flag = check_clear(rem_cells, area_name=gr.name)
        fc_clear_flag = check_clear(rem_cells, req_cells=['Reach the end of Fire Canyon'])
        mp_clear_flag = check_clear(rem_cells, req_cells=['Reach the end of the mountain pass'])
        lt_clear_flag = check_clear(rem_cells, req_cells=['Cross the lava tube'])
        if gr_clear_flag:
            hub_access = 1
        if fc_clear_flag:
            hub_access = 2
        if mp_clear_flag:
            hub_access = 3
        if lt_clear_flag:
            hub_access = 4

if __name__ == '__main__':
    main()
