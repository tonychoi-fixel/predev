# -*- coding: utf-8 -*-
from odoo import http


class Blackbelt(http.Controller):
     @http.route('/blackbelt/blackbelt/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/blackbelt/blackbelt/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('blackbelt.listing', {
             'root': '/blackbelt/blackbelt',
             'objects': http.request.env['blackbelt.blackbelt'].search([]),
         })

     @http.route('/blackbelt/blackbelt/objects/<model("blackbelt.blackbelt"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('blackbelt.object', {
             'object': obj
         })
