#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """A class that prevents the creation of new attributes other than 'first_name'."""

    __slots__ = ["first_name"]  # Only allow 'first_name' as an attribute

    def __setattr__(self, name, value):
        # Prevent setting any attribute other than 'first_name'
        if name != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
