# 
# Author: Jose Lo Huang
# Creation Date: 22/12/2020
# Updates: None
# 
# This code is to define the Error class
# 


class Error:
    # 
    # The Error class will manage the main and repetitive error messages
    # 

    def __init__ ( self ):
        #
        # The only variable is a dummy text for future purposes
        # 
        self.text = None


    def general_error ( self , msg ):
        #
        # This function is to print a general error message if there is an unexpected error
        # 
        print()
        print("******************************************************************")
        print("There was a problem "+ str(msg) +". Check the following: ")
        print("1. Your internet connection ")
        print("2. Your Kubernetes is up and running ")
        print("3. You have the correct permissions ")
        print("******************************************************************")
        print()


    def not_valid_value ( self , value ):
        #
        # This function will indicate that a value is not valid
        # 
        print("======> " + str(value) + " is not a valid value.")
        print("Please choose a valid value.")
        

    def error_kubernetes ( self , msg ):
        #
        # This function will indicate that there was an error with a pod stage
        # 
        print("There was an error "+msg+". Please check the logs.")
        

