import pytest


from timeout.timeout import check_venue


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