class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.items = []
		self.connections = {}
		self.minigame = None

	def add_item(self, item):
		self.items.append(item)

	def connect_room(self, direction, room):
		self.connections[direction] = room

	def get_description(self):
		return self.description

	def set_minigame(self, func):
		"""Attach a minigame callable to this room.

		The callable can be any function that implements the minigame.
		It will be called by `play_minigame` and any return value forwarded.
		"""
		self.minigame = func

	def play_minigame(self, *args, **kwargs):
		"""Run the attached minigame if present.

		Returns the minigame's return value, or None if no minigame set.
		"""
		if callable(self.minigame):
			return self.minigame(*args, **kwargs)
		return None

def glass_minigame():
	print("You tap the stained glass panes and a hidden melody plays.")
	# return a simple result to show play_minigame returning values
	return "melody_started"	

# Example usage of the Room class and minigame integration
Room1 = Room("Entrance Hall", "A grand hall with a chandelier and marble floors.")
Room2 = Room("Library", "A quiet room filled with shelves of books.")   
Room3 = Room("Dining Room", "A large room with a long dining table and ornate chairs.")
Room1.connect_room("north", Room2)
Room1.connect_room("east", Room3)
GlassRoom = Room("Glass Room", "A room with colorful stained glass windows.")
GlassRoom.set_minigame(glass_minigame)

#test the room descriptions, connections, and minigame

print(Room1.get_description())
print("Connections from Entrance Hall:")
for direction, room in Room1.connections.items():
    print(f"  {direction}: {room.name}")
result = GlassRoom.play_minigame()
print("Glass minigame returned:", result)


