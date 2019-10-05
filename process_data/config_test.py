import configparser
import os
config = configparser.ConfigParser()
print(config.sections())
config.read('process_data/config.ini')
#for line in open('config.ini'):
#    print(line)
print(config.sections())
print(config['path']['sy_path'])
print(os.getcwd())