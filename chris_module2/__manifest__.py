# -*- coding: utf-8 -*-
{
    'name': "chris_module2",

    'summary': """
        Mi primer módulo
        by Chris""",

    'description': """
        Descripción de mi primer modulo propuesto para pruebas y aprender.
    """,

    'author': "ChrisIza",
    'website': "https://www.xphera.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '1.0001',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
