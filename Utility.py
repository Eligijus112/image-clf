import os
import yaml


class Utility():
    """
    A class to handle various utility classes
    """

    def __init__(self):
        self.cur_dir = os.getcwd() 

    def makedir(self, path:str):
        """
        A method to create a directory
        """
        if not os.path.exists(f"{self.cur_dir}/{path}"):
            os.mkdir(f"{self.cur_dir}/{path}")

    def read_conf(self, path:str):
        """
        Reads a *.yml file 
        """
        with open(f"{self.cur_dir}/{path}") as file:
            return yaml.load(file, Loader=yaml.FullLoader)