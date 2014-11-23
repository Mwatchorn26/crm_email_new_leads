
#class MyController(http.Controller):
#
#    @http.route('/leads_by_email', type="http")
#    def some_html(self):
#        return "<h1>This is a test</h1>"
    
class NewLeadsController(http.Controller):
    _cp_path = '/crm/'
    _inherit = 'crm.lead'
#    _name = 'crm.newLeads'

    @http.route('/index', type="http")
    def index(self):
        """
        Returns a Login screen (input box for user id, and submit button) 
        The form submits the user id to the PunchIn function/webpage.
        """
        template = """<html>
                            <head></head>
                            <body>
                                <form action="/crm/email_to_new_leads" method="POST" style="vertical-align:middle">
                                    Email To: <input  name="to_addresses"/></textbox><br>
                                    <br>
                                    <button name="submit_emails" value="*">SUBMIT</button>
                                </form>
                            </body>
                      </html>"""

        return template


    @http.route('/email_to_new_leads', type="http", auth='user')
    def email_to_new_leads(self, to_addresses):
        """
         
        """
        print to_addresses
        print str(to_addresses)

        previous_results=""
        if str(to_addresses).len>0:
            previous_results="ECHOING ADDRESSES " + str(to_addresses) + "<br><br>"

        template = """<html>
                            <head></head>
                            <body>
                            """ + previous_results + """
                                <form action="/crm/email_to_new_leads" method="POST" style="vertical-align:middle">
                                    Email To: <input  name="to_addresses"/></textbox><br>
                                    <br>
                                    <button name="submit_emails" value="*">SUBMIT</button>
                                </form>
                            </body>
                      </html>"""

        return template

    def parse_input(self):
        address_string = self._context.get('input_form',[])
        #split the incoming data by a semicolon
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
            #find the index of the '.' occurring after the '@' 
            loc_dot = info[1].index(info[1],beg=loc_at)
            #slice the info[1] string to get just the domain            
            domain = info[1][loc_at+1:loc_dot]
            address_dict = {}
            address_dict = {'name':info[0], 'address':info[1]}
    


