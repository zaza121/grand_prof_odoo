# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ExamenLine(models.Model):

    _name = "hyd_examen.examen_line"
    _description = u"Examen by Class"

    name = fields.Char(string="Observation", required=True)
    examen_id = fields.Many2one(
        comodel_name='hyd_examen.examen',
        string='Examen',
    )
    classe_id = fields.Many2one(
        comodel_name='hyd_examen.classe',
        string='Classe',
    )
    number_candidat = fields.Integer(string='Nombre candidat')
    date_debut = fields.Date(string='Date de debut')
    date_fin = fields.Date(string='Date de fin')
    salle_ids = fields.Many2many(
        comodel_name='hyd_examen.salle',
        string='Salles',
    )
    epreuve_ids = fields.One2many(
        comodel_name='hyd_examen.epreuve',
        inverse_name='examen_line_id',
        string='Epreuves',
    )
    candidature_ids = fields.One2many(
        comodel_name='hyd_examen.candidature',
        inverse_name='examen_line_id',
        string='Candidats',
    )

    def generer_epreuves(self):
        note_obj = self.env["hyd_examen.note"]
        epreuve_obj = self.env["hyd_examen.epreuve"]
        for rec in self:

            # generer examen line pour chaque classe
            for cour in rec.classe_id.cours_ids:
                # salles = salle_obj.search([('classe_id', '=', classe.id)])

                val = {
                    'name': _("%s - %s") % (rec.name, cour.name),
                    'classe_id': rec.classe_id.id,
                    'cours_id': cour.id,
                    'date_debut': rec.date_debut,
                    'date_fin': rec.date_fin,
                    'examen_line_id': rec.id,
                    'examen_id': rec.examen_id.id
                }

                epreuve = epreuve_obj.create(val)

                for candidat in rec.candidature_ids:
                    note = {
                        'name': "Observation",
                        'candidature_id': candidat.id,
                        'epreuve_id': epreuve.id,
                        'valeur': 1,
                    }
                    note_obj.create(note)
