from strip import Strip
import socket

# ip addresses
ip_office =     '192.168.0.19' # V
ip_hallway =    '192.168.0.16' # IV
ip_livingroom = '192.168.0.18' # III
ip_bedroom =    '192.168.0.13' # II
# unused:       '192.168.0.15' # I

# map strip to room & zone
# TODO verify addresses and indices
strips = dict()
# Office
strips['o1'] = Strip(ip_office    , 0, 100)
strips['o2'] = Strip(ip_office    , 1, 100)
strips['o3'] = Strip(ip_office    , 2, 100)
# Hallway
strips['h1'] = Strip(ip_hallway   , 0, 100)
# Living Room
strips['l1'] = Strip(ip_livingroom, 0, 100)
strips['l2'] = Strip(ip_livingroom, 1, 100)
strips['l3'] = Strip(ip_livingroom, 2, 100)
# Bedroom
strips['b1'] = Strip(ip_bedroom   , 0, 100)
#strips['b2'] = Strip(ip_bedroom   , 1, 100)