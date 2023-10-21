# -*- coding: utf-8 -*-
from odoo import models, fields, _


class Examen(models.Model):

    _name = "hyd_examen.examen"
    _description = u"Examen"

    name = fields.Char(string="Nom", required=True)
    annee_id = fields.Many2one(
        comodel_name='hyd_examen.annee_scolaire',
        string='Annee Scolaire',
    )
    date_debut = fields.Date(string='Date de debut')
    date_fin = fields.Date(string='Date de fin')
    composition_id = fields.Many2one(
        comodel_name="hyd_examen.composition",
        string='Candidature',
        domain=[('is_parent', '=', False)]
    )
    classe_ids = fields.Many2many(
        comodel_name='hyd_examen.classe',
        string='classe',
    )
    line_ids = fields.One2many(
        comodel_name='hyd_examen.examen_line',
        inverse_name='examen_id',
        string='lines',
    )

    def generer_examen_line(self):
        salle_obj = self.env["hyd_examen.salle"]
        exaline_obj = self.env["hyd_examen.examen_line"]
        candidature_obj = self.env["hyd_examen.candidature"]
        for rec in self:

            # generer examen line pour chaque classe
            for classe in rec.classe_ids:
                salles = salle_obj.search([('classe_id', '=', classe.id)])

                val = {
                    'name': _("%s en %s") % (rec.name, classe.name),
                    'examen_id': rec.id,
                    'classe_id': classe.id,
                    'date_debut': rec.date_debut,
                    'date_fin': rec.date_fin,
                    'salle_ids': [[6, False, salles.ids]]
                }
                exaline = exaline_obj.create(val)

                for salle in salles:
                    for eleve in salle.eleves_ids:
                        candidature = {
                            'name': "code secret",
                            'eleve_id': eleve.id,
                            'salle_id': salle.id,
                            'examen_line_id': exaline.id
                        }
                        candidature_obj.create(candidature)
