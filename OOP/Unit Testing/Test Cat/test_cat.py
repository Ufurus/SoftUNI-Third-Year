class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

from unittest import TestCase, main

class TestCat(TestCase):

    def test_size(self):
        cat = Cat('cat')
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_eat(self):
        cat = Cat('cat')
        cat.eat()
        self.assertEqual(cat.fed, True)

    def test_eat_after_already_fed(self):
        cat = Cat('cat')
        cat.fed = True
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_fall_asleep(self):
        cat = Cat('cat')
        cat.fed = False
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep(self):
        cat = Cat('cat')
        cat.eat()

        self.assertTrue(cat.sleepy)

        cat.sleep()

        self.assertFalse(cat.sleepy)

if __name__ == '__main__':
    main()
