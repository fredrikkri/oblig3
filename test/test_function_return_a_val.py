from src.main import is_leapyear

def test_function_returns_a_value():
    print("En verdi blir sendt tilbake fra funksjonen")
    assert is_leapyear(year=1701) != None
