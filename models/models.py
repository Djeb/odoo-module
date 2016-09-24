# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Application(models.Model):
    _name = 'lists.application'
    
    name = fields.Char(size=64)
    image = fields.Binary()
    description = fields.Html()
    final_date = fields.Date()
    state = fields.Selection([('open', 'Open'), 
    	('needs offer', 'Needs Offer'), ('offer', 'Offer'), ('approved','Approved'), 
    	('in progress', 'In progress'), ('ready', 'Ready'), ('verified', 'Verified'), ('close', 'Close')])

#    _columns = {
#    	'name' : fields.Char(size=64),
#    	'description' : fields.Html()
#    }

# class lists(models.Model):
#     _name = 'lists.lists'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100