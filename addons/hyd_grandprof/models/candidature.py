# -*- coding: utf-8 -*-
from odoo import models, fields


class Candidature(models.Model):

    _name = "hyd_examen.candidature"
    _description = u"candidature"

    name = fields.Char(string="Code", required=True)

    eleve_id = fields.Many2one(
        comodel_name='hyd_examen.eleve',
        string='Eleve',
    )
    salle_id = fields.Many2one(
        comodel_name='hyd_examen.salle',
        string='Salle',
    )
    examen_line_id = fields.Many2one(
        comodel_name='hyd_examen.examen_line',
        string='Examen',
    )
