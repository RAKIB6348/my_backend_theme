# -*- coding: utf-8 -*-
# from odoo import http


# class MyBackendTheme(http.Controller):
#     @http.route('/my_backend_theme/my_backend_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_backend_theme/my_backend_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_backend_theme.listing', {
#             'root': '/my_backend_theme/my_backend_theme',
#             'objects': http.request.env['my_backend_theme.my_backend_theme'].search([]),
#         })

#     @http.route('/my_backend_theme/my_backend_theme/objects/<model("my_backend_theme.my_backend_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_backend_theme.object', {
#             'object': obj
#         })

