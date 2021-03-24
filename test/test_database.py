import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src

class DatabaseClassTests(unittest.TestCase):

    def test_vault_connection_error(self):
        #TODO give some "valid" url
        self.fail()

    def test_vault_non_existent_database(self):
        #TODO test non existent_database
        self.fail()

    def test_psql_connection(self):
        #TODO exec psql connect
        print("hi")
        test = src.Database()
        test.check_valid()
        self.assertEqual(test.valid, False)

    def test_psql_invalid_vault_url(self):
        try:
            src.Database(dbname="sdfk", vault_url="localhost", vault_port=8200, token="bla")
        except:
            #TODO check the err msg
            return
        else:
            self.fail()


    def test_psql_invalid_vault_port(self):
        try:
            src.Database(dbname="sdfk", vault_url="localhost", vault_port="a", token="bla")
        except:
            #TODO check the error message
            return
        else:
            self.fail()


    def test_psql_valid(self):
        print(src.Database(dbname="psql", vault_url="http://localhost", token="s.GoR2nisHPeKU1vOaw9hZ5L7h").get_creds())




if __name__ == '__main__':
    unittest.main()
