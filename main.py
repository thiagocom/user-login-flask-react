# -*- coding: utf-8 -*-

import os
from app import create_app
from config import Config, DevelopmentConfig, ProductionConfig

def select_config_class(env):

	if env == "development":
		return DevelopmentConfig
	elif env == "production":
		return ProductionConfig
	return Config

environment = os.getenv("FLASK_ENV")
config_class = select_config_class(environment)
app = create_app(config_class)
