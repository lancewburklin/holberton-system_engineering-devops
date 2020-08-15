# custom HTTP header response
package {'haproxy':
    ensure  => installed,
    version => '1.6.3',
}
exec {'wget':
    provider => 'shell',
    command  => 'wget https://raw.githubusercontent.com/lancewburklin/holberton-system_engineering-devops/master/0x0F-load_balancer/1-install_load_balancer && chmod +x 1-install_load_balancer && sudo ./1-install_load_balancer',
}
