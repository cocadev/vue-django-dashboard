from datetime import datetime
import random


def generate_invoice_uuid(client_id):
    return "INV-" + datetime.now().strftime("%Y%m%d%H%M%S") + random.choice(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ') + str(client_id)


class Units:
    choices = (
        ('Mass', (
            ('kg', 'Kilogram'),
            ('g', 'Gram'),
        )
         ),
        ('Length', (
            ('mm', 'Millimeter'),
            ('m', 'Meter'),
        )
         ),
        ('box', 'Box'),
        ('pallet', 'Pallet'),
        ('unit', 'Unit'),
        ('l', 'Litter'),
    )


class Taxes:
    choices = (
        (0, '0%'),
        (7, '7%'),
        (19, '19%'),
    )


class MAP:
    cities = (
        ('A', 'Aachen'),
        ('HH', 'Hamburg'),
        ('H', 'Hannover')
    )

    countries = (
        ('DE', 'Germany'),
    )


class AddressMetaData:
    types = (
        ('1', 'Invoice & shipping'),
        ('2', 'Invoice'),
        ('3', 'Shipping'),
    )


class InvoiceMetaData:
    states = (
        (1, 'received'),
        (2, 'in-progress'),
        (3, 'delivered'),
        (4, 'canceled'),
        (5, 'returned'),
    )
