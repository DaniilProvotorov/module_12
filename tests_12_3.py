import unittest
import runner
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        f1 = runner.Runner('Den')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        f2 = runner.Runner('Max')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        f3 = runner.Runner('Mol')
        f4 = runner.Runner('Cal')
        f3.run()
        f3.run()
        f3.run()
        f3.run()
        f4.walk()
        f4.walk()
        f4.walk()
        f4.walk()
        self.assertNotEqual(f3.distance, f4.distance)

class TournamentCase(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}



    def setUp(self):
        self.r1 = runner_and_tournament.Runner('Усейн', 10)
        self.r2 = runner_and_tournament.Runner('Андрей', 9)
        self.r3 = runner_and_tournament.Runner('Ник', 3)




    def tearDown(self):
        print(self.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        t1 = runner_and_tournament.Tournament(90, self.r1, self.r3)
        all_results = t1.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament2(self):
        t2 = runner_and_tournament.Tournament(90,  self.r2, self.r3)
        all_results = t2.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament3(self):
        t3 = runner_and_tournament.Tournament(90, self.r1, self.r2, self.r3)
        all_results = t3.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results