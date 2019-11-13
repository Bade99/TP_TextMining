# -*- coding: utf-8 -*-

from functools import partial
from os.path import join, dirname, abspath

from similarity.parser import compare_docs, Similarity

get_dset = partial(join, dirname(abspath(__file__)), 'data')


def test_same_file_is_equal():
    file_path = get_dset('Economía de experiencia.pdf')
    assert compare_docs(file_path, file_path) == Similarity(100)
