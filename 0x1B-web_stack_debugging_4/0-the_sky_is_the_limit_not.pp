# Fixing the max read of an Nginx server

exec { 'Install_Stuff':
  command => 'sed -i \'5c ULIMIT="-n 10000"\' /etc/default/nginx && sudo service nginx restart',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
