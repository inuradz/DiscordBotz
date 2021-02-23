"""
Handles information regarding classes
"""

class Command():

    def __init__(self):
        super().__init__()

    def get_command_prefix() -> str:
        """This returns the prefix of a command

        <bot_invoke> <prefix> <extrainformation>
        
        Raises:
            NotImplementedError: To make sure you implement this
        
        Returns:
            str -- The prefix for the command
        """
        raise NotImplementedError("need to implement command prefix")

    def get_help() -> str:
        """This is the detailed help string that explains all the information 
        needed to use this command
        
        Raises:
            NotImplementedError: To make sure you implement this
        
        Returns:
            str -- The help string
        """
        raise NotImplementedError("need to implement a help function")

    #TODO: Add an example of the commandlist 
    def get_small_help() -> str:
        """This is to give a small description so that the command listing can give some more information
        
        Raises:
            NotImplementedError: To make sure you implement this
        
        Returns:
            str -- The small help string
        """
        raise NotImplementedError("need to implement a small help function")

    def simple_line() -> str:
        """This is the command you will run to 
        
        Raises:
            NotImplementedError: To make sure you implement this
        
        Returns:
            str -- This is what you want to return to the user
        """
        raise NotImplementedError("Apple")


