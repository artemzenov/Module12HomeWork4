import rt_with_exceptions
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_runner = rt_with_exceptions.Runner(name='TestName', speed=-1)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_runner = rt_with_exceptions.Runner(name=2)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = rt_with_exceptions.Runner(name='TestName1')
        test_runner2 = rt_with_exceptions.Runner(name='TestName2')
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)