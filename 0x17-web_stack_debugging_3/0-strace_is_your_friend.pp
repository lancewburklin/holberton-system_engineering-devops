# Renames a file to get a server up and running
exec { 'rename':
  path    => '/var/www/html/wp-includes',
  command => 'mv class-wp-locale.php class-wp-locale.phpp',
}
