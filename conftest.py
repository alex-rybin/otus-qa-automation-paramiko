import paramiko
import pytest
from envparse import env

env.read_envfile()

HOST = env.str('REMOTE_HOST')
USER = env.str('REMOTE_USER')
PASSWORD = env.str('REMOTE_PASSWORD')


@pytest.fixture(scope='session')
def ssh_connection():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST, username=USER, password=PASSWORD, port=22)

    yield client

    client.close()
