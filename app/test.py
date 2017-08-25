import unittest
import identidock

class Test(unittest.TestCase):
    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()
    def test_main_page(self):
        page = self.app.get("/")
        assert page.status_code == 200
    def test_post_request(self):
        page = self.app.post("/", data=dict(name="srt"))
        assert page.status_code == 200

if __name__ == "__main__":
    unittest.main()
