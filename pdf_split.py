#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Use PyPDF2 to split a pdf file into individual sections.

This script assumes that you have python3, the python3-magic and python3-pypdf2
modules installed.

Accept a pdf file as input and split it into individual pdf files containing
each part, using section names and page number boundaries defined by the user.

There must be a file with the same name as the source pdf file with the file
extension ".csv" in the same directory as the source file, eg: a source file
named Book.pdf needs a corresponding ".csv" file named Book.csv. The
".csv" file should contain the name of each section with the first and last
pages of that section in the following format:

Chapter-1,1,20
Chapter-2,21,45
Chapter-3,46,75
Glossary,76,80
"""


from os import path
import csv
import sys

from magic import from_file
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_split(pdf_source_file):
    """Use PyPDF2 to split a pdf file into individual parts."""
    if not path.isfile(pdf_source_file):
        sys.exit(f"The pdf file {pdf_source_file} does not exist!")

    file_type = from_file(pdf_source_file)
    if "PDF document" not in file_type:
        sys.exit(f"The file {pdf_source_file} is not a valid pdf file!")

    pages_file = f"{path.splitext(path.basename(pdf_source_file))[0]}.csv"
    if not path.isfile(pages_file):
        sys.exit(f"The pages file {pages_file} does not exist!")

    print(f"Splitting pdf file: {pdf_source_file}")

    with open(pages_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            pdf_destination_file = row[0]
            first_page = int(row[1])
            last_page = int(row[2])

            if path.isfile(pdf_destination_file):
                print(f"The pdf file {pdf_destination_file} already exists.")
                continue

            print(
                f"Splitting pages {first_page} to {last_page} into file: {pdf_destination_file}"
            )

            with open(pdf_source_file, "rb") as input_file:
                pdf_reader = PdfFileReader(input_file)
                output_pdf = PdfFileWriter()

                for page_num in range(first_page - 1, last_page):
                    output_pdf.addPage(pdf_reader.getPage(page_num))

                with open(f"{pdf_destination_file}.pdf", "wb") as output_file:
                    output_pdf.write(output_file)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        pdf_split(sys.argv[1])
