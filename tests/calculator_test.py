from unittest import TestCase, main
from Testing.calculator_unittest import calculator


class CalculatorTest(TestCase):

    # Позитивные тесты (что вводим и что должны получить)
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2)

    def test_multi(self):
        self.assertEqual(calculator('9*4'), 36)

    # Непозитивные тесты
    # проверка raise exeption что оно должно вернуть при ошибочном вводе или при вводе доп знаков
    # вводим что угодно и какие предупреждения (ошибки) должны получить
    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('dfsfsas')
        self.assertEqual('Выражение должно содержать хотя бы один знак +-/*', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.0 * 3.4')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

if __name__ == '__main__':
    main()

# RED GREEN REFACTORING - сперва делваем смешанные тесты, провальные и  правильные и только
# после зеленые тесты
