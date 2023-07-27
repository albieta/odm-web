import logging
from odoo import fields, models, api
from datetime import date, timedelta

_logger = logging.getLogger(__name__)

class researchProposal(models.Model):
    _name = "research.proposal"
    _description = "Proposals"
    name = fields.Char("Title", required=True)
    description = fields.Html(string="Description")
    web_link = fields.Char(string="Url", widget="url")
    expiration_date = fields.Date(string="Expiration Date", default=lambda self: date.today() + timedelta(days=90))
    contact = fields.Many2one("res.partner", string="Contact")
    keywords = fields.Many2many('research.proposal.keyword', string="Keywords")
    validated = fields.Boolean(default=False)