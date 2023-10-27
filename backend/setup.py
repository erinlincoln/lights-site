from strip import Strip
from constants import *
import socket

# map strip to room & zone
# TODO verify addresses and indices
strips = dict()
# Office (V)
strips['o1'] = Strip(IP_OFFICE    , 0, 100)
strips['o2'] = Strip(IP_OFFICE    , 1, 100)
strips['o3'] = Strip(IP_OFFICE    , 2, 100)
# Hallway (I)
strips['h1'] = Strip(IP_HALLWAY   , 1, 100)

# Living Room (III)
strips['l1'] = Strip(IP_LIVINGROOM, 0, 100)
strips['l2'] = Strip(IP_LIVINGROOM, 1, 100)
strips['l3'] = Strip(IP_LIVINGROOM, 2, 100)
# Bedroom (II)
strips['b1'] = Strip(IP_BEDROOM   , 1, 100)
strips['b2'] = Strip(IP_BEDROOM   , 2, 100)