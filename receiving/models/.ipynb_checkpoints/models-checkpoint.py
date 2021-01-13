# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReceivingBlackbelt(models.Model):
     _name = 'receiving.blackbelt'
     _description = 'receiving.blackbelt'
#     _sql_constraints = [ ('uq_deviceserial', 'unique(name, serialnumber)', 'Cannot Use one serial number twice!\nPlease, check serial# and imei')	]
     _sql_constraints = [ ('uq_deviceid', 'unique(name)', 'Cannot Use one device ID twice!\nPlease, check serial# and imei'), ('uq_deviceserial', 'unique(serialnumber)', 'Cannot Use one serial number twice!\nPlease, check serial# and imei') ]

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
     batteryhealth = fields.Char()
     batterycyclecount = fields.Char()
     wipe_type = fields.Char()
     wipe_method = fields.Char()
     wipe_result = fields.Char()
     wipe_date = fields.Datetime(string='Lastest Wipe Date')
     blacklisted = fields.Char()
     userid = fields.Char()
     uniquelicenseid = fields.Char()
     licensereportmode = fields.Char()
     licenseid = fields.Char()
     wipeid = fields.Char()
     licensename = fields.Char()
     windowspcname = fields.Char(string="PC Name")
     locationmapped = fields.Char(string="Port Location")       
     date_update = fields.Datetime(compute="_date_now", store=True, string='Update Date', required=True, readonly=True, copy=False, default=fields.Datetime.now, help="Lastest Update Date")
     date_create = fields.Datetime(store=True, string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date of Serial number by blackbelt")
        
#     @api.depends('value')
     def _date_now(self):
         for record in self:
             record.date_update = fields.Datetime.now  
    
class ReceivingAsn(models.Model):
     _name = 'receiving.asn'
     _description = 'receiving.asn'
     _sql_constraints = [ ('uq_asnimei', 'unique(name, imei)', 'Cannot Use same ASN Number and Imei twice!\nPlease, check ASN# and Imei#')	]

     name = fields.Char(string = 'ASN Number')
     description = fields.Char()
     serialnumber = fields.Char(string = 'Serial Number')
     manufacturer = fields.Char()
     model = fields.Char()
     modelnumber = fields.Char()
     storage = fields.Char()
     color = fields.Char()
     carrier = fields.Char()
     imei = fields.Char(required=True)
     imei2 = fields.Char()
     userid = fields.Char()
     windowspcname = fields.Char(string="PC Name")
     date_update = fields.Datetime(compute="_date_now", store=True, string='Update Date', required=True, readonly=True, copy=False, default=fields.Datetime.now, help="Lastest Update Date")
     date_create = fields.Datetime(store=True, string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date of Serial number by blackbelt")
