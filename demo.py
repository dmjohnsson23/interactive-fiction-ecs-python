from ifecs import *

world = World()

outside = (RoomBuilder(world, 'outside the house', 'outside')
    .add_entity(world.create_entity(
        Reference('mailbox', 'mail box', 'mail', 'box'),
        Container(0, 0),
        Description(
            'There is an open mailbox to the side of the driveway.',
            "It's an ordinary mailbox, probably made of aluminum or tin. It looks like the mailmain was careless and left it open. The box's little red flag is poking up, but there is no mail inside."
        )
    ))
    .entity
)
house = (RoomBuilder(world, 'house')
    .add_passage(outside, Direction.south, ['door', 'front door', 'main door', 'door to the house'])
    .entity
)
player = build_player(world, outside)

world.add_default_systems()

print("Welcome to the demo game!")
Game(world).start()
print('Goodbye!')