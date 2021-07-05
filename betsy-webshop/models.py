# Models go here
import peewee
import datetime
from functools import partial
from peewee import Model
from peewee import CharField
from peewee import TextField
from peewee import DecimalField
from peewee import IntegerField
from peewee import DateField
from peewee import ForeignKeyField
from peewee import ManyToManyField


db = peewee.SqliteDatabase("betsywebshop.db")
# Declare a Moneyfield, being a decimal field suitable for storing currency.
MoneyField = partial(DecimalField, decimal_places=2)


class User(Model):
    full_name = CharField(unique=True)
    street_and_no = CharField()
    postal_code = CharField()
    city = CharField()
    country = CharField()
    bank_account = TextField()

    class Meta:
        database = db
        db_table = 'users'


class Tag(Model):
    label = CharField(unique=True, index=True)

    class Meta:
        database = db
        db_table = 'tags'


class Product(Model):
    name = CharField(index=True)
    unit_price = MoneyField()
    instock = IntegerField()
    owner = ForeignKeyField(User, backref='products')    # one-to-many field
    description = TextField(index=True)
    tags = ManyToManyField(Tag)

    class Meta:
        database = db
        constraints = [peewee.Check('instock >= 0')]
        db_table = 'products'


class Transaction(Model):
    date = DateField(formats='%Y-%m-%d', default=datetime.date.today)
    product_ordered = ForeignKeyField(Product, backref='transaction')
    quantity = IntegerField()
    total_price = MoneyField()
    buyer = ForeignKeyField(User, backref='transaction')

    class Meta:
        database = db
        db_table = 'transactions'


ProductTag = Product.tags.get_through_model()


def create_tables():
    with db:
        db.create_tables([User, Tag, Product, Transaction, ProductTag])


# create_tables()
