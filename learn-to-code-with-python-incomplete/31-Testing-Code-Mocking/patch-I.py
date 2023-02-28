#import urllib.request


# class WebRequest():

#     @classmethod
#     def url(cls):
#         return cls('https://www.google.com/')
    
#     def __init__(self, url):
#         self._url = url
    
#     def execute(self):
#         response = urllib.request.urlopen(self._url)
#         return True if response.status == 200 else False

# wr = WebRequest.url()
# print(wr.execute())


import urllib.request
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"
        return "FAILURE"
    
class WebRequestTest(unittest.TestCase):

    def test_execute_with_success_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "SUCCESS")

    def test_execute_with_failure_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 404
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "FAILURE")
            
if __name__ == "__main__":
    unittest.main()
