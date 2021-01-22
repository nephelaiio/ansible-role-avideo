def test_frontpage(host):
    cmd = 'curl -s http://localhost:8080 | grep this_is_a_test'
    assert host.command(cmd).rc == 0
