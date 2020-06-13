import sys

print(f'Using Python Version {sys.version[0:5]}')
if sys.prefix == sys.base_prefix:
    # no venv
    print(f'Using Python default system environment.')
else:
    # venv
    print(f'Using Python virtual environment: {sys.prefix}')
