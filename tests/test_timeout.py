import pytest


from timeout.timeout import check_venue, check_venues


def test_check_venue_not_suitable_food():
    user = [{
        "name": "Bobby Robson",
        "wont_eat": ["Mexican", "Chinese"],
        "drinks": ["Vokda", "Gin", "whisky", "Rum",
                   "Cider", "Beer", "Soft drinks"],
    }]

    venue = {
        "name": "El Cantina",
        "food": ["Mexican", "Chinese"],
        "drinks": ["Soft drinks", "Tequila", "Beer"],
    }

    expected = ["There is nothing for Bobby to eat"]

    result = check_venue(user, venue)

    assert result == expected


def test_check_venue_suitable_food():
    user = [{
        "name": "Bobby Robson",
        "wont_eat": ["Mexican"],
        "drinks": ["Vokda", "Gin", "whisky",
                   "Rum", "Cider", "Beer", "Soft drinks"],
    }]

    venue = {
        "name": "El Cantina",
        "food": ["Mexican", "Chinese"],
        "drinks": ["Soft drinks", "Tequila", "Beer"],
    }

    expected = []

    result = check_venue(user, venue)

    assert result == expected


def test_check_venue_not_suitable_drinks():
    user = [{
        "name": "Bobby Robson",
        "wont_eat": ["Mexican"],
        "drinks": ["Vokda", "Gin", "whisky", "Rum", "Cider"],
    }]

    venue = {
        "name": "El Cantina",
        "food": ["Mexican", "Chinese"],
        "drinks": ["Soft drinks", "Tequila", "Beer"],
    }

    expected = ["There is nothing for Bobby to drink"]

    result = check_venue(user, venue)

    assert result == expected


def test_check_venues_good_venues():
    users = [{
        "name": "Bobby Robson",
        "wont_eat": ["Mexican"],
        "drinks": ["Vokda", "Beer", "Tea"],
    }]

    venues = [{
        "name": "El Cantina",
        "food": ["Mexican", "Chinese"],
        "drinks": ["Soft drinks", "Tequila", "Beer"],
    },
    {
        "name": "Sultan Sofrasi",
        "food": ["Meat", "Bread", "Fish"],
        "drinks": ["Beer", "Cider", "Soft Drinks"]
    }]

    result = check_venues(users, venues)

    assert "Sultan Sofrasi" in result["good_venues"]
    assert "El Cantina" in result["good_venues"]


def test_check_venues_bad_venues():
    users = [{
        "name": "Bobby Robson",
        "wont_eat": ["Mexican"],
        "drinks": ["Tea"],
    }]

    venues = [{
        "name": "El Cantina",
        "food": ["Mexican"],
        "drinks": ["Soft drinks", "Tequila", "Beer"],
    },
    {
        "name": "Sultan Sofrasi",
        "food": ["Meat", "Bread", "Fish"],
        "drinks": ["Beer", "Cider", "Soft Drinks"]
    }]

    result = check_venues(users, venues)

    assert "Sultan Sofrasi" in result["bad_venues"]
    assert "El Cantina" in result["bad_venues"]
