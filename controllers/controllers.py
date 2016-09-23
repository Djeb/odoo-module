# -*- coding: utf-8 -*-
from openerp import http

# class Lists(http.Controller):
#     @http.route('/lists/lists/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lists/lists/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lists.listing', {
#             'root': '/lists/lists',
#             'objects': http.request.env['lists.lists'].search([]),
#         })

#     @http.route('/lists/lists/objects/<model("lists.lists"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lists.object', {
#             'object': obj
#         })