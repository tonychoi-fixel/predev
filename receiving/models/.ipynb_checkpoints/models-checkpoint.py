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
     operatingsystem = fields.Char()
     rooted = fields.Char()
     storage = fields.Char()
     color = fields.Char()
     carrier = fields.Char()
     carrierbuild = fields.Char()
     productversion = fields.Char()
     imei = fields.Char()
     imei2 = fields.Char()
     wifiaddress = fields.Char()
     bluetoothaddress = fields.Char()
     battery_health = fields.Char()
     battery_cyclecount = fields.Char()
     battery_level = fields.Char()
     battery_grading = fields.Char()
     wipe_type = fields.Char()
     wipe_method = fields.Char()
     wipe_result = fields.Char()
     wipe_duration = fields.Char()
     wipe_version = fields.Char()
     wipe_date = fields.Datetime(string='Wipe Date', required=False)
     func_result = fields.Char()
     func_duration = fields.Char()
     func_date = fields.Datetime(string='Function Date', required=False)
     blacklisted = fields.Char()
     userid = fields.Char()
     wipeid = fields.Char()
     licenseid_unique = fields.Char()
     licenseid_datawipe = fields.Char()
     licenseid_analyst = fields.Char()
     license_reportmode = fields.Char()
     license_name = fields.Char()
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

     name = fields.Char(readonly=False, required=True, string = 'ASN Number')
     ponumber = fields.Char(readonly=False, string = 'PO#')
     trackingnumber = fields.Char(readonly=False, string='Tracking#')
     shippingcarrier = fields.Char(readonly=False, string='Shiping Carrier')
     date_shipping = fields.Date(readonly=False, string='Shipping')
     date_receiving = fields.Date(readonly=False,string='Receiving')
     description = fields.Char(readonly=False)
     serialnumber = fields.Char(readonly=False, string = 'Serial Number')
     manufacturer = fields.Char(readonly=False)
     model = fields.Char(readonly=False)
     modelnumber = fields.Char(readonly=False)
     storage = fields.Char(readonly=False)
     color = fields.Char(readonly=False)
     carrier = fields.Char(readonly=False)
     imei = fields.Char(required=False)
     imei2 = fields.Char(readonly=False)
     sourcegrade = fields.Char(readonlhy=False, string='Sourcing Grade')
     cosmetic = fields.Char(readonlhy=False, string='Cosmetic')
     datawipe = fields.Char()
     function_key = fields.Char()
     function_full = fields.Char()
     userid = fields.Char()
     status = fields.Char(readonly=True, default='')
     windowspcname = fields.Char(readonly=False, string="PC Name")
     date_received = fields.Datetime(store=True, string='Rcvd Date', readonly=True, index=True, copy=False, help="Received date by blackbelt")
     date_update = fields.Datetime(compute="_date_now", store=True, string='Update Date', required=True, readonly=True, copy=False, default=fields.Datetime.now, help="Lastest Update Date")
     date_create = fields.Datetime(store=True, string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now, help="Creation date of Serial number by blackbelt")
