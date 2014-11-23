# -*- coding: utf-8 -*-
{
    "name" : "New Leads by Email Address",
    "summary":"""
        Create new leads by providing the email address. 
    """,
    "description" : """
        Create new leads by providing the email address.
        
        Possible formats:        
        * firstname lastname<emailname@domain.com> (creates a new lead with the name filled out as well as the email address)
        * emailname@domain.com (creates a new lead and inserts 'emailname' as firstname, lastname and part of the email address)
    """,
    "author" : "Transformix Engineering Inc.", 
    "website" : "http://www.Transformix.com",
    "depends" : ['base','crm'],
    "category" : "Customer Relationship Management",
    "version" : "0.1",
    "sequence": 16,
    #"init" : [],
    "demo" : [],
    "data" : ['email_to_new_leads_menu.xml'],
    "data" : [],    
    'test': [],
    #'installable': True,   
    #'complexity': "easy",
    #'active': False,
}