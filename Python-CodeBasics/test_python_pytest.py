import python_pytest
def test_sum():
    total = python_pytest.sum(4,5)
    assert total == 9

def tes_mul():
    result = python_pytest.mul(4,5)    
    assert result == 20

# to run the pytest use py.test or python -m pytest 
# try and use test_ perfix for funtions in  test file and also for the name of the file where you write the test code.