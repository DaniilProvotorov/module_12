import logging
import unittest
import rt_with_exceptions

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            f1 = rt_with_exceptions.Runner('Den', -10)
            logging.info('test_walk" выполнен успешно')
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            f1.walk()
            self.assertEqual(f1.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner', exc_info= True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            f2 = rt_with_exceptions.Runner(12, 16)
            logging.info('test_run" выполнен успешно')
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            f2.run()
            self.assertEqual(f2.distance, 100)
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info= True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8', format=
'%(asctime)s, %(levelname)s, %(message)s')

