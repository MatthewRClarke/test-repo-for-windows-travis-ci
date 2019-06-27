from unittest import TestCase

class TestExample(TestCase):
    def test_that_int_cast_rounds_down(self):
        self.assertEqual(int(1.656), 1)
