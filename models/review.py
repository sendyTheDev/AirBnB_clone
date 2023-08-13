#!/usr/bin/python3
"""Defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A blueprint for review objects"""
    user_id = ""
    place_id = ""
    text = ""
