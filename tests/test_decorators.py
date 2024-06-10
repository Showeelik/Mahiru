import pytest
import os
from decorators import log

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
