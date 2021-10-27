Ten Modifications required for credit:
---
These are the steps I took in trying to complete all 10 modifications properly (notes for partial credit):
1. Changed the description of the template by going to the first "Description:" heading and putting my own description.
2. Replaced the AMI by going under "AWSRegionUbuntu", then changing the "HVM64" ami to the ami of "Ubuntu Server 20.04 LTS (HVM), SSD Volume Type", which is listed from finding it via "Launch Instances" and searching "Ubuntu" when in "Step 1: Choose an Amazon Machine Image (AMI)".
3. Made the VPC range 10.0.0.0/16 by going under "Resources:", under "VPC:", then after "CidrBlock:" I put "10.0.0.0/16".
4. Made the subnet range 10.0.0.0/24 by going under "Resources:", under "Subnet", then after "CiderBlock:" I put "10.0.0.0/24".
5. For the security group setting for inbound SSH within VPC, under "SecurityGroupIngress" I put the IpProtocol as tcp, the FromPort and ToPort as 22, and the CidrIp as 10.0.0.0/16.
6. For the security group setting for inbound SSH from home / trusted network(s), under "SecurityGroupIngress" I put the IpProtocol as tcp, the FromPort and ToPort as 22, and the CidrIp as 174.97.124/32 (which is my home IP address cidr notation).
7. For the security group setting for inbound SSH from WSU, under "SecurityGroupIngress", I put the IpProtocol as tcp, the FromPort and ToPort as 22, and the CidrIp as 130.108.0.0/16.
8. For making the instance setting to set "Tag" "Name" to "CF-instance", I went under "PublicUbuntuInstance:", then under "Tags", and under "Key: Name", I set the "Value:" to "CF-instance".
9. For an instance setting to set a private IP in your subnet range, under "PublicUbuntuInstance" I set the PrivateIpAddress to "10.0.0.25", since that is withing the subnet cidr range of "10.0.0.0/25".
10. To make the cf-template script install git, python3, and pip3, I went under "Fn::Base64:" and added the command line "apt-get install -y git python3 pip3", and for the cf-template to change the hostname, I added the command line "sudo hostname wright-AMI" under "Fn::Base64".

I would love specific corrections on what I was missing / how to get the stack to fully work! I ran into the error "Encountered unspported property Id", which was occurring from the "UbuntuIPAddress" heading, and did not know how to fix it. I think I did not understand something with modification 9 specifically, but I put what I did for each modification so you could see what I thought the instruction wanted me to do / to get credit for the modifications I did correctly or somewhat correctly.
