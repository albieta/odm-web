from odoo import http
from werkzeug.wrappers import Response
import json
import math
import logging
import datetime

_logger = logging.getLogger(__name__)

#if we want to check auth, add --> auth="my_api_key" <-- in the @http.route

class ResearchProposal(http.Controller):

    @http.route("/research/proposal/keywords", methods=["GET"], auth='public')
    def keywords(self, *args, **kwargs):


        Keyword = http.request.env["research.proposal.keyword"]
        keywords = Keyword.search([])

        keyword_names = [keyword.name for keyword in keywords]
        response_data = {
            "keywords": keyword_names
        }
        response_body = json.dumps(response_data)
        return http.Response(response_body, content_type='application/json')

    @http.route("/research/proposal/<int:proposal_id>", methods=["GET"], website=True, auth='public')
    def individual(self, proposal_id, **kwargs):

        proposal = http.request.env['research.proposal'].search([('id', '=', proposal_id)])

        return http.request.render(
            "research_proposal_app.proposal_individual",
            {
                "proposal": proposal,
            }
        )

    @http.route("/contact/proposal/<int:proposal_id>", methods=["GET"], website=True, auth='public')
    def contact(self, proposal_id, **kwargs):

        proposal = http.request.env['research.proposal'].search([('id', '=', proposal_id)])

        return http.request.render(
            "research_proposal_app.contact_proposal",
            {
                "proposal": proposal,
                "has_proposal": bool(proposal),
            }
        )

    @http.route("/research/proposal", methods=["GET"], website=True, auth='public')
    def list(self, *args, **kwargs):

        universities = http.request.env['res.partner'].search([
            ('id', 'in', http.request.env["research.proposal"].search([('validated', '=', True)]).mapped('contact.parent_id.id'))
        ]).read(['comercial', 'name'])

        return http.request.render(
            "research_proposal_app.proposal_web_template",
            {
                "page": 1,
                "universities": universities
            }
        )

    @http.route("/research/proposal/filtered", methods=["POST"], csrf=False, auth='public')
    def filtered(self, *args, **kwargs):

        page = int(kwargs.get('page', 1))
        items_per_page = 10

        current_date = datetime.date.today().strftime('%Y-%m-%d')
        domain = [('expiration_date', '>=', current_date)]
        university = kwargs.get("university")
        keywords_str = kwargs.get("keywords")

        search_query = http.request.params.get('search_query')
        if search_query:
            domain += ['|', ('name', 'ilike', search_query), ('description', 'ilike', search_query)]
        
        if university:
            domain.append(('contact.parent_id.name', '=', university))

        if keywords_str:
            keyword_names = keywords_str.split(',')
            keyword_objs = http.request.env['research.proposal.keyword'].search([('name', 'in', keyword_names)])
            keyword_ids = keyword_objs.ids
            domain.append(('keywords', 'in', keyword_ids))
                
        domain.append(('validated', '=', True))
        proposals = http.request.env['research.proposal'].search(domain, order='expiration_date ASC', limit=items_per_page, offset=(page - 1) * items_per_page)
        total_items = math.ceil(http.request.env['research.proposal'].search_count(domain)/items_per_page)

        return http.request.render(
            "research_proposal_app.proposal_list",
            {
                'proposals': proposals,
                'total_items': total_items,
                'page': page,
                'items_per_page': items_per_page,
            }
        )