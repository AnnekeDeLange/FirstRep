
import models
# from models import Dish
# from models import Restaurant
from models import Rating
# from models import Ingredient
# from models import DishIngredient
import peewee
from peewee import fn
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"

'''
# help function to show all restaurants
def show_restaurants():
    all_rests = (models.Restaurant.select())
    print("Totaal aantal restauranten: ", len(all_rests))
    for r in all_rests:
        print("Restaurant names are", r.name)


def show_all_ratings():
    all_rests = (models.Restaurant
                 .select())
    print("--- There are ", len(all_rests), "restaurants now.")
    for r in all_rests:
        print("<rest-id>", r.id, r.name, r.open_since)
    for rest in all_rests:
        ratq = (models.Rating
                .select()
                .where(models.Rating.restaurant == rest)
                )
        # print(ratq)       # what does ratq-query look like
        print("---", rest.name, "has", len(ratq), "ratings.")
        print("--- Ratings for", rest.name, "[<rest-id", rest.id, ">] are:")
        for rat in ratq:
            print(rat.restaurant.name,
                  "rating=", rat.rating,
                  rat.comment,
                  "[<rating-id:", rat.id, ">]")


def show_all_ratings_for_specific_restaurant(rest_name):
    # show_restaurants()
    # for one restaurant with specific name
    eett = (models.Restaurant
            .select()
            .where(models.Restaurant.name == rest_name)
            )
    ratq = (models.Rating
            .select()
            .where(models.Rating.restaurant == eett)
            )
    for rat in ratq:
        print(rat.restaurant.name,
              "rating=", rat.rating,
              rat.comment,
              "[<rating-id:", rat.id, ">]")


# help function to instantiate restaurants
# create_restaurant("<name>", "YYYY-MM-DD", "HH:MM", "HH:MM")
def create_restaurant(resname, opendate, opentime, closetime):
    models.Restaurant.create(name=resname,
                             open_since=opendate,
                             opening_time=opentime,
                             closing_time=closetime)


# add_rating_to_rest('<restaurant_name>", <new_rating>, "comment")
def add_rating_to_rest(restaurant_name, new_rating, new_comment):
    res = models.Restaurant
    res_to_rate = res.get(res.name == restaurant_name)
    models.Rating.create(restaurant=res_to_rate,
                         rating=new_rating,
                         comment=new_comment)


# help function to delete instance of restaurant
# delete_restaurant("<name>")
def delete_restaurant_by_name(resname):
    print("Before delete : ", show_restaurants())
    all_rests = (models.Restaurant.select())
    print("Totaal aantal restauranten: ", len(all_rests))
    for r in all_rests:
        print("Restaurant name", r.name)
    rest = models.Restaurant
    obj = rest.get(rest.name == resname)
    obj.delete_instance()


# delete_restaurant("<name>")
def delete_restaurant_by_id(restaurant_id):
    r_to_del = (models.Restaurant
                .select()
                .where(models.Restaurant.id == restaurant_id)
                )
    if r_to_del.exists():
        for r in r_to_del:
            r.delete_instance()
            print("restaurant instance deleted")
    else:
        print("no such restaurant instance")


def delete_rating_to_restaurant(rating_id):
    rat = models.Rating
    q = (models.Rating
         .select()
         .where(rat.id == rating_id)
         )
    if q.exists():
        for rating in q:
            rating.delete_instance()
            print("rating deleted")
    else:
        print("no such rating")


# # helper to remove new dishes - indien nodig
# GEEN IDEE OF DEZE WERKT
# dshs_to_rem = (models.Dish
#                .select()
#                .where(models.Dish.name == 'London Poor Mens Omelette')
#                )
# ingr_to_upd = (models.Dish
#                .select(models.Dish.ingredients)
#                .where(models.Dish.name == 'London Poor Mens Omelette')
#                )
# # # remove and clear loop
# for d in dshs_to_rem:
#     d.ingredients.remove(d)
#     for i in ingr_to_update:
#         d.ingredients.remove(i)
#     d.ingredients.clear()
# # end remove and clear loop
# # GEEN IDEE OF DEZE WERKT

'''
# DEZE WERKT OOK
# def cheapest_dish2() -> models.Dish:
#     """You want to get food on a budget
#     Query the database to retrieve the cheapest dish available
#     """
#     q = (models.Dish
#          .select(models.Dish.name,
#                  models.Dish.price_in_cents)
#          .order_by(models.Dish.price_in_cents.desc())
#          .limit(1)
#          )
#     return q


# MY VERSION = OK
def cheapest_dish() -> models.Dish:
    """You want to get food on a budget
    Query the database to retrieve the cheapest dish available
    """
    query = (models.Dish
             .select(fn.Min(models.Dish.price_in_cents))
             )
    return query


#  # ORIGINAL
# def vegetarian_dishes() -> List[models.Dish]:
#     pass
#  # END ORIGINAL


#  # MY VERSION
# # this is final version
def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available
    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    veggie_dishes = [dish for dish
                     in models.Dish.select()
                     if all([i.is_vegetarian
                             for i in dish.ingredients])
                     ]
    return veggie_dishes
#  # END MY VERSION


# # MY VERSION = OK
def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    average = (models.Rating
               .select(fn.AVG(models.Rating.rating))
               )
    bst_rst = (models.Restaurant
               .select()
               .join(Rating)
               .order_by(average)
               .limit(1)
               )
    return bst_rst
# # END - MY VERSION


# MY VERSION = OK
def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    # show_restaurants()  # show all restaurants
    rest = (models.Restaurant.select().limit(1))
    # for r in rest:
    #     first_rest_id = r.id
    #     print("1st Restaurants id is", r.id)
    models.Rating.create(restaurant=rest,
                         rating=7,
                         comment='We had a real nice evening!')
# END MY VERSION


# ORIGINAL
# def dinner_date_possible() -> List[models.Restaurant]:
#     """You have asked someone out on a dinner date, but where to go?

#     You want to eat at around 19:00 and your date is vegan.
#     Query a list of restaurants that account for these constraints.
#     """
#     pass
# END ORIGINAL

#  # MY VERSION
def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    # vegan_ingrs = (models.Ingredient
    #                .select()
    #                .where(models.Ingredient.is_vegan == 1)
    #                )
    # vegan_dishes = [dish for dish
    #                 in models.Dish.select()
    #                 if all([i.is_vegen
    #                         for i in dish.ingredients])]
    rests = [rest for rest in models.Restaurant
             .select()
             .where((models.Restaurant.opening_time.hour <= 19)
                    & (models.Restaurant.opening_time.minute <= 00)
                    & (models.Restaurant.closing_time.hour >= 20)
                    & (models.Restaurant.closing_time.minute >= 30)
                    )
             if len([dish for dish
                     in models.Dish
                     .select()
                     .where(models.Dish.served_at == rest.id)
                     if all([i.is_vegan for i in dish.ingredients])
                     ]) > 0
             ]
    return rests
#  # MY VERSION


#  MY VERSION = OK
def add_dish_to_menu() -> models.Dish:
    """Youve created a new dish for your restaurant, that you want
    to add to the menu.
    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    # GET OR CREATE all ingredients needed for Dish
    cheese_key = models.Ingredient.get_or_create(
        name='cheese',
        defaults={'is_vegetarian': True,
                  'is_vegan': False,
                  'is_glutenfree': True})
    cheese_key[0].save()
    # print(cheese_key)
    onion_key = models.Ingredient.get_or_create(
        name='onion',
        defaults={'is_vegetarian': True,
                  'is_vegan': True,
                  'is_glutenfree': True})
    onion_key[0].save()
    # print(onion_key)
    eggs_key = models.Ingredient.get_or_create(
        name='eggs',
        defaults={'is_vegetarian': True,
                  'is_vegan': False,
                  'is_glutenfree': True})
    eggs_key[0].save()
    # print(eggs_key)
    rice_key = models.Ingredient.get_or_create(
        name='rice',
        defaults={'is_vegetarian': True,
                  'is_vegan': True,
                  'is_glutenfree': False})
    rice_key[0].save()
    # print(rice_key)
    shrimps_key = models.Ingredient.get_or_create(
        name='shrimps',
        defaults={'is_vegetarian': False,
                  'is_vegan': False,
                  'is_glutenfree': True})
    shrimps_key[0].save()
    # print(shrimps_key)
    # get a restaurant to serve dish (1st rest is my_rest)
    a_rest = (models.Restaurant .select() .limit(1))
    # CREATE NEW DISH
    new_dish = models.Dish.create(name='London Poor Mens Omelette',
                                  served_at=a_rest,
                                  price_in_cents=300,
                                  )
    new_dish.save()
    # print(new_dish)
    # ADD INGREDIENTS to ManytoMany-TABLE
    new_dish.ingredients.add([
        models.Ingredient.get(models.Ingredient.name == 'cheese'),
        models.Ingredient.get(models.Ingredient.name == 'onion'),
        models.Ingredient.get(models.Ingredient.name == 'eggs'),
        models.Ingredient.get(models.Ingredient.name == 'rice'),
        models.Ingredient.get(models.Ingredient.name == 'shrimps')
        ])
    # ingres = new_dish.ingredients
    # for i in ingres:
    #     print(i.name)
    return new_dish
# END MY VERSION


# ## HELPER FUNCTIONS
# show_restaurants()
# show_all_ratings()
# show_all_ratings_for_specific_restaurant("Zoeloe")
# show_dishes()

# create_restaurant("<name>", "YYYY-MM-DD", "HH:MM", "HH:MM")
# create_restaurant("Zoeloe", "2008-01-22", "11:30", "23:30")
# show_restaurants()

# add_rating_to_rest("Zoeloe", 3, "Not that good")
# add_rating_to_rest("rest_name", None, "comment")
# add_rating_to_rest("Quark", 1, "Not good")

# delete_restaurant_by_name("<name>")
# delete_restaurant("Plok")
# delete_restaurant_by_id(8)

# delete_rating_to_restaurant(<rating_id>)
# rating_id can be found by show_all_ratings
# delete_rating_to_restaurant(20)
# END HELPER FUNCTIONS


"""
# EXERCISE FUNCTIONS ##############
cheapest_dish()
# print(len(dishes))
# for dish in dishes:
#     print(dish.name, dish.price_in_cents)

"""
# add_rating_to_restaurant()

# best_average_rating()
# show_all_ratings()

# vegetarian_dishes()

# add_dish_to_menu()

# dinner_date_possible()
