# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Webcontroller Demo',
    'category': 'Website',
    'sequence': 160,
    'website': 'https://www.surekhatech.com/',
    'summary': 'Website, Website controller, Controller Demo',
    'version': '1.0',
    'description': """
Website Controller Demo
============

        """,
    'depends': ['hr','website'],
    'data': [
        'data/data.xml',
        'views/templates.xml'
    ],
    'installable': True,
    'application': True,
}