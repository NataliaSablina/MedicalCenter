from django.db import models


class Price:
    def __init__(self, price, currency):
        self.price = price
        self.currency = currency

        