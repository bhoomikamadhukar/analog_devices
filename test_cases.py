import io
import unittest
from contextlib import redirect_stdout

import main
from main import count_lines, get_all_files


class TestDirectory(unittest.TestCase):
    def test_count_lines(self):
        lines = count_lines('/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/t1.txt')
        self.assertEqual(lines, 7)

    def test_incorrect_file(self):
        lines = count_lines('/Users/madhukar/PycharmProjects/CodeTest/test_folder/t1.txt')
        self.assertEqual(lines, "File not found")

    def test_for_invalid(self):
        f = io.StringIO()
        with redirect_stdout(f):
            main.get_all_files('/Users/bm/PycharmProjects/CodeTest/test_folder/')
        self.assertRegex(f.getvalue(), "Invalid directory")

    def test_for_working(self):
        f = io.StringIO()
        with redirect_stdout(f):
            main.get_all_files('/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/')
        self.assertRegex(f.getvalue(), "/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/t1.txt:  "
                                       "7\n/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/h.txt:  "
                                       "0\n/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/another_sub"
                                       "/hey.txt:  "
                                       "1\n/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/sub_directory"
                                       "/t2.txt:  0\n----------------------------------------\nNumber of files found: "
                                       "  4\nTotal Number of lines:8\nAverage lines per file:2.0\n")

    def test_for_none(self):
        f = io.StringIO()
        with redirect_stdout(f):
            main.get_all_files('/Users/bhoomikamadhukar/PycharmProjects/CodeTest/example/')
        self.assertRegex(f.getvalue(), "This directory does not have files to count lines")

    def test_for_average(self):
        f = io.StringIO()
        with redirect_stdout(f):
            main.get_all_files('/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/sub_directory/')
        self.assertRegex(f.getvalue(),
                         '/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/sub_directory/t2.txt:  '
                         '0\n----------------------------------------\nNumber of files found:   1\nTotal Number of '
                         'lines:0\nAverage lines per file is 0\n')

unittest.main()
