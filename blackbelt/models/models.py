# -*- coding: utf-8 -*-

from odoo import models, fields, api


class blackbelt(models.Model):
     _name = 'blackbelt.blackbelt'
     _description = 'blackbelt.blackbelt'

     name = fields.Char(string = 'Device Id')
     serialnumber = fields.Char(string = 'Serial Number')
     manufacturer = fields.Char()
     model = fields.Char()
     modelnumber = fields.Char()
     storage = fields.Char()
     color = fields.Char()
     carrier = fields.Char()
     imei = fields.Char()
     imei2 = fields.Char()
     wipe_type = fields.Char()
     wipe_method = fields.Char()
     wipe_result = fields.Char()
     wipe_date = fields.Datetime(string='Lastest Wipe Date')
     blacklisted = fields.Char()
     date_create = fields.Datetime(string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date of Serial number by blackbelt")
    
            
class blackbeltserial(models.Model):
     _name = 'blackbelt.serial'
     _description = 'blackbelt.serial'

     name = fields.Char(string = 'Serial Number')
     manufacturer = fields.Char()
     date_create = fields.Datetime(string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date of Serial number by blackbelt")
    
    
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
     

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100