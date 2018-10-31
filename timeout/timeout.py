

def check_venues(users, venues):

    good_venues = []
    bad_venues = {}

    for venue in venues:
        issues = check_venue(users, venue)
        if issues:
            bad_venues.update({
                venue["name"]: issues
            })
        else:
            good_venues.append(venue["name"])

    return {
        "good_venues": good_venues,
        "bad_venues": bad_venues,
    }


def check_venue(users, venue):

    issues = []

    for user in users:
        name = user["name"].split(" ")[0]
        accpetable_food = set(venue["food"]) - set(user["wont_eat"])

        if not accpetable_food:
            issues.append(f"There is nothing for {name} to eat")

        accpetable_drinks = set(user["drinks"]) & set(venue["drinks"])

        if not accpetable_drinks:
            issues.append(f"There is nothing for {name} to drink")

    return issues
