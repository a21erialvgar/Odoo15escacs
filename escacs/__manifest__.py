# -*- coding: utf-8 -*-
{
    'name': "ChessERP",

    'summary': """
        Modul per gestionar dades sobre competicions d'escacs""",

    'description': """
        Amb aquest mòdul es podran gestionar les dades sobre tornejos, partides i jugadors d'escacs d'arreu del món.
    """,

    'author': "Eric Alves García",
    'website': "http://www.inspedralbes.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #Indiquem que també es aplicació
    'application': True,
}
