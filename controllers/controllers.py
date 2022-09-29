# -*- coding: utf-8 -*-
# from odoo import http


# class Bra(http.Controller):
#     @http.route('/bra/bra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bra/bra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bra.listing', {
#             'root': '/bra/bra',
#             'objects': http.request.env['bra.bra'].search([]),
#         })

#     @http.route('/bra/bra/objects/<model("bra.bra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bra.object', {
#             'object': obj
#         })
