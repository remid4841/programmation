import unittest
from demo.demo import ClientS3


class TestClientS3(unittest.TestCase):
    def test_put_object(self):
        s3cl = ClientS3()
        response = s3cl.put_object("blarg", "my-bucket", "file.txt")
        response_status = response['ResponseMetadata']["HTTPStatusCode"]
        self.assertEqual(response_status, 200)


if __name__ == "__main__":
    unittest.main()
