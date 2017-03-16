Provisioning a new site 
===========

## Required packages:

* nginx
* Python 3.6
* Git
* pip
* virtualenv

e.g.,  on Ubuntu:

	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

#Folder structure
Assume we have a user at /home/username

/home/username
---sites
	---SITENAME
		---database
		---source
		---static
		---virtualenv