# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.modules.module import get_module_resource
import base64


class Classe(models.Model):

    _name = "hyd_examen.classe"
    _description = "Classe"

    name = fields.Char(string="Nom classe")
    cycle_id = fields.Many2one(
        comodel_name='hyd_examen.cycle',
        string='Cycle'
    )
    cours_ids = fields.Many2many(
        comodel_name="hyd_examen.cours",
        relation="classe_to_cours",
        string='Cours',
    )
