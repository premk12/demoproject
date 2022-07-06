import pytest
@pytest.fixture()
def setup():
    print("Get driver")
    print("Maximize window")
    print("print title")
    print("close window")


def test_1(setup):

    print("Get facebook.com or open url")

def test_2():

    print("Get amazon.com or open url")


def test_3():

    print("Get gmail.com or open url")
