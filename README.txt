Republic of Ireland
Munster Technological University
Department of Computer Science
Student: Jose Lo Huang

Project 2 - Kubernetes

##################################
1. Introduction
##################################

This code is designed to execute basic administrative commands and
show the usage of Kubernetes components, such as: pods, controllers and
services.

The main functions are:

1. List all pods
2. Describe a pod
3. Create a pod
4. Scale the number of pods
5. Execute a command on a pod
6. Deploy a pod to every node
7. Delete a pod
8. Create a new architecture with Cluster IPs and Load Balancer

##################################
2. Code
##################################

The code included on this package is as follows:

* Kubernetes-manager.py = Manage the main program.
* Error.py = Define the Error class and functions.
* Menus.py = Includes all the menus to trigger the kubernetes tasks.
* Kubernetes.py = Define the Kubernetes class and functions.

Note: All the files must be on the same directory.

Additionally, includes the pods subfolder for the kubernetes yaml files
definitions and templates:

* ds-busybox.yaml
* frontend.conf
* frontend.yaml
* nginx-deploy.yaml
* php-redis-service.yaml
* php-redis.yaml
* redis-arch-master-service.yaml
* redis-arch-master.yaml
* redis-arch-workers-service.yaml
* redis-arch-workers.yaml
* redis-deploy.yaml

The kubernetes daemonset example is from:
https://theithollow.com/2019/08/13/kubernetes-daemonsets/

And the kubernetes architecture with cluster IP and load balancer example is from:
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/

2.1. How to Run 

The code was tested on Ubuntu Linux 18 (AWS EC2) and Mac OS Catalina with Python 3.8.

* Run the code on your cluster:

./Kubernetes-manager.py

2.2. Components and classes dependencies tree

+- Kubernetes-manager.py +- Menu.py +- Kubernetes.py +- Error.py
                                                     +- pods +- ds-busybox.yaml
                                                             +- frontend.conf
                                                             +- frontend.yaml
                                                             +- nginx-deploy.yaml
                                                             +- php-redis-service.yaml
                                                             +- php-redis.yaml
                                                             +- redis-arch-master-service.yaml
                                                             +- redis-arch-master.yaml
                                                             +- redis-arch-workers-service.yaml
                                                             +- redis-arch-workers.yaml
                                                             +- redis-deploy.yaml

2.3. Menus 

2.3.1. The main menu

KUBERNETES MANAGER V1.0.
1. List all pods
2. Describe a pod
3. Create a pod
4. Scale the number of pods
5. Execute a command on a pod
6. Deploy a pod to every node
7. Delete a pod
8. Create a new architecture with Cluster IPs and Load Balancer
9. Exit

##################################
3. Conclusion
##################################

After run this code, the user can manage the Kubernetes pods tasks in an easy and
efficient way. Also, it will provide an easy way to do the following intermediate tasks:

* Create a pod deployment for nginx and redis
* Create a daemonset deployment
* Create a multi-tier architecture using cluster IP and load balancer

##################################
4. References 
##################################

https://kubernetes.io/
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
https://github.com/kubernetes/examples/blob/master/guestbook/redis-master-deployment.yaml
https://coreos.com/tectonic/docs/latest/tutorials/sandbox/deleting-deployment.html
https://www.techrepublic.com/article/how-to-scale-a-deployment-within-a-kubernetes-cluster/
https://blog.macstadium.com/blog/how-to-k8s-exec-into-a-running-kubernetes-pod
https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
https://medium.com/google-cloud/kubernetes-run-a-pod-per-node-with-daemon-sets-f77ce3f36bf1
https://theithollow.com/2019/08/13/kubernetes-daemonsets/
https://github.com/kubernetes/kubernetes/issues/33245
https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
https://www.ovh.com/blog/getting-external-traffic-into-kubernetes-clusterip-nodeport-loadbalancer-and-ingress/
https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
https://kubernetes.io/docs/tutorials/stateless-application/guestbook/









