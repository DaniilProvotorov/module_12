import unittest
import runner

class RunnerTest(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main

