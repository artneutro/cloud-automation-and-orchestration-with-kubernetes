# 
# Author: Jose Lo Huang
# Creation Date: 22/12/2020
# Updates: None
# 
# This code is to define the Kubernetes class
#


import os
import time
import Error


class Kubernetes:
    # 
    # The Kubernetes class will manage the kubernetes tasks
    # 

    def __init__ ( self ):
        #
        # A instantiation of Error class for error messages
        # 
        self.error = Error.Error()


    def list_pods ( self ):
        #
        # This function lists all the pods
        # 
        try:
            all_pods = []
            os.system("kubectl get pods -o wide")
            for i in os.popen('kubectl get pods -o wide | awk \'{print $1}\'').read().split('\n'):
                all_pods.append(i)
            return all_pods[1:-1]
        except:
            self.error.error_kubernetes("listing the pods")


    def describe_pod ( self ):
        #
        # This function describes a pod chosen by the user
        # Input:
        # * Pod name
        # 
        try:
            all_pods = self.list_pods()
            while True:
                pod_name = input("Please insert the pod name: ")
                if pod_name in all_pods:
                    os.system("kubectl describe pod "+pod_name)
                    break
                else:
                    self.error.not_valid_value(pod_name)
        except:
            self.error.error_kubernetes("describing the pod")


    def create_pod ( self ):
        #
        # This function creates a pod deployment using nginx or redis images.
        # Input:
        # * Image name
        # 
        try:
            while True:
                print("Please insert the pod image of your preference: ")
                print("1. nginx")
                print("2. redis")
                image_name = input()
                if str(image_name) in ['1','nginx']:
                    os.system("kubectl apply -f pods/nginx-deploy.yaml")
                elif str(image_name) in ['2','redis']:
                    os.system("kubectl apply -f pods/redis-deploy.yaml")
                else:
                    self.error.not_valid_value(image_name)
                time.sleep(3)
                self.list_pods()
                break
        except:
            self.error.error_kubernetes("creating the pod")


    def scale_pods ( self ):
        #
        # This function scales the number of pods of a particular type deployment.
        # Input:
        # * New number of pods
        # * Pod type
        # 
        try:
            pod_number = input("Please insert the new number of pods of your preference: ")
            while True:
                print("Please insert the pod image to scale: ")
                print("1. nginx")
                print("2. redis")
                image_name = input()
                if str(image_name) in ['1','nginx']:
                    os.system("kubectl scale deployments/nginx-deployment --replicas="+str(pod_number))
                elif str(image_name) in ['2','redis']:
                    os.system("kubectl scale deployments/redis-deployment --replicas="+str(pod_number))
                else:
                    self.error.not_valid_value(image_name)
                time.sleep(3)
                self.list_pods()
                break
        except:
            self.error.error_kubernetes("scaling the pods")


    def execute_command_pod ( self ):
        #
        # This function executes a command on a pod chosen by the user.
        # Input:
        # * Command
        # * Pod name
        # 
        try:
            command_list = input("Please insert the command: ").split(' ')
            command = ''
            for i in command_list:
                command += i+' '
            all_pods = self.list_pods()
            while True:
                pod_name = input("Please insert the pod name: ")
                if pod_name in all_pods:
                    os.system("kubectl exec "+pod_name+" -- "+command)
                    break
                else:
                    self.error.not_valid_value(pod_name)
        except:
            self.error.error_kubernetes("executing the command on the pod")


    def  deploy_pods( self ):
        #
        # This function creates a pod daemonset using a public monitor image.
        # 
        try:
            os.system("kubectl apply -f pods/ds-busybox.yaml")
            time.sleep(3)
            self.list_pods()
        except:
            self.error.error_kubernetes("deploying the daemonset")
            

    def delete_pod ( self ):
        #
        # This function deletes a pod.
        # Input:
        # * Pod name
        # 
        try:
            all_pods = self.list_pods()
            while True:
                pod_name = input("Please insert the pod name: ")
                if pod_name in all_pods:
                    os.system("kubectl delete pod "+pod_name)
                    break
                else:
                    self.error.not_valid_value(pod_name)
        except:
            self.error.error_kubernetes("deleting the pod")


    def create_architecture ( self ):
        #
        # This function creates a kubernetes architecture using Cluster IP and Load Balancer services.
        # From: https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
        # 
        try:
            # Creating all the architecture. Total time 270 seconds.
            print()
            # Creating the Redis master
            print("******************************************************************")
            print("******************** CREATING REDIS MASTER ***********************")
            os.system("kubectl apply -f pods/redis-arch-master.yaml")
            time.sleep(30)
            os.system("kubectl get pods -o wide")
            # Cluster IP service
            print("******************************************************************")
            print("**************** CREATING REDIS MASTER SERVICE *******************")
            os.system("kubectl apply -f pods/redis-arch-master-service.yaml")
            time.sleep(30)
            os.system("kubectl get services")
            # Creating the Redis workers
            print("******************************************************************")
            print("******************* CREATING REDIS WORKERS ***********************")
            os.system("kubectl apply -f pods/redis-arch-workers.yaml")
            time.sleep(30)
            os.system("kubectl get pods -o wide")
            # Cluster IP service
            print("******************************************************************")
            print("**************** CREATING REDIS WORKERS SERVICE ******************")
            os.system("kubectl apply -f pods/redis-arch-workers-service.yaml")
            time.sleep(30)
            os.system("kubectl get services")
            # Creating the PHP guestbook
            print("******************************************************************")
            print("****************** CREATING PHP GUESTBOOK ************************")
            os.system("kubectl apply -f pods/php-redis.yaml")
            time.sleep(90)
            os.system("kubectl get pods -o wide")
            # Load Balancer service
            print("******************************************************************")
            print("********************* CREATING PHP SERVICE ***********************")
            os.system("kubectl apply -f pods/php-redis-service.yaml")
            time.sleep(30)
            os.system("kubectl get services")
            # Checking the architecture
            print("******************************************************************")
            print("******************** CHECKING PHP SERVICE ************************")
            time.sleep(30)
            ip = os.popen("kubectl get service frontend | tail -1 | awk '{print $3}'").read()
            print("curl http://"+str(ip))
            os.system("curl http://"+str(ip))
            time.sleep(1)
        except:
            self.error.error_kubernetes("creating the architecture")


