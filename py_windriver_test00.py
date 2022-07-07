import unittest
from appium import webdriver


class SampleTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_input(self):
        self.driver.find_element_by_accessibility_id("clearButton").click()
        self.driver.find_element_by_accessibility_id("num7Button").click()

        result = self.driver.find_element_by_accessibility_id(
            "CalculatorResults")
        self.assertIn(" 7 ", str(result.text))

    def test_calc(self):
        self.driver.find_element_by_accessibility_id("num2Button").click()
        self.driver.find_element_by_accessibility_id("plusButton").click()
        self.driver.find_element_by_accessibility_id("num7Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id(
            "CalculatorResults")
        self.assertIn(" 9 ", str(result.text))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SampleTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
