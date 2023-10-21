# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Composition(models.Model):

    _name = "hyd_examen.composition"
    _description = "Composition"

    name = fields.Char(string="Nom")
    code = fields.Char(string='Code')
    is_parent = fields.Boolean(string='Is parent')
    parent_id = fields.Many2one(
        comodel_name='hyd_examen.composition',
        string='Parent', domain=[('is_parent', '=', True)])
    child_ids = fields.One2many(
        comodel_name='hyd_examen.composition',
        inverse_name='parent_id',
        string='Childs',
    )
    anonymous = fields.Boolean(string='Anonymous exam')
