from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='wjq^(wo9mu46_t*w3uu&m%3-1#p6@fb)8u=@3ew21c%c+tgxuq')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
