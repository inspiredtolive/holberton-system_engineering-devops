# Configures SSH client to use the private key.

file_line { 'Disables password-based authentication':
    ensure => 'present',
      path => '/etc/ssh/ssh_config',
      line => '	PasswordAuthentication no',
    match  => 'PasswordAuthentication yes',
}

file_line { 'Configures private key authentication':
    ensure => 'present',
      path => '/etc/ssh/ssh_config',
      line => '	IdentityFile ~/.ssh/holberton',
