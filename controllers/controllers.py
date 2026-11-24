# from odoo import http


# class AppTow(http.Controller):
#     @http.route('/app_tow/app_tow', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_tow/app_tow/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_tow.listing', {
#             'root': '/app_tow/app_tow',
#             'objects': http.request.env['app_tow.app_tow'].search([]),
#         })

#     @http.route('/app_tow/app_tow/objects/<model("app_tow.app_tow"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_tow.object', {
#             'object': obj
#         })

