# -*- coding: utf-8 -*-

from flask import Flask

def create_app(config_class=None):

	"Factory app"

	app = Flask("app")

	# Main route
	def index():
		return "Welcome to development world"

	app.add_url_rule("/", "index", index)

	# Configuration
	app.config.from_object(config_class)

	return app
