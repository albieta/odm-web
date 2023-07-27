from odoo import fields, models

class Category(models.Model):
    _name = "research.proposal.keyword.category"
    _description = "Categories"

    name = fields.Char(required=True, translate=True)