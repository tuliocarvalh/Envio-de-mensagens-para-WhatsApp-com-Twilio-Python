
from twilio.rest import Client 



account_sid = '' 
auth_token = '' 

client = Client(account_sid, auth_token) 

twilionumber = ''
my_number= ''



def in_wpp(self) :

    message = client.messages.create( 
                                      from_=twilionumber,  
                                      body=self,      
                                      to=my_number, 
                                  ) 
        
    print(message.sid)
