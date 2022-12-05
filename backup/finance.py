from tortoise.models import Model
from tortoise import fields

class Quotes(Model):
    id = fields.IntField(pk=True)
    timestamp = fields.DatetimeField(null=True)
    exchange = fields.CharField(max_length=255, null=True)
    bidPrice = fields.DecimalField(source_field='bid_price', max_digits=10, decimal_places=6, null=True)
    askPrice = fields.DecimalField(source_field='ask_price', max_digits=10, decimal_places=6, null=True)
    lastPrice = fields.DecimalField(source_field='last_price', max_digits=10, decimal_places=6, null=True)

    def __str__(self):
        return self.timestamp