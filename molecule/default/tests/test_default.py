import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
    ("/etc/hosts_test", "8.8.8.8"),
    ("/etc/hosts_test", "test_host"),
    ("/etc/hosts_test", "test_alias"),

])
def test_files(host, file, content):
    file = host.file(file)
    assert file.exists
    assert file.contains(content)
