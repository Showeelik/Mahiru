import pytest
import os
from src.decorators import log, retry, unstable_function
from unittest.mock import patch, call


def test_log_to_file():

    @log(filename="testlog.txt")
    def sample_function(x, y):
        return x + y
    
    result = sample_function(1, 2)
    assert result == 3

    with open("testlog.txt", "r") as file:
        lines = file.readlines()
    
    assert len(lines) == 1
    assert "sample_function ok" in lines[0]
    
    os.remove("testlog.txt")

def test_log_error_to_file():

    @log(filename="errorlog.txt")
    def error_function(x, y):
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        error_function(1, 2)

    with open("errorlog.txt", "r") as file:
        lines = file.readlines()
    
    assert len(lines) == 1
    assert "error_function error: ValueError. Inputs: (1, 2), {}" in lines[0]
    
    os.remove("errorlog.txt")

def test_log_to_console(capsys):

    @log()
    def console_function(x, y):
        return x * y

    result = console_function(2, 3)
    assert result == 6

    captured = capsys.readouterr()
    assert "console_function ok" in captured.out

def test_log_error_to_console(capsys):
    
    @log()
    def console_error_function(x, y):
        raise IndexError("Console test error")

    with pytest.raises(IndexError, match="Console test error"):
        console_error_function(2, 3)
    
    captured = capsys.readouterr()
    assert "console_error_function error: IndexError. Inputs: (2, 3), {}" in captured.out



@pytest.fixture
def decorated_unstable_function():
    return retry(max_attempts=5)

def test_retry_success_after_failures(decorated_unstable_function):
    with patch('decorators.unstable_function', side_effect=[ConnectionError, ConnectionError, 'Success!']) as mock_func:
        decorated_func = decorated_unstable_function(mock_func)
        result = decorated_func()
        assert result == 'Success!'
        assert mock_func.call_count == 3

def test_retry_exceeds_max_retries(decorated_unstable_function):
    with patch('decorators.unstable_function', side_effect=ConnectionError) as mock_func:
        decorated_func = decorated_unstable_function(mock_func)
        with pytest.raises(ConnectionError):
            decorated_func()
        assert mock_func.call_count == 5

def test_retry_waits_between_attempts(decorated_unstable_function):
    with patch('decorators.unstable_function', side_effect=ConnectionError) as mock_func, \
         patch('time.sleep', return_value=None) as sleep_mock:
        decorated_func = decorated_unstable_function(mock_func)
        with pytest.raises(ConnectionError):
            decorated_func()
        assert mock_func.call_count == 5
        assert sleep_mock.call_count == 5
        sleep_mock.assert_has_calls([call(1), call(1), call(1), call(1)])