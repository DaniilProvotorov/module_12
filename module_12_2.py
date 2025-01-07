import unittest
import runner_and_tournament

class TournamentCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        #print(all_results)


    def setUp(self):
        self.r1 = runner_and_tournament.Runner('Усейн', 10)
        self.r2 = runner_and_tournament.Runner('Андрей', 9)
        self.r3 = runner_and_tournament.Runner('Ник', 3)




    def tearDown(self):
        print(self.all_results)

    def test_Tournament1(self):
        t1 = runner_and_tournament.Tournament(90, self.r1, self.r3)
        all_results = t1.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results





    def test_Tournament2(self):
        t2 = runner_and_tournament.Tournament(90,  self.r2, self.r3)
        all_results = t2.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results

    def test_Tournament3(self):
        t3 = runner_and_tournament.Tournament(90, self.r1, self.r2, self.r3)
        all_results = t3.start()
        last_key = max(all_results.keys())
        last_runner = all_results[last_key]
        self.assertTrue(last_runner == self.r3)
        self.all_results = all_results




if __name__ == "__main__":
    unittest.main()