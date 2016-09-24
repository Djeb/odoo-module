# -*- coding: utf-8 -*-
{
    'name': "Lists",
    'summary': """
        Module for edit and viewing applications list""",
    'description': """
        Make the dream come true
    """,
    'author': "K.W.",
    'website': "-",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'demo': [
        'views/demo.xml',
    ],
    # always loaded
    'application': True,
    'installable': True,
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml'
        #'views/table_view.xml',
    ],
        
}