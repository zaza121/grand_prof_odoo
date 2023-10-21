# -*- coding: utf-8 -*-
from odoo import fields, models


class Petites(models.Model):

    _name = "tuto_odoo.petites"

    nom = fields.Char(string="Nom de la petite")

    details = fields.Html()


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    petite_id = fields.Many2one('tuto_odoo.petites', string="Petite")
