# -*- coding: utf-8 -*-
from odoo import api, fields, models


class GroupCours(models.Model):

    _name = "hyd_examen.group_cours"
    _description = "Cours"

    name = fields.Char(string="Group de cours")
    sequence = fields.Char(string="Sequence")
    cours_ids = fields.One2many(
        comodel_name='hyd_examen.cours',
        inverse_name='group_id',
        string='Cours',
    )
