# -*- coding: utf-8 -*-
# from odoo import http


# class Detectius(http.Controller):
#     @http.route('/detectius/detectius', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/detectius/detectius/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('detectius.listing', {
#             'root': '/detectius/detectius',
#             'objects': http.request.env['detectius.detectius'].search([]),
#         })

#     @http.route('/detectius/detectius/objects/<model("detectius.detectius"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('detectius.object', {
#             'object': obj
#         })
