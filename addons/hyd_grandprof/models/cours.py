# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Cours(models.Model):

    _name = "hyd_examen.cours"
    _description = "Cours"

    name = fields.Char(string="Nom cours")
    matiere_id = fields.Many2one(
        comodel_name='hyd_examen.matiere',
        string='Matiere'
    )
    classe_id = fields.Many2one(
        comodel_name='hyd_examen.classe',
        string='Classe'
    )
    group_id = fields.Many2one(
        comodel_name='hyd_examen.group_cours',
        string='Group'
    )
    enseignant = fields.Many2one(
        comodel_name='hr.employee',
        string='Enseignant'
    )
    classe_ids = fields.Many2many(
        comodel_name="hyd_examen.classe",
        relation="classe_to_cours",
        string='Classes',
    )
    coef = fields.Integer(string='Coef')
