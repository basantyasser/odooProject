# -*- coding: utf-8 -*-
# from odoo import http


# class PrintCertificate(http.Controller):
#     @http.route('/print_certificate/print_certificate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/print_certificate/print_certificate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('print_certificate.listing', {
#             'root': '/print_certificate/print_certificate',
#             'objects': http.request.env['print_certificate.print_certificate'].search([]),
#         })

#     @http.route('/print_certificate/print_certificate/objects/<model("print_certificate.print_certificate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('print_certificate.object', {
#             'object': obj
#         })
