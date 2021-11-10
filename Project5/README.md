README.md Documentation - Part 2
---
1. Configured file by using the command "sudo vim /etc/hosts". At the bottom of the file, entered the private IP address of each instance followed by the hostname of the instance. Here is an example for what the webServ2Host /etc/hosts file looked like:

10.0.0.8 proxy

127.0.0.1 proxy

10.0.0.31 webServ1Host

10.0.0.32 webServ2Host

2. SSH into systems using private IPs by first in .ssh creating a folder called "ceg3120-aws-vm.pem" and inserting the private key. Then use "chmod 400 ceg3120-aws-vm.pem" to keep the private key private. Now you can use a command such as "ssh -i .ssh/ceg3120-aws-vm.pem ubuntu@webServ1Host" to toggle between instances using the private IP addresses stored in /etc/hosts.
3. HAProxy Configuration & Documentation Requirements:
 - How to install package: Use the command "apt-get install -y packageName" (insert name of package where "packageName" is) to install a package.
