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


def test_AnimalShelter_dequeue_enqueue_cat():
    shilter = AnimalShelter()
    cat1 = Cat("citty")
    shilter.enqueue(cat1)
    actual = shilter.dequeue("cat")
    expected = "citty"
    assert actual == expected


def test_AnimalShelter_dequeue_enqueue_multiable_cat():
    shilter = AnimalShelter()
    cat1 = Cat("citty")
    cat2 = Cat("shiry")
    cat3 = Cat("pee")
    shilter.enqueue(cat1)
    shilter.enqueue(cat2)
    shilter.enqueue(cat3)
    actual_1 = shilter.dequeue("cat")
    actual_2 = shilter.dequeue("cat")
    expected_1 = "citty"
    expected_2 = "shiry"
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_AnimalShelter_dequeue_enqueue_dog():
    shilter = AnimalShelter()
    dog1 = Dog("rock")
    shilter.enqueue(dog1)
    actual = shilter.dequeue("dog")
    expected = "rock"
    assert actual == expected


def test_AnimalShelter_dequeue_enqueue_multiable_dog():
    shilter = AnimalShelter()
    dog1 = Dog("rock")
    dog2 = Dog("zoodka")
    dog3 = Dog("vally")
    shilter.enqueue(dog1)
    shilter.enqueue(dog2)
    shilter.enqueue(dog3)
    actual_1 = shilter.dequeue("dog")
    actual_2 = shilter.dequeue("dog")
    expected_1 = "rock"
    expected_2 = "zoodka"
    assert actual_1 == expected_1
    assert actual_2 == expected_2
