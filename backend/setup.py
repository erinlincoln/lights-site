from classes import Zone, Room

# define each zone
l1 = Zone( '192.168.0.15', 2, [100, 100] )
l2 = Zone( '192.168.0.17', 3, [100, 100, 100] )
l3 = Zone( '192.168.0.18', 3, [100, 100, 100] )
l4 = Zone( '192.168.0.16', 2, [100, 100] )
l5 = Zone( '192.168.0.19', 3, [100, 100, 100] )

# define each room
office = Room( 'office', [ l5 ])
# livingRoom = Room( 'livingRoom', [ l1, l3, l4 ])
livingRoom = Room( 'livingRoom', [ l3, l4 ])
bedroom = Room( 'bedroom', [ l2 ])

# setup array of rooms
rooms = [ office, livingRoom ]