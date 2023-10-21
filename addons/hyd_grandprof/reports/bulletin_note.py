from odoo import api, models


class ReportBulletinNote(models.AbstractModel):
    _name = 'report.hyd_examen.bulletin_note_template'

    def _get_report_values(self, docids, data=None):
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('hyd_examen.bulletin_note_template')
        # get the records selected for this rendering of the report
        obj = self.env[report.model].browse(docids or data.get('eleves_ids', []))
        eleves = self.env["hyd_examen.eleve"].browse(
            obj.eleve_id and obj.eleve_id.id or data.get('eleves_ids', []))
        candidatures = self.env["hyd_examen.candidature"].browse(docids)
        # return a custom rendering context
        # raise Warning(candidatures)
        return {
            # 'lines': docids.get_lines(),
            'docs': candidatures,
            'data': data,
        }
