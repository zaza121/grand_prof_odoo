# -*- coding: utf-8 -*-
from odoo import models, fields


class AnneeScolaire(models.Model):

    _name = "hyd_examen.annee_scolaire"
    _description = u"Annee Scolaire"

    name = fields.Char(string="Observation", required=True)
    status = fields.Boolean(string='En cours ?')
    date_debut = fields.Date(string='Date de debut')
    date_fin = fields.Date(string='Date de fin')
