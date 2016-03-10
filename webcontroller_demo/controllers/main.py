# -*- coding: utf-8 -*-
from openerp import SUPERUSER_ID
from openerp.addons.web import http
from openerp.http import request


class WebsiteDemo(http.Controller):

    @http.route('/employee', type='http', auth='user', website=True)
    def display_employee_data(self):
        cr, context, pool = request.cr, request.context, request.registry

        hr_employee = pool.get('hr.employee')
        hr_employee_ids = hr_employee.search(cr, SUPERUSER_ID, [], context=context)
        hr_employee_data = hr_employee.browse(cr, SUPERUSER_ID, hr_employee_ids, context=context)

        values = {
                  'employees' : hr_employee_data 
                  }

        return request.website.render("website.employee", values)
