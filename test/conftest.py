import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nThe function named 'is_leapyear()'is running...")
