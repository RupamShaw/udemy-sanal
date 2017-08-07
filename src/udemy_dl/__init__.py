#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python script to download a business udemy.com course, for personal offline use."""
import logging
import colorlog

from .udemy_dl import udemy_dl

__all__ = ['udemy_dl']
__title__ = 'udemy-sanal'
__author__ = 'Sanal Malhotra'
__license__ = 'Unlicense'
__copyright__ = 'Copyright 2017'


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s[%(levelname)s-%(lineno)d] %(message)s'))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(level=logging.INFO)
