# -*- coding: utf-8 -*-

import datetime
from odoo import _, api, fields, models
from odoo.exceptions import UserError


def get_hierachy(elt):
    res = []
    for line in elt.child_ids:
        res.extend(get_hierachy(line))
    res.append(elt)
    return res


class PrintBulletinWizard(models.TransientModel):
    _name = 'print.bulletin.wizard'
    _description = 'Print Bulletin de note wizard'

    examen_id = fields.Many2one(
        comodel_name='hyd_examen.examen',
        string='Examen'
    )
    eleve_ids = fields.Many2many(
        comodel_name='hyd_examen.eleve',
        string='Eleves',
    )

    def print_bulletin(self):
        self.ensure_one()

        hierachies = get_hierachy(self.examen_id.composition_id)
        eleves = [
            ev.get_bulletin_info(self.examen_id.id) for ev in self.eleve_ids]
        datas = {
            'eleves_ids': self.eleve_ids.ids,
            'eleves': eleves,
            'examen': self.examen_id.id,
            'header_exam': [hierachy.name for hierachy in hierachies]
        }
        res = self.env.ref("hyd_examen.report_bulletin_note").report_action(
            [], data=datas)
        return res
