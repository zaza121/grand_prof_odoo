# -*- coding: utf-8 -*-
from odoo import models, fields


class Note(models.Model):

    _name = "hyd_examen.note"
    _description = u"Note"

    name = fields.Char(string="Observation", required=True)
    active = fields.Boolean(string='Active', default=True)
    candidature_id = fields.Many2one(
        comodel_name="hyd_examen.candidature",
        string='Candidature',
    )
    eleve_id = fields.Many2one(
        comodel_name='hyd_examen.eleve',
        string='Eleve',
        related="candidature_id.eleve_id",
        store=True,
    )
    salle_id = fields.Many2one(
        comodel_name='hyd_examen.salle',
        string='Salle',
        related="candidature_id.salle_id",
        store=True,
    )
    examen_line_id = fields.Many2one(
        comodel_name='hyd_examen.examen_line',
        string='Examen par Classe',
        related="candidature_id.examen_line_id",
        store=True,
    )
    examen_id = fields.Many2one(
        comodel_name='hyd_examen.examen',
        string='Examen',
        related="candidature_id.examen_line_id.examen_id",
        store=True,
    )
    code = fields.Char(string="Code", related="candidature_id.name",)
    valeur = fields.Float(string="Note", required=True)
    rang = fields.Integer(string="Rang")
    epreuve_id = fields.Many2one(
        comodel_name='hyd_examen.epreuve',
        string='Epreuve',
    )
