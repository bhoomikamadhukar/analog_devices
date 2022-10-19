"""
Provides line count.
"""

from glob import glob
import os


def count_lines(filename):
    """
    A function to count number of lines in a file.
    :param filename: Path of the file
    :return: Line count
    """
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as file:
            line_count = len(file.readlines())
        return line_count

    return "File not found"


def get_all_files(directory, extension=".txt"):
    """
    A function to explore a directory structure searching for files with the given extension.
    :param directory: This is the required argument of the name of the directory
    :param extension: This is an optional argument that defaults to text files
    :return: total number of files, line count and average line count
    """

    if os.path.isdir(directory):
        path = directory + '**' + '/*' + extension
        files = glob(path, recursive=True)
        if files:
            count = []
            for file in files:
                count.append(count_lines(file))
            file_count = list(zip(*(files, count)))
            for file_path, line_count in file_count:
                print(f"{file_path}:  {line_count}")
            print("----------------------------------------")
            print(f"Number of files found:   {len(files)}")
            print(f"Total Number of lines:{sum(count)}")
            if all(v == 0 for v in count):
                print("Average lines per file is 0")
            else:
                print(f"Average lines per file:{sum(count) / len(count)}")

        else:
            print("This directory does not have files to count lines")
    else:
        print("Invalid directory")


if __name__ == "__main__":
    get_all_files('/Users/bhoomikamadhukar/PycharmProjects/CodeTest/test_folder/')
