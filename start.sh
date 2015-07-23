#!/bin/bash

VIRTUALENV_NAME="googleplayscraper-py3"

export SCRAPER_PROD=1

~/.virtualenvs/${VIRTUALENV_NAME}/bin/python /opt/googleplayscraper/current/main.py --init