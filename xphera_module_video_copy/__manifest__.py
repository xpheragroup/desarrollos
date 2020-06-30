# -*- coding: utf-8 -*-
{
    'name': "Módulo Xphera Video Copy",

    'summary': """
        Módulo con Desarrollos a la medida para suplir necesidades.""",

    'description': """
        Módulo con Desarrollos a la medida para suplir necesidades.""",

    'author': "Xphera Group S.A.S.",
    'website': "http://www.xphera.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'mrp', 'product'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
