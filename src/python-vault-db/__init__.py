import requests as rq

class Database:
    def __init__(self, dbname, vault_url, token):
        self.dbname = dbname
        self.url = vault_url
        self.valid = False
        self.lastReq = None #TODO some datetime in here
        self.ttl = None
        self.token = token
        self.username = ""
        self.password = ""
        self.get_creds()

    def check_valid(self):
        #TODO check datetime for current datetime
        if self.ttl == None:
            return False
        return True

    def get_creds(self):
        self.check_valid()
        if (self.valid):
            return {"username": self.username, "password": self.password}
        else:
            rq.get(url=self.url, headers={"X-Vault-Token":self.token})
            #TODO set datetime for current datetime
            #TODO set these to the correct response values
            self.username = None
            self.password = None