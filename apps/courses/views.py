# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, reverse
from models import *
from django.contrib import messages

def index(request):
	context = {
		"courses": Course.objects.all()
	}
	return render(request, "courses/index.html", context)

def add(request):
	errors = Course.objects.validate(request.POST)
	if errors:
		for error in errors:
			messages.error(request, error)
	else:
		Course.objects.create(name = request.POST["name"], desc = request.POST["desc"])
	return redirect(reverse("index"))

def warn(request, id):
	context = {
		"course": Course.objects.get(id=id)
	}
	return render(request, "courses/warn.html", context)

def destroy(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	return redirect(reverse("index"))