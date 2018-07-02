import socket
from time import sleep
from unittest.mock import patch

import pytest

from ..util import resolve


@pytest.fixture
def gethostbyname_mock():
    with patch('hostres.util.gethostbyname') as m:
        yield m


def test_resolve(gethostbyname_mock):

    def side_effect(hostname, queue):
        queue.put('1.2.3.4')
    gethostbyname_mock.side_effect = side_effect

    out = resolve('hostname')

    assert out == '1.2.3.4'


def test_resolve_oserror(gethostbyname_mock):
    gethostbyname_mock.side_effect = socket.error('BOOM!')

    out = resolve('hostname')

    assert out == 'hostname'


def test_resolve_timeout(gethostbyname_mock):

    def side_effect(hostname, queue):
        sleep(2)
        queue.put('1.2.3.4')  # will be ignored
    gethostbyname_mock.side_effect = side_effect

    out = resolve('hostname', 0.1)

    assert out == 'hostname'
