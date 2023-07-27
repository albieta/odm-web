from odoo import fields, models

class Keyword(models.Model):
    _name = "research.proposal.keyword"
    _description = "Keywords"

    name = fields.Char(required=True, translate=True)
    category = fields.Many2one("research.proposal.keyword.category", string="Category")
    color = fields.Char( string="Color")