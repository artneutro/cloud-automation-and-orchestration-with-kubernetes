# 
# Author: Jose Lo Huang
# Creation Date: 22/12/2020
# Updates: None
# 
# This code is to maintain all the management menus in the same place.
# From this code, the specific Kubernetes tasks are triggered.
# 

import Kubernetes
import Error

error = Error.Error()

def main_menu ():
    # 
    # Main Menu:
    # This function shows the main menu and request the user option.
    # 
    print("==================================================================")
    print("KUBERNETES MANAGER V1.0.")
    print("1. List all pods")
    print("2. Describe a pod")
    print("3. Create a pod")
    print("4. Scale the number of pods")
    print("5. Execute a command on a pod")
    print("6. Deploy a pod to every node")
    print("7. Delete a pod")
    print("8. Create a new architecture with Cluster IPs and Load Balancer")
    print("9. Exit")
    print("==================================================================")
    option = input("Please insert the number of the service you want to manage : ")
    return option


def menu ():
    # 
    # Router menu:
    # This procedure is in charge of route the user to the different kubernetes functions
    # depending on the chosen options.
    # 
    option = None
    kubernetes = Kubernetes.Kubernetes()
    while (option != "9"):
        option = main_menu()
        print()
        # List all pods
        if (option == "1"):
            print("******************************************************************")
            print(" ALL PODS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.list_pods()
        # Describe a pod
        elif (option == "2"):
            print("******************************************************************")
            print(" DESCRIBE A POD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.describe_pod()
        # Create a pod
        elif (option == "3"):
            print("******************************************************************")
            print(" CREATE A POD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.create_pod()
        # Scale the number of pods
        elif (option == "4"):
            print("******************************************************************")
            print(" SCALE PODS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.scale_pods()
        # Execute a command on a pod
        elif (option == "5"):
            print("******************************************************************")
            print(" EXECUTE COMMAND ON POD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.execute_command_pod()
        # Deploy a pod to every node
        elif (option == "6"):
            print("******************************************************************")
            print(" DEPLOY POD TO EVERY NODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.deploy_pods()
        # Delete a pod
        elif (option == "7"):
            print("******************************************************************")
            print(" DELETE A POD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.delete_pod()
        # Create a new architecture with cluster IP and load balancer
        elif (option == "8"):
            print("******************************************************************")
            print(" CREATE ARCHITECTURE WITH CLUSTER IP AND LOAD BALANCER >>>>>>>>>> ")
            print("******************************************************************")
            kubernetes.create_architecture()
        # Exit program 
        elif (option == "9"):
            del kubernetes
        else:
            error.not_valid_value(option)
        print()


