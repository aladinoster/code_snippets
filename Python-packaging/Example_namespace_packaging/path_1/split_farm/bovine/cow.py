# Absolute import
#from farm.bovine.common import ruminate

# Relative import 
from .common import ruminate

# Relative import  - Requires de call like common.ruminate()
# from . import ruminate

def rum_cow():
    print('This is the cow ruminate:')
    ruminate()