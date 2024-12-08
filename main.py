import unittest
import logging
import test_12_4


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_4.RunnerTest))
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)