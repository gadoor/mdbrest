"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/3/16'
"""
import yaml


def load_config():
    config_file = "../config.yml"
    with open(config_file) as f:
        config = yaml.load(f)
    return config