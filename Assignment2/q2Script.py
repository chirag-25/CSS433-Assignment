#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    r1 = net.addSwitch('r1', cls=OVSKernelSwitch)
    r2 = net.addSwitch('r2', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    A = net.addHost('A', cls=Host, ip='10.0.0.1', defaultRoute=None)
    B = net.addHost('B', cls=Host, ip='10.0.0.2', defaultRoute=None)
    C = net.addHost('C', cls=Host, ip='10.0.0.3', defaultRoute=None)
    D = net.addHost('D', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')
    Ar1 = {'bw':1000,'delay':'1ms'}
    net.addLink(A, r1, cls=TCLink , **Ar1)
    r1D = {'bw':1000,'delay':'1ms'}
    net.addLink(r1, D, cls=TCLink , **r1D)
    r1r2 = {'bw':500,'delay':'10ms'}
    net.addLink(r1, r2, cls=TCLink , **r1r2)
    r2C = {'bw':1000,'delay':'5ms'}
    net.addLink(r2, C, cls=TCLink , **r2C)
    r2B = {'bw':1000,'delay':'1ms'}
    net.addLink(r2, B, cls=TCLink , **r2B)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('r1').start([c0])
    net.get('r2').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

