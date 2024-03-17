import pytest

# Регистрируем новые метки в Pytest
def pytest_configure(config):
    config.addinivalue_line("markers", "critical: Marks a test as critical.")
    config.addinivalue_line("markers", "medium: Marks a test as medium.")
