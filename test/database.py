import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import vaultdatabaseengine

class MyTestCase(unittest.TestCase):
    def test_psql(self):
        #TODO exec psql connect
        print("hi")
        test = vaultdatabaseengine.Database()
        test.check_valid()
        self.assertEqual(test.valid, False)

    def test_psql_invalid_vault_url(self):
        #TODO figure out how to fail unit test check
        try:
            vaultdatabaseengine.Database(dbname="sdfk", vault_url="localhost", vault_port=8200, token="bla")
        except:
            print("did it")
            return

    def test_psql_invalid_vault_port(self):
        try:
            vaultdatabaseengine.Database(dbname="sdfk", vault_url="localhost", vault_port="a", token="bla")
        except:
            return

    def test_psql_valid(self):
        print(vaultdatabaseengine.Database(dbname="psql", vault_url="http://localhost", token="s.GoR2nisHPeKU1vOaw9hZ5L7h").get_creds())




if __name__ == '__main__':
    unittest.main()
