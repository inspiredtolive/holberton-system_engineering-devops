# Fixes typos in wp-settings.php
exec {'phpp':
  path    => '/bin',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
