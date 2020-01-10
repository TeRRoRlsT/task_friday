import unittest

from main import create_canvas, draw_line, draw_rectangle, brush, main, INPUT_FILE, OUTPUT_FILE
from unittest.mock import patch, call


class TestPaint(unittest.TestCase):
    def setUp(self):
        self.canvas = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ]

    def test_create_canvas_wrong_params(self):
        self.assertRaises(IndexError, create_canvas, None, -10, -15)
        self.assertRaises(IndexError, create_canvas, None, 2, -10)

        self.assertRaises(TypeError, create_canvas, None, int, 3)
        self.assertRaises(TypeError, create_canvas, [], 2, None)

        self.assertRaises(ValueError, create_canvas, None, 2, 'error')
        self.assertRaises(ValueError, create_canvas, None, '14o', 3)

    def test_create_canvas_wrong_correct(self):
        self.assertEqual(create_canvas(None, 3, 2), [
            ['-', '-', '-', '-', '-', ],
            ['|', ' ', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', ],
        ])
        self.assertEqual(create_canvas([], 11, 4), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_draw_rectangle_wrong_params(self):
        self.assertRaises(TypeError, draw_rectangle, list, 1, 2, 3, 4)
        self.assertRaises(TypeError, draw_rectangle, dict, 1, 2, 3, 4)

        self.assertRaises(ValueError, draw_rectangle, [[]], str(), '2', '3', '4')
        self.assertRaises(ValueError, draw_rectangle, [[]], 1, '2', '34*5', '4')

    def test_draw_rectangle_correct_1(self):
        self.assertEqual(draw_rectangle(self.canvas, 1, 1, 4, 4), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_draw_rectangle_correct_2(self):
        self.assertEqual(draw_rectangle(self.canvas, '1', '1', '2', '2'), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_draw_rectangle_correct_3(self):
        self.assertIsNone(draw_rectangle(None, 1, 2, 3, 4))
        self.assertIsNone(draw_rectangle(None, '4', '3', '2', '1'))

    def test_draw_line_wrong_params(self):
        self.assertRaises(TypeError, draw_line, False, 1, 2, 1, 4)
        self.assertRaises(TypeError, draw_line, [], '1', 2, '1', None)

        self.assertRaises(ValueError, draw_line, [], 1, 2, '#1', 4.)
        self.assertRaises(ValueError, draw_line, [], '1', '2', '1', '4.')

    def test_draw_line_correct_1(self):
        self.assertEqual(draw_line(self.canvas, 1, 1, 1, 4), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_draw_line_correct_2(self):
        self.assertEqual(draw_line(self.canvas, 1, 1, 4, 1), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_draw_line_correct_3(self):
        self.assertIsNone(draw_line(None, 1, 2, 1, 4))
        self.assertIsNone(draw_line(None, '1', '2', '1', '4'))

    def test_brush_wrong_params(self):
        self.assertRaises(TypeError, brush, False, 3, 4, 2)
        self.assertRaises(TypeError, brush, type, 1, '2', 'b')

        self.assertRaises(IndexError, brush, self.canvas, -15, 2, 'c')
        self.assertRaises(IndexError, brush, self.canvas, 5, -22, 'c')

        self.assertRaises(ValueError, brush, self.canvas, '1', '.2', 'c')
        self.assertRaises(ValueError, brush, self.canvas, '1.', 2, 'd')

    def test_brush_correct_1(self):
        self.assertEqual(brush(self.canvas, 1, 1, 'b'), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x', ' ', ' ', '|', ],
            ['|', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x', ' ', ' ', '|', ],
            ['|', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x', ' ', ' ', '|', ],
            ['|', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'x', ' ', ' ', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_brush_correct_2(self):
        self.assertEqual(brush(self.canvas, 10, 1, 'b'), [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'b', 'b', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'b', 'b', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'b', 'b', '|', ],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'b', 'b', '|', ],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ],
        ])

    def test_brush_correct_3(self):
        self.assertIsNone(brush(None, 1, 1, 'b'))
        self.assertIsNone(brush(None, '10', '1', 'b'))

    def test_main_io(self):
        with patch('builtins.open') as fout:
            fout().__enter__().readlines.return_value = ['C 20 4',
                                                         'L 1 2 6 2',
                                                         'L 6 3 6 4',
                                                         'R 16 1 20 3',
                                                         'B 10 3 o']
            main()

        fout.assert_has_calls(
            [call(INPUT_FILE), call(OUTPUT_FILE, 'w'), call(OUTPUT_FILE, 'a')],
            any_order=True,
        )


if __name__ == '__main__':
    unittest.main()
