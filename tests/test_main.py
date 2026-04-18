import pytest

def sort_sentences(sentences):
    return sorted(sentences, key=lambda sentence: len(sentence.split()))

def test_sort_sentences():
    sentences = ["hello world", "this is a test", "python is fun"]
    expected = ["hello world", "python is fun", "this is a test"]
    assert sort_sentences(sentences) == expected

def test_sort_sentences_empty_list():
    sentences = []
    expected = []
    assert sort_sentences(sentences) == expected

def test_sort_sentences_single_element():
    sentences = ["hello world"]
    expected = ["hello world"]
    assert sort_sentences(sentences) == expected

def test_sort_sentences_equal_length():
    sentences = ["hello world", "foo bar"]
    expected = ["foo bar", "hello world"]
    assert sort_sentences(sentences) == expected
