from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'coolapp')
]

setup(name='coolapp',
      version = '0.1.0',
      description = 'A cool application',
      options = {'build_exe': build_options},
      executables = executables)
