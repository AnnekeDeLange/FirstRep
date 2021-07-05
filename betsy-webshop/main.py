__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


import models
import my_helpers
from peewee import fn


# def connect_to_database():
#     models.db.connect()


"""Parts of main are :
1. INIT - fill database with initial content.
2. REQUIRED FUNCTION DEFINITIONS - Functions required for the assignment.
3. CREATE DATABASE TABLES ( + optional fill DaTABASE)
    steps 1 and 2
4. TESTING SCENARIO's - optional scenario for each function)
    steps 3 to 9
   - Testing scenario for each required function, specifying example
     function calls, that can be un-commented to activate."""


# # PART 1 INIT - initialise database and generate some content

def create_some_users_and_add_their_products_to_catalog():
    my_helpers.make_some_user_instances(['Annie', 'Bob', 'Carla',
                                         'David', 'Eleonor', 'Fran'])
    # add products for user1
    add_product_to_catalog(
        1,
        {'name': 'Strawberry jam',
         'unit_price': '2.50',
         'instock': 8,
         'description': "100% pure strawberry jam.",
         'tags': ['preserves', 'jam', 'no sugar',
                  'bioculture', 'food']
         })
    add_product_to_catalog(
        1,
        {'name': 'Blueberry jam',
         'unit_price': '2.40',
         'instock': 6,
         'description': "100% pure orange marmelade.",
         'tags': ['preserves', 'jam', 'no sugar',
                  'bioculture', 'food']
         })
    # add products for user2
    add_product_to_catalog(
        2,
        {'name': 'Stool',
         'unit_price': '30.00',
         'instock': 2,
         'description': "Modern design stool of birch wood.",
         'tags': ['design', 'furniture', 'wood', 'birch']
         })
    add_product_to_catalog(
        2,
        {'name': 'Garden bench',
         'unit_price': '22.50',
         'instock': 3,
         'description': "Robust garden bench of oak.",
         'tags': ['classic', 'furniture', 'wood', 'oak', 'garden']
         })
    # products for user 3
    add_product_to_catalog(
        3,
        {'name': 'Lemon curd',
         'unit_price': '3.40',
         'instock': 7,
         'description': "Creamy lemon curd.",
         'tags': ['preserves', 'curd', 'bioculture', 'food']
         })
    add_product_to_catalog(
        3,
        {'name': 'Mango chutney',
         'unit_price': '2.85',
         'instock': 5,
         'description': "Sweet and spicy mango chutney.",
         'tags': ['preserves', 'chutney', 'bioculture', 'food']
         })
    # products for user 4
    add_product_to_catalog(
        4,
        {'name': 'Sweater',
         'unit_price': '35.00',
         'instock': 4,
         'description': "Pure woolen sweater with Irish pattern.",
         'tags': ['wool', 'natural', 'sweater',
                  'clothing', "sheep"]
         })
    add_product_to_catalog(
        4,
        {'name': 'Cardigan',
         'unit_price': '45.50',
         'instock': 3,
         'description': "Pure angora wool cardigan with wooden buttons.",
         'tags': ['wool', 'natural', 'sweater',
                  'clothing', 'angora goat']
         })
    # products for user 5
    add_product_to_catalog(
        5,
        {'name': 'Closet',
         'unit_price': '25.50',
         'instock': 2,
         'description': "Industrial design closet of wood and metal.",
         'tags': ['furniture', 'office', 'closet',
                  'industrial', 'design']
         })
    # products for user 6
    add_product_to_catalog(
        6,
        {'name': 'Table',
         'unit_price': '52.00',
         'instock': 2,
         'description': "Design office table of plywood.",
         'tags': ['table', 'office', 'furniture', 'plywood']
         })

# # END PART 1 INIT ------------------------------------------------------


# # PART 2 REQUIRED FUNCTIONS DEFINITIONS

def search_product(term):
    '''Case-insensitive search for term in field product.name.'''
    lower_term = term.lower()
    found = (models.Product
             .select()
             .where(
                    (fn.Lower(models.Product.name).contains(lower_term))
                    |
                    (fn.Lower(models.Product.description).contains(lower_term))
                    )
             )
    return found


def list_user_products(user_id):
    """Lists the products of the specified user."""
    up_list = [p for p
               in models.Product
                        .select()
                        .where(models.Product.owner == user_id)]
    return up_list


def list_products_per_tag(tag_id):
    '''Lists all products that are linked to the specified tag.'''
    tp_id_list = [p.product_id for p
                  in (models.ProductTag
                            .select()
                            .where(models.ProductTag.tag_id == tag_id))
                  ]
    tp_list = [models.Product.get(models.Product.id == p) for p in tp_id_list]
    # specify result of this function
    tag_for_list = models.Tag.get_or_none(models.Tag.id == tag_id)
    if tag_for_list is None:
        result = ["This tag does not exist (anymore)."]
    elif tp_list == []:
        result = ["This tag is not linked to a product."]
    else:
        result = tp_list
    return result


# is building block 1 of add_product_to_catalog
def make_new_product(owner_id, product_specs):
    '''Creates new product based on product_specs and links to user.
    A product specification dictionary may look like this:
    {'name': 'stool',
     'unit_price': '25.00',
     'instock': 2,
     'description': "Positive marketing text to boost selling.",
     'tags': ['furniture', 'wood', 'design'] }
    Linking the tags to the product is handled in
    in building block2: add_tags_to_product.
    '''
    new_prod = models.Product.create(name=product_specs['name'],
                                     unit_price=product_specs['unit_price'],
                                     instock=product_specs['instock'],
                                     owner=owner_id,
                                     description=product_specs['description'])
    new_prod.save()
    return new_prod


# is building block2 of add_product_to_catalog
def add_tags_to_product(list_of_tags_to_add, product_id):
    '''Creates tags in the list_of_tags_to_add, if they don't exist yet.
       Subsequently, links each tag to the tags-field of the
       specified product, if it is not yet present.'''
    for t in list_of_tags_to_add:
        new_tag = models.Tag.get_or_create(label=t)
        new_tag[0].save()
        prod_to_update = models.Product.get(models.Product.id == product_id)
        # check if product already has this tag #
        if new_tag[0] not in prod_to_update.tags:
            prod_to_update.tags.add([
                models.Tag.get(models.Tag.label == t)
                ])
    prod_to_update.save()


def add_product_to_catalog(user_id, product):
    '''The specified product is created and linked to the specified user.
    A product specification dictionary may look like this:
    {'name': 'stool',
     'unit_price': '25.00',
     'instock': 2,
     'description': "Positive marketing text to boost selling.",
     'tags': ['furniture', 'wood', 'design'] }
    '''
    new_prod = make_new_product(user_id, product)
    add_tags_to_product(product['tags'], new_prod.id)
    return new_prod


def update_stock(product_id, new_quantity):
    '''Updates the stock quantity of spcified product.'''
    product = models.Product
    qry = product.update(instock=new_quantity).where(product.id == product_id)
    qry.execute()
    updated_product = models.Product.get(models.Product.id == product_id)
    return updated_product


def purchase_product(product_id, buyer_id, quantity):
    """Handles the specified purchase between a buyer and a seller.
       To log the purchase a new transaction is created. """
    product_ordered = models.Product.get_by_id(product_id)
    no_in_stock = product_ordered.instock
    if buyer_id == product_ordered.owner.id:
        print("Owners of a product cannot purchase their own products.")
        ta = None
    elif no_in_stock < quantity:
        print(f"There are only {no_in_stock} items of this product in stock.")
        print("Please change your order, or send an e-mail for a back order.")
        ta = None
    else:
        ta = models.Transaction.create(
                product_ordered=product_id,
                quantity=quantity,
                total_price=(quantity * product_ordered.unit_price),
                buyer=buyer_id)
        new_quantity = no_in_stock - quantity
        update_stock(product_id, new_quantity)
    return ta


def remove_product(product_id):
    '''Deletes the specified product instance.
       Also removes its taglinks in the ProductTag table.'''
    # delete the product instance
    p_to_del = models.Product.get_or_none(models.Product.id == product_id)
    if p_to_del is None:
        result = "This product does not exist (anymore)."
    else:
        p_to_del.delete_instance()
        # and delete all related rows in the ProductTag-table
        taglinks = (models.ProductTag.select()
                    .where(models.ProductTag.product_id == product_id))
        for row in taglinks:
            row.delete().where(models.ProductTag.product_id
                               == product_id).execute()
        result = "The product and it's links to tags are removed."
    return result

# # END PART 2 REQUIRED FUNCTIONS DEFINITIONS ---------------------------


# # PART 3 CREATE DATABASE TABLES and fill database with content

# # STEP 1 - CREATE database tables
models.create_tables()


# # STEP 2 - FILL database with content
# create_some_users_and_add_their_products_to_catalog()

# my_helpers.show_all_users()
# my_helpers.show_all_products()

# # END PART 3 CREATE DATABASE TABLES and fill database with content ------


# # PATRT 4 TEST SCENARIO FOR testing REQUIRED Function for ASSIGNMENT
# # activate function calls Step-by-step as testing script.
# # To activate the calls uncommenting the lines with a single # sign.

# # TEST SCENARIO FOR testing REQUIRED Functions for ASSIGNMENT

# # STEP 3 - test SEARCH function

# # 3.1 check case insensitivity
# searchresult = search_product('design')
# for p in searchresult:
#     print("searchresult is", p.id, p.name)

# # 3.2 check search in description
# searchresult = search_product('metal')
# for p in searchresult:
#     print("searchresult is", p.id, p.name)


# # STEP 4 - test ADD_PRODUCT_TO_CATALOG function
# # SINGLE EXAMPLE CALL - user with id=6 must exist
# add_product_to_catalog(
#     6,
#     {'name': 'Oil painting',
#      'unit_price': '275.00',
#      'instock': 1,
#      'description': "Mountain landscape, oil on canvas.",
#      'tags': ['art', 'painting', 'oil']
#      })
# my_helpers.show_all_products()


# # STEP 5 - test UPDATE_STOCK function
# # format - update_stock(product_id, new_quantity)
# # EXAMPLE CALL - product with id=3 must exist
# my_helpers.show_all_products()
# update_stock(3, 4)
# my_helpers.show_all_products()


# # STEP 6 - test LIST_USER_PRODUCTS
# # EXAMPLE CALL - user with id=3 must exist
# my_helpers.show_all_products()
# up_list = list_user_products(2)
# user_to_show = models.User.get_by_id(2)
# print("User", user_to_show.id, "is", user_to_show.full_name)
# # print to test result
# if up_list == []:
#     print("This user has no products yet.")
# else:
#     for p in up_list:
#         print("Products are:", p.id, p.name)


# # STEP 7 - test LIST_PRODUCTS_PER_TAG
# # EXAMPLE CALL - tag with id=3 exists

# # STEP 7.1 - show all tags
# my_helpers.show_all_tags()

# # STEP 7.2 - EXAMPLE CALL to show products of tag with id=4
# taglist = list_products_per_tag(4)
#  # show result
# tag_to_show = models.Tag.get_by_id(4)
# print("Label of tag with id", tag_to_show.id, "is", tag_to_show.label)
# if taglist == ["This tag does not exist (anymore)."]:
#     print(taglist)
# elif taglist == ["This tag is not linked to a product."]:
#     print(taglist)
# else:
#     for p in taglist:
#         prod = models.Product.get(models.Product.id == p)
#         print("tag is linked to:", prod.id, prod.name)


# # STEP 8 - test REMOVE_PRODUCT
# # EXAMPLE CALL for REMOVE_PRODUCT - product with id=1 must exist
# my_helpers.show_all_products()
# prod_to_remove = models.Product.get_by_id(4)
# result_of_removal = remove_product(4)
# print(result_of_removal)
# print("All products after removal of", prod_to_remove.id,
#       prod_to_remove.name)
# my_helpers.show_all_products()
# print("All products-tag pairs after removal of", prod_to_remove.id,
#       prod_to_remove.name)
# my_helpers.show_ProductTag_rows()


# # STEP 9 - test PURCHASE_PRODUCT
# # EXAMPLE CALL - product with id=5 and buyer_id with id=4 must exist
# #  format - purchase_product(product_id, buyer_id, quantity)

# # STEP 9.1 pruchase of a product by the owner is prevented
# transaction = purchase_product(5, 3, 2)
# if transaction is not None:
#     print("transaction", transaction.date, transaction.product_ordered.name,
#           "in stock now", transaction.product_ordered.instock,
#           "owner of product", transaction.product_ordered.owner.full_name,
#           transaction.total_price,
#           "buyer", transaction.buyer.full_name)

# # STEP 9.2 purchase quantity that exceeds quantity is instock, is prevented
# transaction = purchase_product(5, 4, 9)
# if transaction is not None:
#     print("transaction", transaction.date, transaction.product_ordered.name,
#           "in stock now", transaction.product_ordered.instock,
#           "owner of product", transaction.product_ordered.owner.full_name,
#           transaction.total_price,
#           "buyer", transaction.buyer.full_name)

# # # STEP 9.3 test of correct purchase and updating of quantity in stock
# transaction = purchase_product(6, 2, 1)
# if transaction is not None:
#     print("The transaction for this purchase:")
#     print("+ transaction", transaction.date)
#     print("+ product ordered:", transaction.product_ordered.name)
#     print("+ number_ordered:", transaction.quantity)
#     print("+ unit_price of product is",
#           transaction.product_ordered.unit_price)
#     print("+ seller is", transaction.product_ordered.owner.full_name)
#     print("+ id of seller is:", transaction.product_ordered.owner.id)
#     print("+ seller's bankaccount is:",
#           transaction.product_ordered.owner.bank_account)
#     print("+ total transaction price is €", transaction.total_price)
#     print("+ buyer", transaction.buyer.full_name)
#     print("+ id of buyer is:", transaction.buyer.id)
#     print("+ left in stock after transaction",
#           transaction.product_ordered.instock)


# # function calls for basic reporting functions
# my_helpers.show_all_products()
# my_helpers.show_all_users()
# my_helpers.show_all_products()
# my_helpers.show_all_tags()
# my_helpers.show_ProductTag_rows()

# # END PATRT 4 TEST SCENARIO FOR testing REQUIRED Function for ASSIGNMENT
