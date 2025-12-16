#!/usr/bin/env python3
import pytest
import sys

if __name__ == "__main__":
    # Запуск всех тестов
    print("Running all tests...")
    result = pytest.main(["-v", "tests/"])
    sys.exit(result)