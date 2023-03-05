inventory = ["Red Paperclip"]
ui = None
e_001 = None
e_002 = None
e_002trade = None
def intro():
	global ui
	first = input(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n	Welcome to Red Paperclip\n\n A trading game where you use your red paperclip\nto get bigger and better items.\n\nYour in-game commands: "north", "south", "east",\n "west", "grab", "trade", and "interact"\n\n				    Have fun!\n\n	/// Press enter to continue. ///\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n""")
	print()
intro()

def encounter_001():
	global ui
	global e_001
	if e_001 != 1:
		print(f"You close the door of your old sedan and turn towards the Carlsen Mall, in front of it the weekend's farmer's market.\nYou have nothing but a red paperclip.")
	else:
		print(f"\nYou are back at the parking lot next to your car.")
	while ui != "north":
		ui = input()
		if ui == "north":
			e_001 = 1
			encounter_002()
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")
			print()
			encounter_001()

def encounter_002():
	global ui
	global e_002
	print(f"\nYou enter the farmer's market. Around you there are vendors selling fresh fruits, hand-made clothing, and other knick-knacks.\n")
	while ui != "north" and "south" and "trade":
		ui = input()
		if ui == "north":
			encounter_003()
		elif ui == "south":
			encounter_001()
		elif ui == "trade":
			encounter_002trade()
		elif ui == "inventory":
			print(f"inventory")
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")

def encounter_002trade():
	global ui
	global e_002trade
	global inventory
	if e_002trade != 1:
		ui = input(f"\nYou walk towards a stand selling personilized wooden pens.\nDo you \"trade\" with the vendor?\n")
		if ui == "trade":
				print(f"\nYou explain your quest to the elderly man behind the stand. He looks at you with a confused face then laughs\nsaying \"Sure buddy, I'm sure a paperclip is going to bring you real far. You can have this old pen, it's nearly outta ink anyways.\"\n")
				inventory.remove("Red Paperclip")
				inventory.append("Wooden Pen")
				print(f"+ Wooden Pen\n- Red Paperclip\n")
				e_002trade = 1
				encounter_003()
		else:
			print(f"\n\"{ui}\" is not valid right now, try typing \"trade\"")
			print()
			encounter_002trade()
	else:
		print(f"You walk towards the wooden pen vendor, but then remeber you've already traded with him.")
		encounter_003()

def encounter_003():
	print("3")
encounter_001()