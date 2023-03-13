#maybe
import pytest
from logger import TestsLogger

log = TestsLogger.log


def test_dummytest_1(record_property):
    """Test if x = 1"""
    x = 1
    record_property('x', 1)
    record_property('expected', 1)
    assert x == 1


def test_dummytest_3():
    """Test if x = 1"""
    x = 1
    log.debug("hello stranger")
    assert x == 1
