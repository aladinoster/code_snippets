import sys
sys.path.extend(['path_1', 'path_2'])

import split_farm
print(split_farm.__path__)

import split_farm.bird
import split_farm.bovine

print(split_farm.bird.__path__)
print(split_farm.bovine.__path__)