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
 - Modified files / their locations: Modified haproxy.cfg in /etc/haproxy
 - Configurations set: Please look at the haproxy.cfg file included, but to summarize, the global settings are standard, where the maxconn (max connections) is set to 50,000, and the user and group are set to haproxy. In defaults, the timeout connect is every 10 seconds, the timeout for the client and server is every 30 seconds, the mode is set to tcp, and the option is set to tcplog. The maxconn per server is 3,000. In the frontend, there is a bind to the private IP address of my proxy to port 80, and the default backend is set to back_end. In the backend, the balance is set to roundrobin, and the servers are set to the webServ1Host and webServ2Host I created.
 - How to restart the service after a configuration change: sudo systemctl restart haproxy.service
 - Resources used: haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/ and class lectures

4. Webserver 1 & 2 configuration & documentation requirements
 - How to install package: Use the command "apt-get install -y packageName" (insert the name of the package where "packageName is) to install a package.
 - Modified files / their locations: Modified index.html in /var/www/html in both webServ1Host and webServ2Host.
 - Configurations set: I changed each file to hold the contents of the "index.srv1.html" and "index.srv2.html", respectively. (If this is not a configuration, no other configurations were set for the sites to work.)
 - How to restart the service after a configuration change: I assume the command reboot for the webservers, but I did not have to restart the service for the change in my website to take effect.
 - Resources used: linuxshelltips.com/install-apache-in-linux/ (to find how to implement a html file for a visible web page) and class lectures

5. Two screenshots:
 - Content from "server 1":
![Server-1](https://user-images.githubusercontent.com/77339445/141179071-6df01725-bcbd-41fa-a8f3-8c8bda47f7db.png)
 - Content from "server 2":
![Server-2](https://user-images.githubusercontent.com/77339445/141179094-2e0a19e3-cade-4982-9893-58efb1b201bf.png)

6. This is optional (not including it since I am deleting the stack once testing / documentation is complete).
