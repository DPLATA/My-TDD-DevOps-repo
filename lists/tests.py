#from django.test import TestCase
import pytest
from django.urls import resolve, reverse
from lists.views import home_page

# Create your tests here.

def test_home_page(client):
    found = resolve('/')
    #response = client.get(url)
    assert found.func == home_page