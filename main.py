ui = None
e_001 = None
def intro():
	global ui
	first = input(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n	Welcome to Red Paperclip\n\n A trading game where you use your red paperclip\nto get bigger and better items.\n\nYour in-game commands: "north", "south", "east",\n "west", "grab", "trade", "interact", "help"\n\n				    Have fun!\n\n	/// Press enter to continue ///\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n""")
	print()
intro()

def encounter_001():
	global ui
	global e_001
	if e_001 != 1:
		ui = input(f"You close the door of your old sedan and turn towards the Carlsen Mall, in front of it the weekend's farmer's market.\nYou have nothing but a red paperclip.\n")
		if ui == "north":
			e_001 = 1
			encounter_002()
		else:
			print(f"\n{ui} is either not an option or not valid right now!")
			print()
			encounter_001()
	else:
		ui = input(f"You are back at the parking lot next to your car.\n")
		if ui == "north":
			encounter_002()
		else:
			print(f"\n{ui} is either not an option or not valid right now!")
			print()
			encounter_001()

def encounter_002():
	global ui
	ui = input(f"You enter the farmer's market.\n")
	if ui == "north":
		encounter_003()
	elif ui == "south":
		encounter_001()
	else:
		print(f"\n{ui} is either not an option or not valid right now!")
		print()
		encounter_002()
def encounter_003():
encounter_001()