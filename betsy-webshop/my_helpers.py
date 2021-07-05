# HELPER FUNCTIONS for betsy-webshop

import models

"""In my_helpers are the functions definitions and calls for
testing purposes.
1. Helper function definitions
2. Function calls of helper function. Un-comment to activate.
3. Final testing scenario calls are left in main."""


# # 1 FUNCTION definitions of Helper functions -----------------

# USER MAINTENANCE

def make_some_user_instances(userlist):
    no_of_users = len((models.User.select()))
    ins = no_of_users + 1
    new_user_list = []
    for usr in userlist:
        naam = f"{usr} Achternaam{ins}"
        straat_en_no = f"Straatname{ins} {ins}"
        postcode = f"333{ins} BE"
        stad = f"Stad{ins}"
        land = "Netherlands"
        bankrekening = f"NL 12 XXXX 0123 4567 8{ins}"
        models.User.create(full_name=naam,
                           street_and_no=straat_en_no,
                           postal_code=postcode,
                           city=stad,
                           country=land,
                           bank_account=bankrekening)
        ins = ins + 1
    return new_user_list


# #@ show all users
def show_all_users():
    user_list = (models.User.select())
    for u in user_list:
        print('id {} {} aan {} te {} in {} bnk-acc{}'
              .format(u.id,
                      u.full_name,
                      u.street_and_no,
                      u.city,
                      u.country,
                      u.bank_account))


# END USER MAINTENANCE


# PRODUCT MAINTENANCE

def show_all_products():
    """Show all field of all products, with tags and owner."""
    product_list = (models.Product.select())
    for p in product_list:
        print('''id {} {} <"{}"> price € {} .
              In stock {}; owner is {} id {}'''
              .format(p.id,
                      p.name,
                      p.description,
                      p.unit_price,
                      p.instock,
                      p.owner.full_name,
                      p.owner.id))
        tags_of_p = []
        for t in p.tags:
            tags_of_p.append(t.label)
        print("              Tags are: ", tags_of_p)


def show_ProductTag_rows():
    """Shows all rows of the link table ProductTag."""
    tm = (models.ProductTag.select())
    for row in tm:
        print("rownr", row.id, "with content", row.product_id, row.tag_id)


def show_all_tags():
    """Shows all tags that are created, by adding products to the catalog."""
    tags_now = (models.Tag.select())
    for t in tags_now:
        print("tag", t.id, t.label)


# FUNCTIONS FOR TESTING PURPOSES - USED DURING DEVELOPMENT
def create_tag(tag_label):
    """Function for testing purposes only. Creates a single tag."""
    new_tag = models.Tag.get_or_create(label=tag_label)
    new_tag[0].save()


def delete_tag(tag_id):
    """Function for testing purposes only. Deletes a single tag."""
    tag_to_delete = models.Tag.get_or_none(models.Tag.id == tag_id)
    if tag_to_delete is not None:
        tag_to_delete.delete_instance()
    else:
        print("This tag does not exist.")
    # remove row from get_through_table with id of removed tag
    trace = (models.ProductTag.select()
                   .where(models.ProductTag.tag_id == tag_id))
    for row in trace:
        print("rownr", row.id, "with prod", row.product_id,
              "and tag", row.tag_id)
        row.delete().where(models.ProductTag.tag_id == tag_id).execute()


# # OTHER UPDATES of elementary fields e.g. name
def update_field_of_product(product_id, fieldname, new_value):
    product = models.Product
    qry = product.update(fieldname=new_value).where(product.id == product_id)
    qry.execute()

# END 1  FUNCTION definitions of Helper functions -----------------


# # 2 FUNCTION CALLS of Helper functions ---------------------

# # USER MAINTENANCE ---------------

# CALL EXAMPLE to creates some (extra) users
#  make_some_user_instances(['George', 'Harry', 'Iris', 'Jenny']
# #@ show all users
# show_all_users()

#  # END USER MAINTENANCE -----------


# PRODUCT MAINTENANCE ---------------

# #@ show all products with tags and owner
# show_all_products()

# # (create and) add (new) tags to a specific product
# # building block of add_product_to_catalog
# add_tags_to_product(["garden"], 7)

# # update_field_of_product(product_id, fieldname, new_value)
# # building block of add_product_to_catalog
# update_field_of_product(
#     1,
#     'description',
#     "This is the updated content of the description field.")

# END PRODUCT MAINTENANCE ------------


# TAG MAINTENANCE --------------------------

# # create tag
# create_tag('food')

#  # delete_tag
# delete_tag(16)

# show_all_tags()

# END TAG MAINTENANCE ------------------------


# # MAINTENANCE of link table PRODUCTTAG --------------

# remove row from get_through_table with id of removed product
# trace = (models.ProductTag.select().where(models.ProductTag.product_id == 9))
# for row in trace:
#     print("rownr", row.id, "with content", row.product_id, row.tag_id)
#     row.delete().where(models.ProductTag.product_id == 9).execute()

# show_ProductTag_rows()

# # MAINTENANCE of link table PRODUCTTAG ---------------

# # END 2 FUNCTION CALLS of Helper functions ------------------------
