class Client:
    def __init__(self, name, case_type):
        self.__name = name
        self.__case_type = case_type

    def get_name(self):
        return self.__name
    
    def get_case_type(self):
        return self.__case_type
    
    def show_details(self):
        return (self.get_name() , self.get_case_type())
       

class IndividualClient(Client):
    def __init__(self, name, case_type, personal_lawyer):
        super().__init__(name, case_type)
        self.__personal_lawyer = personal_lawyer

    def get_personal_lawyer(self):
        return self.__personal_lawyer

    def show_individual_details(self):
        
        return self.show_details() , self.get_personal_lawyer()
    
class CorporateClient(Client):
    def __init__(self, name, case_type, company_rep):
        super().__init__(name, case_type)
        self.__company_rep = company_rep

    def get_company_rep(self):
        return self.__company_rep

    def show_corporate_details(self):
        return super().show_details() + (self.get_company_rep(),) 


class Lawfully:
    def __init__(self):
        self.__clients = []
    
    def add_client(self, client):
        self.__clients.append(client)

    def get_all_clients(self):
        return [client.show_details() for client in self.__clients]


law_firm = Lawfully()

law_firm.add_client(IndividualClient("John Doe" , "Divorce" , "Atty. Smith"))
law_firm.add_client(CorporateClient("TechnoCorp Inc." , "Patent Dispute" , "Legal Head Mr. Brown"))


clients_data = law_firm.get_all_clients()

for data in clients_data:
    print(data)

# case =  Client("Zander", "Tax")
# print(case.show_details())

# client = IndividualClient("Zander", "Tax", "Brody")        
# print(client.show_individual_details())

# client = CorporateClient("Red", "bread", "James")
# print(type(client.show_corporate_details()))

# print(type(case.show_details()))