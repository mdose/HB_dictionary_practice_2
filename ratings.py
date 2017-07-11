"""Restaurant rating lister."""


def read_restaurant_ratings():
    open_ratings = open("scores.txt")

    restaurant_ratings = {}

    for line in open_ratings:
        line = line.rstrip()
        restaurant, ratings = line.split(":")
        restaurant_ratings[restaurant] = ratings

    #import pdb; pdb.set_trace()

    sorted_restaurants = sorted(restaurant_ratings.items())

    for restaurant, ratings in sorted_restaurants:
        print "{} is rated {}".format(restaurant, ratings)

read_restaurant_ratings()
