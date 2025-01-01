# -*- coding: utf-8 -*-
{
    'name': "metallerie_sync_1618",

    'summary': "syncronisation odoo V16 V18",

    'description': """
Module pour la syncronisation de Odoo version 16 vers la version 18
    """,

    'author': "My Company",
    'website': "https://www.metallerie.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale_management','website','stock','purchase','website_sale','mrp','project_todo],

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
}

