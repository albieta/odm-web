# -*- coding: utf-8 -*-
{
    'name': "Solar Panels App",
    'summary': "Manage and access of solar panels",
    'author': "Doctor Energy",
    'license': "AGPL-3",
    'website': "https://www.doctorenergy.eu/unase-a-doctor-energy/",
    'version': '15.0.1.0.0',
    'depends': ['base', 'website'],
    'application': True,
    'category': "Services",
    'data': [
        "security/ir.model.access.csv",
	    "views/research_menu.xml",
        "views/proposal.xml",
        "views/keywords.xml",
        "views/categories.xml",
        "views/web/proposal_list.xml",
        "views/web/proposal_web_menu.xml",
        "views/web/proposal_web_template.xml",
        "views/web/proposal_individual.xml",
        "views/web/contact_proposal.xml",
        "views/web/form_contact_proposal.xml",
    ],
    'assets': {
        "web.assets_frontend": {
            "panel_app/static/src/css/research_proposal_web_template.css",
            "panel_app/static/src/js/research_proposal_web_template.js",
        }
    }
}
