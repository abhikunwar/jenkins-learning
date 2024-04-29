from pathlib import Path
import os
import configparser
# config = configparser.ConfigParser()
base_path = Path(__file__).resolve().parent.parent
ini_file = "petdata.ini"
config_folder = "config"
# print(base_path)

def read_ini():
    global ini_file
    config_path = os.path.join(base_path,config_folder)
    # print("config_path",config_path)
    ini_file = os.path.join(config_path,ini_file)
    config_parser = configparser.ConfigParser()
    config_parser.read(ini_file)
    return config_parser
# ini_content = read_ini()
# print("***")
# print(ini_content['pet']['url'])



    
