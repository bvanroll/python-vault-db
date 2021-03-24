import requests as rq
import datetime as dt

class Database2:
    def __init__(self, dbname, vault_url, token, vault_port=8200):
        self.dbname = dbname
        self.url = vault_url + ":" + str(vault_port) + "/v1/database/creds/" + dbname
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

    def update_creds(self):
        r = rq.get(url=self.url, headers={"X-Vault-Token": self.token, "Content-Type": "application/json"})
        # print(r.status_code)
        # print(r.text)
        if r.status_code != 200:
            raise Exception("status code was nog 200")
        data = r.json()
        # TODO set datetime for current datetime
        # TODO set these to the correct response values
        self.username = data["data"]["username"]
        self.password = data["data"]["password"]
        self.lease_id = data["lease_id"]
        self.request_id = data["request_id"]
        self.wrap_info = data["wrap_info"]
        self.warnings = data["warnings"]
        self.auth = data["auth"]
        self.ttl = dt.datetime.now() + dt.timedelta(seconds=float(data["lease_duration"]))


    def get_creds(self):
        if not (self.check_valid()):
            self.update_creds()
        return {"username": self.username, "password": self.password}

    def get_username(self):
        if not (self.check_valid()):
            self.update_creds()
        return self.username
