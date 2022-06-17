import unittest

from display_log import LogLine
from main import parse

# the log line that will be used in comparison
exampleLogLine: str = """[2022-06-13T11:16:05.617Z] "GET /metrics HTTP/1.1" 200 - via_upstream - "-" 0 16352 2 2 "-" "Prometheus/2.28.1" "87e3003d-bb9d-4b76-8ff8-d243780b9444" "172.16.147.14:8080" "172.16.147.14:8080" inbound|8080|| 127.0.0.6:44234 172.16.147.14:8080 172.16.31.6:60392 - default"""


class TestLogPasser(unittest.TestCase):

    #  the object LogLine to the exampleLogLine
    def test_run(self):
        self.assertEqual(
            LogLine("2022-06-13T11:16:05.617Z", "GET", "/metrics", "HTTP/1.1", "200", "-", "via_upstream", "-", "-",
                    "0", "16352", "2", "2", "-", "Prometheus/2.28.1", "87e3003d-bb9d-4b76-8ff8-d243780b9444",
                    "172.16.147.14:8080", "172.16.147.14:8080", "inbound|8080||", "127.0.0.6:44234",
                    "172.16.147.14:8080", "172.16.31.6:60392", "-", "default"),
            parse(exampleLogLine),
            "Something is wrong")