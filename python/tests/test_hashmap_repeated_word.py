from  hashmap_repeated_word.hashmap_repeated_word import HashTable
import pytest

@pytest.fixture
def hashmap():
    hashtable = HashTable()

    hashtable.add(
        'A', "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")

    hashtable.add(
        'B', "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")

    hashtable.add('C', "Once upon a time, there was a brave princess who...")

    return hashtable


# def test_repeated_word_with_existin_string_in_hashtable_1(hashmap):
#     expected = "A"
#     actual = hashmap.repeated_word(
#         "Once upon a time, there was a brave princess who...")
#     assert actual == expected


def test_repeated_word_with_existin_string_in_hashtable_2(hashmap):
    expected = 'Summer'
    actual = hashmap.repeated_word(
        "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert actual == expected


def test_repeated_word_with_existin_string_in_hashtable_3(hashmap):
    expected = 'It'
    actual = hashmap.repeated_word(
        "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert actual == expected


def test_repeated_word_with_multiabl_existing_string_in_hashtable(hashmap):
    expected_1 = 'A'
    expected_2 = 'Summer'
    actual_1 = hashmap.repeated_word(
        "Once upon a time, there was a brave princess who...")
    actual_2 = hashmap.repeated_word(
        "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_repeated_word_with_no_existin_string_in_hashtable(hashmap):
    expected = "this is not an existing string --> No matched data"
    actual = hashmap.repeated_word(
        "Once upon a time,")
    assert actual == expected
