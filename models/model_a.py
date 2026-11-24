# app_tow/models/asset.py
from odoo import models, fields

class MODELA(models.Model):
    _name = "model_a"
    _description = "Asset"


    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price =fields.Float()
    bedroom = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden =fields.Boolean()
    grden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('North','North'),
        ('South','South'),
        ('East','East'),
        ('West','West'),
    ])



    