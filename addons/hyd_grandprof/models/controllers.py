# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.website_form.controllers.main import WebsiteForm
import logging
import json


class Academy(http.Controller):

    @http.route("/academy/academy/", auth='public', website=True)
    def index(self, **kw):
        petites_obj = http.request.env["tuto_odoo.petites"]
        return http.request.render(
            'tuto_odoo.index', {'exs': petites_obj.search([])})

    @http.route("/academy/<model('tuto_odoo.petites'):petite>/",
                auth="public", website=True)
    def petite(self, petite):
        return http.request.render(
            'tuto_odoo.details', {'choosed': petite})

    @http.route("/academy/new_petite/",
                auth="public", website=True)
    def new_petite(self):
        return http.request.render(
            'tuto_odoo.nouveau', {})

    @http.route("/colis/paris", auth='public', website=True)
    def index_colis(self, **kw):
        petites_obj = http.request.env["tuto_odoo.petites"]
        return http.request.render(
            'tuto_odoo.index_colis', {'exs': petites_obj.search([])})


class PetitesForm(WebsiteForm):

    # Check and insert values from the form on the model <model>
    @http.route('/petites_form/<string:model_name>',
                type='http', auth="public", methods=['POST'], website=True)
    def petites_form(self, model_name, **kwargs):

        _logger = logging.getLogger(__name__)
        params = http.request.params

        print ("************* %s ===============" % params)
        _logger.info("************* %s ===============" % str(params))
        if model_name == 'tuto_odoo.petites':
            # geoip_country_code = request.session.get('geoip', {}).get('country_code')
            # geoip_state_code = request.session.get('geoip', {}).get('region')
            # if geoip_country_code and geoip_state_code:
            #     State = request.env['res.country.state']
            #     request.params['state_id'] = State.search([('code', '=', geoip_state_code), ('country_id.code', '=', geoip_country_code)]).id
            print ("************* %s ===============" % model_name)
        id_record = http.request.env['tuto_odoo.petites'].sudo().create(
            {'nom': params['nom'], 'details': params['details']})
        return json.dumps({'id': id_record.id})
        # return http.request.redirect('/academy/academy/')
        # return super(WebsiteForm, self).website_form(model_name, **kwargs)


# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
