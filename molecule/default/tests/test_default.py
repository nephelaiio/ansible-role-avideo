def test_php(host):
    assert host.command('php --version').rc == 0
