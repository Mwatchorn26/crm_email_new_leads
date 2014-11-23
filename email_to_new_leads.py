# -*- coding: utf-8 -*-
##############################################################################
#
#    Transformix Engineering Inc.
#    Copyright (C) 2004-today Transformix Engineering (<http://www.transformix.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models

class create_lead(models.TransientModel):
    """Create Lead"""
    _name = "leads_by_email.create"

    input_form = fields.Char(string="Emails", required=True)
    
    def parse_input(self):
        address_string = self._context.get('input_form',[])
        #split the incoming data by a semi-colon
        addresses = address_string.split(';')
        #loop through all the addresses found
        for address in addresses:
            #strip away spaces before and after our address
            address = address.strip()
            if '<' not in address:
                address = '<'.join(address)
            #remove any trailing '>' if they exist, and split the address based on the less-than symbol.
            info = address.replace('>','').split('<')
            
            #verify that there are no spaces in the email address.
            assert(' ' not in info[1])
            
            #find the index of the '@' symbol
            loc_at = info[1].index(info[1])
            #find the index of the '.' ocurring after the '@' 
            loc_dot = info[1].index(info[1],beg=loc_at)
            #slice the info[1] string to get just the domain            
            domain = info[1][loc_at+1:loc_dot]
            address_dict = {}
            address_dict = {'name':info[0], 'address':info[1]}
    

    @api.multi
    def confirm(self):
        events = self.env['event.event'].browse(self._context.get('event_ids', []))
        events.do_confirm()
        return {'type': 'ir.actions.act_window_close'}
