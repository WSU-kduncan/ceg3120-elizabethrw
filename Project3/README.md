Part 1 - Build a VPC
---
1. VPC's role: VPC stands for Virtual Private Cloud. It is private cloud hosted within a public cloud, and it is used as a virtual network that is isolated from other public cloud users (to do things such as store data, host a website, etc.). Image to show VPC has been created and configured:

2. Subnet's role: A subnet specifies a range of IP addresses in the VPC I made. Public subnets are used for resources that are connected to the internet (aka the resources are public), and private subnets are for resources that should not be connected to the internet (aka the resources are private). Image to show a subnet has been created and configured:

3. Internet gateway's role: A gateway creates a way for communication to occur between the resources in my VPC and the internet. Image to show a gateway has been created and configured:

4. Route table's role: A route table dictates where network traffic is allowed to be directed via the rules I specify (which are the routes I choose to include on the route table). Image to show a route table has been created and configured:

5. Security group's role: Acts as a network firewall by specifying what users are allowed (and therefore clarifies that all other users are not allowed) to connect to my VPC. Image to show a security group has been created and configured:

Part 2 - EC2 Instances
---
1. AMI selected: Ubuntu Server 20.04 LTS (HVM), SSD Volute Type
 - Default username of the instance type selected: ubuntu
 - Instance type selected: t2.micro
2. How I attached the instance to my VPC: In "Step 3: Configure Instance Details" under "Network", I selected my VPC named wright-VPC.
3. Whether a public IPv4 address will be auto-assigned to the instance / Justify choice to do so (or not do so): An IPv4 address can be auto-assigned, but it is best to use an Elastic IP I choose so Amazon cannot reassign the IP Address it gives me whenever another person pays for it or uses it.
4. How I attached a volume to my instance: Under "Step 4: Add Storage", I just went to Step 5 and accepted the default volume it chose.
5. How I tagged instance with a "Name" of "wright-instance": In "Step 5: Add Tags", I selected "Add tag" and made the Key "Name" and the Value "wright-instance".
6. How I associated my security group, "wright.sg" to my instance: In "Step 6: Configure Security Group", I selected "Select an existing security group", and chose the security group named "wright-sg".
7. How I reserved an Elastic IP address / tagged it with "wright-EIP" / associated the Elastic IP with my instance: Select "Elastic IPs", then select "Allocate Elastic IP address", then select "Add new tag", then make the Key "Name" and the Value "wright-EIP", click "Allocate". Under "Actions", select "Associate Elastic IP address", then select "Instance", then choose "wright-instance". Click "Associate". 
8. Screenshot of instance details:

9. How I ssh'd into my instance: Use the command "ssh -i ceg3120-aws-vm ubuntu@52.3.67.147".
 - How I changed the hostname to "wright-AMI": Use the command "sudo hostname wright-AMI".
10. Screenshot of ssh connection to my instance (with the new hostname):

