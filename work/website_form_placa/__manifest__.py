# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Online Proposal Submission',
    'category': 'Website/Website',
    'summary': 'Add a research proposal form to your website',
    'version': '1.0',
    'description': """
Generate research proposals from a form published on your website. This module requires the use of the *Form Builder* module (available in Odoo Enterprise) in order to build the form.
    """,
    'depends': ['website', 'panel_app'],
    'data': [
        'data/website_form_proposal_data.xml',
        ],
    'application': True,
    'assets': {
        'website.assets_editor': [
            'website_form_placa/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
}
