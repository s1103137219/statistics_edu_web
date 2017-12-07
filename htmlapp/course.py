#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.contrib import auth
from django.http import *
import os
from htmlapp.forms import loginform 
from django.db import connection
from django.contrib.auth.decorators import login_required
from htmlapp.models import *
from django.contrib.auth.models import User
import sys


      