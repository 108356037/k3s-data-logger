#!/bin/bash
sudo swapoff -a
vlanip=$(ifconfig | grep 192.168 | cut --delimiter=' ' --fields=10)
# sudo k3s server --node-external-ip $vlanip --node-ip $vlanip --write-kubeconfig-mode 644 &
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --node-external-ip ${vlanip} --node-ip ${vlanip} --write-kubeconfig-mode 644" sh -s - --docker
sleep 2m
token=$(sudo cat /var/lib/rancher/k3s/server/node-token)
####label edge as worker
k3s kubectl label nodes jetsonv1-desktop kubernetes.io/role=worker

#########this is for worker node
#curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent --token ${vlanip} --server ${vlanip}:6443" sh -s -
curl -sfL https://get.k3s.io | K3S_URL="https://${vlanip}:6443" K3S_TOKEN=${token}  sh -s - --docker
