# -*- coding: utf-8 -*-
from odoo import http


class Receiving(http.Controller):
     @http.route('/receiving/blackbelt/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/receiving/blackbelt/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('receiving.listing', {
             'root': '/receiving/blackbelt',
             'objects': http.request.env['receiving.blackbelt'].search([]),
         })

     @http.route('/receiving/blackbelt/objects/<model("receiving.blackbelt"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('receiving.object', {
             'object': obj
         })
