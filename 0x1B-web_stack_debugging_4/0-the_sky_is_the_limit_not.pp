# increase ulimit and reload nginx
exec { 'increase ulimit':
  path    => '/bin',
  command => "sed -i 's/15/4096/g' /etc/default/nginx"
}

exec { 'nginx reload':
  path    => '/usr/sbin',
  command => 'service nginx reload'
}
