import csv
import os
from operator import truediv
from subprocess import Popen
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import RemoteController

from plotter import gu
from calculate_alpha import calculate_alpha
from visualize_network import visualize_net

import numpy as np
import time

def run(m,n):
    net = Mininet(controller=RemoteController)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    i = 0

    hosts = []
    Nodes = []
    attacked_host = None
    attacked_switch = None
    print("adding main resource")
    host_main = net.addHost("Main")

    # print("adding main switch")
    switch_main = net.addSwitch(f's{i}', protocols='OpenFlow13')
    i = i + 1
    print("adding link ",switch_main," - ",host_main)
    net.addLink(switch_main, host_main)

    # host_name = f'attacker'
    # attacker = net.addHost(host_name)
    # print("adding link ",switch_main," - ",attacker)
    # iface = net.addLink(switch_main, attacker)

    for j in range(0,n):
        switch = net.addSwitch(f's{i}', protocols='OpenFlow13')
        i = i + 1
        print(f"adding path {j+1} and linking ",switch_main," - ",switch)
        net.addLink(switch_main, switch)
        Nodes.append(switch)

    for host_id in range(0,m):
        if len(ParentNodes[host_id].nodes) > 1:

            switch = net.addSwitch(f's{i}', protocols='OpenFlow13')
            i = i + 1
            for j in ParentNodes[host_id].nodes:
                print("adding link ",switch," - ",Nodes[j])
                net.addLink(switch, Nodes[j])
            host_name = f'h{host_id}'
            if attacked_host is None:
                attacked_host = net.addHost(host_name)
                hosts.append(attacked_host)
                print("adding link ",switch," - ",attacked_host)
                net.addLink(switch, attacked_host)
                attacked_switch = switch

                print("adding attacker")
                host_name = f'attacker'
                attacker = net.addHost(host_name)
                print("adding link ",switch," - ",attacker)
                iface = net.addLink(switch, attacker)
            else:
                host = net.addHost(host_name)
                hosts.append(host)
                print("adding link ",switch," - ",host)
                net.addLink(switch, host)

    for j in range(0,n):
        node_has_resources = False
        for k in range(0,len(ChildResources[j].resources)):
            print(f"Working on child resource {ChildResources[j].resources[k]} of alpha {ChildResources[j].alphas[k]}")
            if ChildResources[j].alphas[k] == 1:
                host_id = ChildResources[j].resources[k]
                print("adding resource ",host_id)
                if not node_has_resources:
                    node_has_resources = True
                    switch = net.addSwitch(f's{i}', protocols='OpenFlow13')
                    i = i + 1
                    print("adding link ",switch," - ",Nodes[j])
                    net.addLink(switch, Nodes[j])

                host_name = f'h{host_id}'
                host = net.addHost(host_name)
                hosts.append(host)
                print("adding link ",switch," - ",host)
                net.addLink(switch, host)
                # print("adding link ",switches[j]," - ",host)
                # net.addLink(switches[j], host)

    net.start()
    visualize_net(net,n)
    if attacked_host is not None:
        # attacker.cmd("xterm &")
        attacked_host_ip = attacked_host.IP()
        print(f"the IP of {attacked_host} is: {attacked_host_ip}")
    text = input("Enter A to attack else the network will continue without attacking\n")

    file_name = "../tmp.txt"
    if text == "a" or text == "A":
        if attacked_host is not None:
            print('[*] Monitoring\n')
            cmd = f"bwm-ng -o csv -T rate -C ',' > '{file_name}' &"
            Popen(cmd, shell=True).wait()
            # time.sleep(10)
            attack_time = 5

            print("\n[*] Starting HTTP server on ", attacked_host," (simulates service under attack)...")
            attacked_host.cmd('python3 -m http.server 80 &')

            print(f"\n[*] Starting DoS attack from attacker to {attacked_host} with IP {attacked_host_ip}...")
            attacker.cmd(f'hping3 {attacked_host_ip} -S --flood -V &')
            print(f'hping3 {attacked_host_ip} -S --flood -V &')


            # attacked_switch_ip = attacked_switch.IP()
            # print("[*] Starting DoS attack to switch ...")
            # IP_src = "10.0.{}.{}"
            # attacker.cmd(f"""python3 -c "
            # from scapy.all import IP, send
            # import time
            # start = time.time()
            # while time.time() - start < {attack_time}:
            #     for i in range(50):
            #         pkt = IP(src='{IP_src}'.format(i%255, i%255), dst='{attacked_switch_ip}')/'X'*100
            #         send(pkt, iface='{iface}', verbose=0)
            # " &""")


            print("\n[*] Sending legitimate traffic from ", host_main," to ", attacked_host," and measuring packet loss...")
            result = host_main.cmd(f'ping -c 10 {attacked_host_ip}')
            print("\n=== Ping Results (", host_main," → ", attacked_host,") During Attack ===\n")
            print(result)

            time.sleep(attack_time)
            # host_main.cmd('pkill python3')

            # print("[*] Killing any lingering attack processes...")
            # attacker.cmd('pkill -f scapy')

            print("\n[*] Stopping attack...")
            attacker.cmd('pkill hping3')

            wait_time = 10
            print(f"\n[*] running for {wait_time} seconds without attack...")
            time.sleep(wait_time)

            data = {}
            print('[*] Stop Monitoring\n')
            with open(file_name) as csvf:
                csvr = csv.reader(csvf, delimiter=',')
                for row in csvr:
                    key = row[1]
                    tme = float(row[0])
                    load = float(row[4]) * 8
                    if key in data:
                        data[key]['time'].append(tme)
                        data[key]['load'].append(load)
                    else:
                        data[key] = {}
                        data[key]['time'] = []
                        data[key]['load'] = []
            cmd = "killall bwm-ng"
            Popen(cmd, shell=True).wait()
            # if os.path.exists(file_name):
            #     os.remove(file_name)
            print('[*] Plotting results\n')
            gui(data)
        else:
            print("[*] No host to attack.")
    else:
        if text == "t" or text == "T":
            data = {}
            with open(file_name) as csvf:
                csvr = csv.reader(csvf, delimiter=',')
                for row in csvr:
                    key = row[1]
                    tme = float(row[0])
                    load = float(row[4]) * 8
                    if key in data:
                        data[key]['time'].append(tme)
                        data[key]['load'].append(load)
                    else:
                        data[key] = {}
                        data[key]['time'] = []
                        data[key]['load'] = []
            print('[*] Plotting results\n')
            gui(data)

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    m = 20
    n = 6
    random_array = np.random.randint(1, 10, size=m)
    R = np.sort(random_array)[::-1]
    print(R)
    alpha,ParentNodes,ChildResources = calculate_alpha(R,m,n)
    print(alpha)

    run(m,n)
