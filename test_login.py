
import unittest

def login(username, password):
    if username == "student" and password == "12345":
        return "Login Successful"
    return "Invalid Credentials"


class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        result = login("student", "12345")
        self.assertEqual(result, "Login Successful")

    def test_invalid_login(self):
        result = login("student", "wrong123")
        self.assertEqual(result, "Invalid Credentials")


if __name__ == "__main__":
    unittest.main()
