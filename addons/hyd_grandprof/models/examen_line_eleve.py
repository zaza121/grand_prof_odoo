# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.modules.module import get_module_resource
import base64


class Cycle(models.Model):

    _name = "hyd_examen.cycle"
    _description = "Cyle scolaire"

    name = fields.Char(string="Employee Name")
    description = fields.Char(string="Description")
