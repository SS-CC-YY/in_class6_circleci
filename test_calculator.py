"""
Tests for calculator app
"""
import calculator


class TestCalculatorAPP:
    def test_add(self):
        assert 5 == calculator.add(2,3)

    def test_subtract(self):
        assert 5 == calculator.subtract(8,3)