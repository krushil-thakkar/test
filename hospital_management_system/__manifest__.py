# -*- coding: utf-8 -*-
{
    'name': "hospital management system",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/clinic.xml',
        'views/doctor.xml',
        'views/template.xml',
        'views/create_patient.xml',
        'wizards/create_doctor.xml',
        'wizards/appointment_report_view.xml',
        'report/report_prescription_details.xml',
        'report/report.xml',
        'views/patient.xml',
        'views/prescription.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
