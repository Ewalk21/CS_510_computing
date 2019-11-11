import fib

def test_fib():
    result  = fib.main(10)
    correct = 55
    assert result == correct
