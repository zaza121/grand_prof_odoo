# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Salle(models.Model):

    _name = "hyd_examen.salle"
    _description = "Salle"

    name = fields.Char(string="Nom classe")
    classe_id = fields.Many2one(
        comodel_name='hyd_examen.classe',
        string='classe'
    )
    capacite = fields.Integer(string='Capacité')
    eleves_ids = fields.Many2many(
        comodel_name='hyd_examen.eleve',
        relations="salle_2_eleve",
        string='Eleves',
    )
