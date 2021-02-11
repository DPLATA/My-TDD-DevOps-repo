#from django.test import TestCase
import pytest
from django.urls import resolve
from lists.views import home_page
from lists.models import Item

# Create your tests here.

def test_home_page(client):
    found = resolve('/')
    #response = client.get(url)
    assert found.func == home_page

def test_saving_and_retrieving_items(db):
    first_item = Item.objects.create()
    first_item.text = 'First item ever'
    first_item.save()
    #second_item = Item()
    #second_item.text = 'Item two'
    #second_item.save()
    saved_items = Item.objects.all()
    assert saved_items.count() == 1
    #first_saved_item = saved_items[0]
    #second_saved_item = saved_items[1]
    #assert first_saved_item.text == 'First item ever'
    #assert second_saved_item.text == 'Item two'