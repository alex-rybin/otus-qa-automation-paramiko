def test_ssh_running(ssh_connection):
    stdin, stdout, stderr = ssh_connection.exec_command('service --status-all')
    data = stdout.read().decode('utf-8').split('\n')
    assert ' [ + ]  ssh' in data


def test_folders_correct(ssh_connection):
    stdin, stdout, stderr = ssh_connection.exec_command('ls /')
    data = stdout.read().decode('utf-8').split('\n')
    essential_folders = [
        'bin',
        'boot',
        'dev',
        'etc',
        'home',
        'lib',
        'lost+found',
        'media',
        'mnt',
        'opt',
        'proc',
        'root',
        'run',
        'sbin',
        'srv',
        'tmp',
        'usr',
        'var',
    ]
    assert all(folder in data for folder in essential_folders)
