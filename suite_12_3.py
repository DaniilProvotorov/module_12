import unittest
import tests_12_3

tour = unittest.TestSuite()
tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentCase))#называл класс немного по-другому при выполнении предыдущего задания
tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tour)