# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"
    
    tel_user_id = fields.Char(
        string='Id Telegram'
    )
