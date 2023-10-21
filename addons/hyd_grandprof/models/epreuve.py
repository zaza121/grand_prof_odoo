# -*- coding: utf-8 -*-
from odoo import models, fields


class Epreuve(models.Model):

    _name = "hyd_examen.epreuve"
    _description = u"Epreuve"

    name = fields.Char(string="Label", required=True)
    objectif = fields.Char(string="Objectif")
    classe_id = fields.Many2one(
        comodel_name='hyd_examen.classe',
        string='classe'
    )
    cours_id = fields.Many2one(
        comodel_name='hyd_examen.cours',
        string='cours'
    )
    date_debut = fields.Date(string='Date de debut')
    date_fin = fields.Date(string='Date de fin')
    note_ids = fields.One2many(
        comodel_name="hyd_examen.note",
        inverse_name='epreuve_id',
        string='Notes'
    )
    examen_line_id = fields.Many2one(
        comodel_name='hyd_examen.examen_line',
        string='Examen',
    )
    examen_id = fields.Many2one(
        comodel_name='hyd_examen.examen',
        string='Examen',
        related="examen_line_id.examen_id"
    )
