# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': "extend_crm",
    'version': '18.0.0.1',
    'summary': """
            Extiende el modelo crm.lead con nuevos campos y lógica""",

    'description': """
           Este módulo agrega campos adicionales y lógica personalizada al modelo CRM Lead (crm.lead) 
           """,

    'author': "Marlon Palencia Cadena",
    'secuence': 15,
    'depends': [
        'crm'
    ],
    'data': [
        'data/demo_data.xml',
        'security/ir.model.access.csv',
        'views/crm_order_view.xml',
        'data/cron_compute_since_approved.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
