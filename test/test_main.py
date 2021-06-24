import main

def test_startApp():
    assert main.startApp() == "Welcome to Matrix calculator!"
    
def test_endApp():
    assert main.endApp == "Thank you for using Matrix calculator!"