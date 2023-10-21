# -*- coding: utf-8 -*-
from odoo import models, fields


class Matiere(models.Model):

    _name = "hyd_examen.matiere"
    _description = u"Matiere de l etablissement"

    name = fields.Char(string="Nom", required=True)

    code = fields.Char(string="Code", required=True)

    description = fields.Char(string="Description")
