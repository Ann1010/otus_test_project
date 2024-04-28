import logging
import os
import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action='store', default='https://petstore.swagger.io/v2/')
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture(scope='session', autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='session', autouse=True)
def logger_test(request):
    logger = logging.getLogger('testing')
    log_level = request.config.getoption("--log_level")
    os.makedirs('logs', exist_ok=True)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    return logger
