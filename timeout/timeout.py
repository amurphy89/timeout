
def check_venue(users, venue):

	issues = []

	for user in users:
		name = user["name"].split(" ")[0]
		accpetable_food = [x for x in venue["food"] if x not in user["wont_eat"]]

		if not accpetable_food:
			issues.append(f"There is nothing for {name} to eat")
	
	return issues


