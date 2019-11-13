import os
import pdftotext
from collections import namedtuple


from docx import Document

Similarity = namedtuple('Similarity', 'rate')


def doc_to_text(filename):
    return '\n'.join(
        x.text for x in
        Document(filename).paragraphs
        if x.text
    )


def pdf_to_text(filename):
    with open(filename, 'rb') as f:
        pdf = pdftotext.PDF(f)

    return '\n'.join(pdf)


def file_to_str(file_path):
    file_extension = os.path.splitext(file_path)[1]

    PARSERS = {
        '.pdf': pdf_to_text,
        '.docx': doc_to_text,
    }
    parse_func = PARSERS.get(file_extension)
    if not parse_func:
        raise ValueError('Only .docx and .pdf parsing is supported. Convert them before using the tool')

    return parse_func(file_path)


def compare_docs(file, basefile):
    """Compares two documents and output a similarity index that goes from 0 to 100"""
    input_text = file_to_str(file)
    baseline_text = file_to_str(basefile)  # To improve efficiency we could store the text content by filename key

    if input_text.strip() == baseline_text.strip():
        return Similarity(100)

    # Split into list of sentences
    # Transform each sentence to stem
    # Compare content with each of our corpus files. (For the demo it could be just one test file)
    # If anyone is greater than say.. 80%, show it as plagio.
