inventory = ["Red Paperclip"]
ui = None
e_001ParkingLot = None
e_002FarmersMarket = None
e_002trade = None
e_003ScrapArea = None
e_003trade = None
e_004inorout = None
e_006SeesCandy = None
floor = 1

def map():
	global floor
	if floor == 1:
		print(f"""\nmap1\n""")
	else:
		print(f"""\nmap2\n""")

def intro():
	global ui
	first = input(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n	Welcome to Red Paperclip\n\n A trading game where you use your red paperclip\nto get bigger and better items.\n\nYour in-game commands: "north", "south", "east",\n "west", "grab", "inventory", "map", "trade", and "interact"\n\n				    Have fun!\n\n	/// Press enter to continue. ///\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n""")
	print()
intro()

def encounter_006_SeesCandy():
	ui = None
	global inventory
	global e_006SeesCandy
	if e_006SeesCandy != 1:
		print(f"You enter the See's Candy store and tell your objective to the lady behind the counter.\nShe explains to you that she doesn't have the authority to make a \"trade\" with you.\nShe can offer a free dark chocolate sample though.")
		inventory.append(f"Dark Chocolate Sample")
		print(f"\n+ Dark Chocolate Sample\n")
		e_006SeesCandy = 1
		print(f"You leave the shop.")
		encounter_005()
	else:
		print(f"You approach the See's candy but then remember that you've already recieved a free sample from them.")

def encounter_007():
	print("7")

def encounter_005():
	ui = None
	print(f"To your left you see a See's Candy store.")
	while ui != "north":
		ui = input()
		if ui == "north":
			encounter_007()
		elif ui == "south":
			encounter_004_MallEntrance()
		elif ui == "west":
			encounter_006_SeesCandy()
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		elif ui == "map":
			map()
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")

def encounter_001_ParkingLot():
	ui = None
	global e_001ParkingLot
	if e_001ParkingLot != 1:
		print(f"You close the door of your old sedan and turn towards the Carlsen Mall, in front of it the weekend's farmers' market.\nYou have nothing but a red paperclip.")
	else:
		print(f"\nYou are back at the parking lot next to your car.")
	while ui != "north":
		ui = input()
		if ui == "north":
			e_001ParkingLot = 1
			encounter_002_FarmersMarket()
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		elif ui == "map":
			map()
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")
			print()

def encounter_002_FarmersMarket():
	ui = None
	global e_002FarmersMarket
	global e_004inorout
	e_004inorout = None
	if e_002FarmersMarket != 1:
		print(f"You enter the farmers' market. Around you there are vendors selling fresh fruits, hand-made clothing, and other knick-knacks.")
	while ui != "north":
		ui = input()
		if ui == "north":
			encounter_004_MallEntrance()
		elif ui == "south":
			encounter_001_ParkingLot()
		elif ui == "west":
			encounter_003_ScrapArea()
		elif ui == "trade":
			encounter_002trade()
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		elif ui == "map":
			map()
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")

def encounter_002trade():
	ui = None
	global e_002trade
	global inventory
	if e_002trade != 1:
		print(f"\nYou walk towards a stand selling personilized wooden pens.\nDo you \"trade\" with the vendor?")
	else:
		print(f"You walk towards the wooden pen vendor, but then remeber you've already traded with him.")
		encounter_004_MallEntrance()
	while ui != "trade" or "yes" or "y":
		ui = input()
		if ui == "trade" or "yes" or "y":
			print(f"\nYou explain your quest to the elderly man behind the stand. He looks at you with a confused face then laughs\nsaying \"Sure buddy, I'm sure a paperclip is going to bring you real far. You can have this old pen, it's nearly outta ink anyways.\"\n")
			inventory.remove("Red Paperclip")
			inventory.append("Wooden Pen")
			print(f"+ Wooden Pen\n- Red Paperclip\n")
			e_002trade = 1
			encounter_004_MallEntrance()
		else:
			print(f"\n\"{ui}\" is not valid right now, try typing \"trade\" or \"yes\"")
			print()

def encounter_003_ScrapArea():
	ui = None
	global e_003ScrapArea
	global e_003trade
	global inventory
	if e_003ScrapArea != 1:
		print(f"You head into a fenced-in area by the entrance of the mall. There are industrial dumpsters filled with old boxes and large trash bags.\nYou see an old, destitute man wearing a desert camo baseball cap with a gold-bordered star, his shirt is torn and stained; next to him, a skinny greyhound. ")
		e_003ScrapArea = 1
	else:
		print(f"You walk back into the fenced-in yard, the scruffy veteran with his mangled shirt and hungry dog are still here.")
	while ui != "east":
		ui = input()
		if ui == "trade":
			if e_003trade != 1:
				if "T-Shirt" in inventory:
					print(f"You hand the fellow your spare t-shirt, he gazes at you with a soft bygone love.\n\"Th-thank you.\" he says as he outstretches his hand, you shake it and realize he left within it a silver band.\n")
					inventory.remove("T-Shirt")
					inventory.append("Silver Band")
					print(f"+ Silver Band\n- T-Shirt\n")
					e_003trade = 1
				else:
					print(f"Currently you have nothing to give to the old man.")
			else:
				print(f"Having already traded with the now grinning old man, you have nothing else to give to him.")
		elif ui == "east":
			encounter_002_FarmersMarket()
		elif ui == "interact":
			if "Koi" in inventory:
				print(f"You hand the shimmering koi to the scrawny greyhound. It takes the fish and canters back to its makeshift den.\nFollowing it you find bitten children's toys and tattered shoes, but in the center a large Louis Vittion bag.\n")
				inventory.remove("Koi")
				inventory.append("Louis Vittion Bag")
				print(f"+ Louis Vittion Bag\n- Koi")
			else:
				print(f"Currently you have nothing to give to the greyhound.")
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		elif ui == "map":
			map()
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")

def encounter_004_MallEntrance():
	global e_004inorout
	ui = None
	if e_004inorout != 1:
		print(f"You enter the mall through its automatic double doors and see people busy with their day and shops lively with bussiness.")
		e_004inorout = 1
	else:
		print(f"You walk towards the doors of the mall, facing the exit. You see the farmers' market through the glass doors.")
	while ui != "north":
		ui = input()
		if ui == "north":
			encounter_005()
		elif ui == "south":
			encounter_002_FarmersMarket()
		elif ui == "inventory":
			print(f"\n{inventory}\n")
		elif ui == "map":
			map()
		else:
			print(f"\n\"{ui}\" is either not an option or not valid right now!")

encounter_001_ParkingLot()