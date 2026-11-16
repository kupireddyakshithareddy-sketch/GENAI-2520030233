
import unittest

def calculate_cost(input_tokens, output_tokens, input_price, output_price):
    input_cost = (input_tokens / 1000000) * input_price
    output_cost = (output_tokens / 1000000) * output_price
    return input_cost + output_cost


class TestBudget(unittest.TestCase):

    def test_normal_cost(self):
        cost = calculate_cost(10000, 2000, 0.15, 0.60)
        self.assertAlmostEqual(cost, 0.0027)

    def test_zero_tokens(self):
        cost = calculate_cost(0, 0, 0.15, 0.60)
        self.assertEqual(cost, 0)

    def test_input_only(self):
        cost = calculate_cost(10000, 0, 0.15, 0.60)
        self.assertAlmostEqual(cost, 0.0015)

    def test_output_only(self):
        cost = calculate_cost(0, 2000, 0.15, 0.60)
        self.assertAlmostEqual(cost, 0.0012)


if __name__ == "__main__":
    unittest.main()
