__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


import models
import my_helpers
from peewee import fn


# INIT - initialise database and generate some content

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

# END INIT -----------------------------------------------


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


if __name__ == '__main__':

    print("CREATE TABLES - First the database tables are created")
    models.create_tables()
    print("FILL DATABASE - and the database is filled with some content.")
    create_some_users_and_add_their_products_to_catalog()
    print("The users are:")
    my_helpers.show_all_users()
    print("And the products in the database are:")
    my_helpers.show_all_products()

    print("\n")
    print("""SEARCH
          Search on the term 'design' shows products with both
          upper case and lower case in the name """)
    searchresult = search_product('design')
    print("Function call: search_product('design')")
    for p in searchresult:
        print("search result is", p.id, p.name)
    print("""SEARCH
            Searching on 'metal' shows also that search also
            covers the description field.""")
    print("Function call: search_product('metal')")
    searchresult = search_product('metal')
    for p in searchresult:
        print("searchresult is", p.id, p.name)

    print("\n")
    print("""ADD_PRODUCT_TO_CATALOG -
             Add another product to the catalog, for user with id=6.""")
    print("""Function call: add_product_to_catalog(
                6,
                {'name': 'Oil painting',
                'unit_price': '275.00',
                'instock': 1,
                'description': "Mountain landscape, oil on canvas.",
                'tags': ['art', 'painting', 'oil']
                })""")
    add_product_to_catalog(
        6,
        {'name': 'Oil painting',
         'unit_price': '275.00',
         'instock': 1,
         'description': "Mountain landscape, oil on canvas.",
         'tags': ['art', 'painting', 'oil']
         })
    print("Function call: my_helpers.show_all_products()")
    my_helpers.show_all_products()

    print("\n")
    print("""UPDATE STOCK -
             Update the stock of this new product (product_id=11).
             Old quantity was 1, new quantity will be 3.""")
    print("Function call: update_stock(11, 3)")
    update_stock(11, 3)
    print("Function call: my_helpers.show_all_products()")
    my_helpers.show_all_products()

    print("\n")
    print("""LIST_USER_PRODUCTS""")
    print("Function call: list_user_products(6)")
    up_list = list_user_products(6)
    user_to_show = models.User.get_by_id(6)
    print("User", user_to_show.id, "is", user_to_show.full_name)
    # print to test result
    if up_list == []:
        print("This user has no products yet.")
    else:
        for p in up_list:
            print("Products of this user are:", p.id, p.name)

    print("\n")
    print("""LIST_PRODUCTS_PER_TAG""")
    print("First, show all tags in the database at this moment.")
    print("Function call: my_helpers.show_all_tags()")
    my_helpers.show_all_tags()
    print("""And then show the products linked to specified tag.""")
    print("Function call: list_products_per_tag(4)")
    taglist = list_products_per_tag(4)
    tag_to_show = models.Tag.get_by_id(4)
    print("Label of tag with id", tag_to_show.id, "is '",
          tag_to_show.label, "'.")
    if taglist == ["This tag does not exist (anymore)."]:
        print(taglist)
    elif taglist == ["This tag is not linked to a product."]:
        print(taglist)
    else:
        print("List of products the tag is linked to:")
        for p in taglist:
            prod = models.Product.get(models.Product.id == p)
            print("Product", prod.id, prod.name)

    print("\n")
    print("""REMOVE_PRODUCT""")
    print("Function call: remove_product(4)")
    prod_to_remove = models.Product.get_or_none(models.Product.id == 4)
    result_of_removal = remove_product(4)
    print(result_of_removal)
    if prod_to_remove is not None:
        print("All products after removal of", prod_to_remove.id,
              prod_to_remove.name, "are updated.")
        print("Function call: my_helpers.show_all_products()")
        my_helpers.show_all_products()
        print("The list with  products-tag pairs after removal of",
              prod_to_remove.id, prod_to_remove.name, "is also updated.")
        print("Function call: my_helpers.show_ProductTag_rows()")
        print("Pairs in this table are shown as <product.id> <tag,id>.")
        my_helpers.show_ProductTag_rows()

    print("\n")
    print("""PURCHASE_PRODUCT""")
    print("""Function format is:
          purchase_product(product_id, buyer_id, quantity)""")
    print("1. The purchase of product by the owner is prevented:")
    print("Function call: transaction = purchase_product(5, 3, 2)")
    transaction = purchase_product(5, 3, 2)

    print("\n")
    print("""2. Also, a purchase quantity that exceeds the quantity is instock,
             is prevented.""")
    print("Function call: transaction = purchase_product(5, 4, 9)")
    transaction = purchase_product(5, 4, 9)

    print("\n")
    print("""3. Finally, a proper purchase creates
          a new transaction record.""")
    print("Function call: purchase_product(6, 4, 2)")
    transaction = purchase_product(6, 4, 2)
    if transaction is not None:
        print("""The transaction record makes the following information
              about the transaction available:""")
        print("+ transaction id:", transaction.id)
        print("+ transaction date:", transaction.date)
        print("+ product ordered:", transaction.product_ordered.name)
        print("+ quantity (ordered):", transaction.quantity)
        print("+ total transaction price is €", transaction.total_price)
        print("+ unit_price of product is",
              transaction.product_ordered.unit_price)
        print("+ seller is", transaction.product_ordered.owner.full_name)
        print("+ id of seller is:", transaction.product_ordered.owner.id)
        print("+ seller's bankaccount is:",
              transaction.product_ordered.owner.bank_account)
        print("+ buyer", transaction.buyer.full_name)
        print("+ id of buyer is:", transaction.buyer.id)
        print("+ left in stock after transaction",
              transaction.product_ordered.instock)
