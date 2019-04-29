import unittest
from redact_problem import Redact


class Redact_Words(unittest.TestCase):

    def test_input(self):
        redact_obj = Redact()
        assert redact_obj.redact_words(['This', 'is', 'sample', 'text'], ['sample']) == ['This', 'is', 'text']  # base case
        assert redact_obj.redact_words(['This', 'is', 'sample', 'text'], ['text']) == ['This', 'is', 'sample']

if __name__ == '__main__':
    unittest.main()
