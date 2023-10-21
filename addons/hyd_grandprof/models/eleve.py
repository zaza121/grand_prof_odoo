# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.modules.module import get_module_resource
import base64


class Eleve(models.Model):

    _inherit = ['hr.employee.base', 'mail.thread', 'mail.activity.mixin', 'resource.mixin', 'image.mixin']
    _name = "hyd_examen.eleve"
    _description = "Eleve"

    name = fields.Char(
        string="Employee Name",
        related='resource_id.name',
        store=True,
        readonly=False,
        tracking=True
    )
    prenom = fields.Char(string='Prenom')
    user_id = fields.Many2one(
        'res.users',
        'User',
        related='resource_id.user_id',
        store=True,
        readonly=False
    )
    user_partner_id = fields.Many2one(
        related='user_id.partner_id',
        related_sudo=False,
        string="User's partner"
    )
    active = fields.Boolean(
        'Active',
        related='resource_id.active',
        default=True,
        store=True,
        readonly=False
    )
    address_home_id = fields.Many2one(
        'res.partner',
        'Address',
        help='Enter here the private address of the employee, not the one linked to your company.',
        groups="hr.group_hr_user", tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]"
    )
    is_address_home_a_company = fields.Boolean(
        'The employee address has a company linked',
        compute='_compute_is_address_home_a_company',
    )
    private_email = fields.Char(
        related='address_home_id.email',
        string="Private Email",
        groups="hr.group_hr_user"
    )
    country_id = fields.Many2one(
        'res.country',
        'Nationality (Country)',
        groups="hr.group_hr_user",
        tracking=True
    )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
        groups="hr.group_hr_user",
        default="male",
        tracking=True
    )
    birthday = fields.Date(
        'Date of Birth',
        groups="hr.group_hr_user",
        tracking=True
    )
    image_1920 = fields.Image(default=lambda self: self._default_image())
    phone = fields.Char(
        related='address_home_id.phone',
        related_sudo=False,
        readonly=False,
        string="Private Phone",
        groups="hr.group_hr_user"
    )
    child_ids = fields.One2many(
        'hr.employee',
        'parent_id',
        string='Direct subordinates'
    )
    note_ids = field_name_ids = fields.One2many(
        comodel_name='hyd_examen.note',
        inverse_name='eleve_id',
        string='Notes',
    )
    number_notes = fields.Integer(
        string='Nombre dde notes',
        compute="_compute_number_notes")

    @api.model
    def _default_image(self):
        image_path = get_module_resource('hr', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    def _compute_number_notes(self):
        for rec in self:
            rec.number_notes = len(rec.note_ids)

    @api.model
    def get_bulletin_info(self, examen_id):

        note_ids = self.note_ids.filtered(lambda x: x.examen_id.id == examen_id)
        group_cours = note_ids.mapped("epreuve_id.cours_id.group_id")
        group_cours.sorted(key=lambda r: r.sequence)

        gen_moyenne = 0
        gen_coef = 0
        gen_mc = 0
        groups = []

        for group in group_cours:

            g_moyenne = 0
            g_coef = 0
            g_mc = 0

            notes = []
            for note in note_ids.filtered(lambda x: x.epreuve_id.cours_id.group_id.id == group.id):
                moyenne = note.valeur
                coef = note.epreuve_id.cours_id.coef
                notes.append({
                    'matiere': note.epreuve_id.cours_id.name,
                    'enseignant': note.epreuve_id.cours_id.enseignant.name,
                    'moyenne': moyenne,
                    'coef': coef,
                    'total': coef * moyenne,
                    'objectif': note.epreuve_id.objectif,
                    'observation': note.name,
                })

                g_coef += coef
                g_mc += coef * moyenne

            g_moyenne = g_mc / g_coef or 1
            groups.append({
                'group': group.name,
                'g_moyenne': g_moyenne,
                'g_coef': g_coef,
                'g_mc': g_mc,
                'notes': notes})

            gen_coef += g_coef
            gen_mc += g_mc

        gen_moyenne = gen_mc / gen_coef or 1
        res = {
            'gen_moyenne': gen_moyenne,
            'gen_coef': gen_coef,
            'gen_mc': gen_mc,
            'notes': groups}
        return res

    def open_notes(self):
        self.ensure_one()
        action = self.env.ref("hyd_examen.note_action_view").read()[0]
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = {"search_default_gp_examen_line_id": 1}
        return action

    def print_bulletin(self):
        self.ensure_one()
        action = self.env.ref("hyd_examen.print_bulletin_wizard_action").read()[0]
        action['context'] = {"default_eleve_ids": self.ids}
        return action
