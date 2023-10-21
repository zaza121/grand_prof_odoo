# -*- coding: utf-8 -*-
{
    'name': "Grand Prof",

    'summary': "Gerer les examens dans un examen",

    'description': """ Register all the salary grid of your enterprise """
                   """ and set inside the salary of contract form the """
                   """ salary using his grid. By the way update all """
                   """ salary of employee by modifying the grid. """,

    'author': "HyD Freelance",
    'website': "http://",
    'category': u'School',
    'version': '13.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
            # data
            # "data/petites.xml",
            # "data/coups.xml",
            # views
            # "views/menu.xml",
            # "views/eleve_views.xml",
            # "views/matiere_views.xml",
            # "views/candidature_views.xml",
            # "views/cycle_views.xml",
            # "views/classe_views.xml",
            # "views/cours_views.xml",
            # "views/salle_views.xml",
            # "views/epreuve_views.xml",
            # "views/composition_views.xml",
            # "views/examen_views.xml",
            # "views/examen_line_views.xml",
            # "views/annee_scolaire_views.xml",
            # "views/note_views.xml",
            # "views/group_cours_views.xml",
            # "views/templates.xml",
            "views/res_partner_views.xml",

            # workflow
            # security
            # "security/ir.model.access.csv",
            # reports
            # "reports/bulletin_note.xml",
            # wizards
            # "wizards/print_bulletin_wizard_views.xml",
    ],

    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'price': 100,
    'currency': 'USD',
    'images': ['static/images/main_screenshot.png']
}
