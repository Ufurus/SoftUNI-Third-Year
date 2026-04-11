class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

from unittest import TestCase, main

class WorkerTest(TestCase):

    def test_init(self):
        worker = Worker("test", 1000, 100)
        self.assertEqual("test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works_no_energy_raises(self):
        worker = Worker("test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        worker.energy = -1
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work(self):
        worker = Worker("test", 1000, 100)
        self.assertEqual(0, worker.money)
        self.assertEqual(100, worker.energy)

        worker.work()
        self.assertEqual(99, worker.energy)
        self.assertEqual(1000, worker.money)

        worker.work()
        self.assertEqual(98, worker.energy)
        self.assertEqual(2000, worker.money)

    def test_get_info(self):
        worker = Worker("test", 1000, 100)
        expected_result = 'test has saved 0 money.'
        result = worker.get_info()
        self.assertEqual(expected_result, result)

        worker.work()
        expected_result = 'test has saved 1000 money.'
        result = worker.get_info()
        self.assertEqual(expected_result, result)

    def test_rest(self):
        worker = Worker("test", 1000, 100)
        self.assertEqual(100, worker.energy)

        worker.rest()
        self.assertEqual(101, worker.energy)

        worker.rest()
        self.assertEqual(102, worker.energy)

if __name__ == '__main__':
    main()