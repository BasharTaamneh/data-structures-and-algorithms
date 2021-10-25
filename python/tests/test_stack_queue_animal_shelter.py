from linked_list.stack_queue_animal_shelter.stack_queue_animal_shelter import Cat, Dog, Anypit, AnimalShelter
import pytest


def test_importin():
    assert Cat('')
    assert Dog('')
    assert Anypit('')
    assert AnimalShelter()


def test_AnimalShelter_is_empty():
    shilter = AnimalShelter()
    with pytest.raises(Exception):
        actual = shilter.dequeue("")
        expected = "AnimalShelter is empty."
        assert actual == expected


def test_AnimalShelter_enqueue_anipt_ether_dog_or_cat():
    shilter = AnimalShelter()
    anypit = Anypit("paired")
    actual = shilter.enqueue(anypit)
    expected = False
    assert actual == expected


def test_AnimalShelter_enqueue_cat():
    shilter = AnimalShelter()
    anypit = Anypit("paired")
    actual = shilter.enqueue(anypit)
    expected = False
    assert actual == expected
