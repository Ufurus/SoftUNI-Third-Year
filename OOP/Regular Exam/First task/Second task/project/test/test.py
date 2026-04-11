from unittest import TestCase, main
from project.star_system import StarSystem

class StarSystemTest(TestCase):

    def setUp(self):
        """Initializes a base system for reuse."""
        self.star_system = StarSystem("TestSystem", "Red giant", 'Single', 5)

    def test_init(self):
        self.assertEqual('TestSystem', self.star_system.name)
        self.assertEqual('Red giant', self.star_system.star_type)
        self.assertEqual('Single', self.star_system.system_type)
        self.assertEqual(5, self.star_system.num_planets)
        self.assertIsNone(self.star_system.habitable_zone_range)

    def test_name_raises_for_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("   ", "Red giant", 'Single', 5)
        self.assertEqual('Name must be a non-empty string.', str(ex.exception))

    def test_star_type_raises_for_invalid_type(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Ugabuga", 'Single', 5)
        expected_msg = f'Star type must be one of {sorted(StarSystem._STAR_TYPES)}.'
        self.assertEqual(expected_msg, str(ex.exception))

    def test_system_type_raises_for_invalid_type(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", 'Ugabuga', 5)
        expected_msg = f'System type must be one of {sorted(StarSystem._STAR_SYSTEM_TYPES)}.'
        self.assertEqual(expected_msg, str(ex.exception))

    def test_num_planets_raises_for_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", 'Single', -1)
        self.assertEqual('Number of planets must be a non-negative integer.', str(ex.exception))

    def test_habitable_zone_range_raises_for_invalid_values(self):
        # Case: Start is greater than end
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", 'Single', 5, (5, 2))
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ex.exception))

        # Case: Tuple length is not 2
        with self.assertRaises(ValueError) as ex:
            StarSystem("Alpha", "Red giant", 'Single', 5, (1, 2, 3))
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ex.exception))

    def test_gt_operator_raises_when_not_habitable(self):
        """Tests the > operator directly."""
        s1 = StarSystem("Alpha", "Red giant", "Single", 5, (1.0, 3.0))
        # s2 is not habitable because habitable_zone_range is None
        s2 = StarSystem("Beta", "Red giant", "Single", 5, None)

        with self.assertRaises(ValueError) as ex:
            _ = s1 > s2
        self.assertEqual("Comparison not possible: One or both systems lack a defined habitable zone or planets.", str(ex.exception))

    def test_compare_star_systems_returns_correct_messages(self):
        """Tests the static method for success and failure cases."""
        s1 = StarSystem("Alpha", "Red giant", "Single", 5, (1.0, 5.0)) # Width: 4.0
        s2 = StarSystem("Beta", "Red giant", "Single", 5, (1.0, 2.0))  # Width: 1.0
        s3 = StarSystem("Gamma", "Red giant", "Single", 0, (1.0, 2.0)) # Not habitable (0 planets)

        # Case: s1 > s2
        res1 = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual(res1, "Alpha has a wider habitable zone than Beta.")

        # Case: s2 < s1 (s1 is wider or equal)
        res2 = StarSystem.compare_star_systems(s2, s1)
        self.assertEqual(res2, "Alpha has a wider or equal habitable zone compared to Beta.")

        # Case: Error caught and returned as string
        res3 = StarSystem.compare_star_systems(s1, s3)
        self.assertEqual(res3, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

if __name__ == '__main__':
    main()