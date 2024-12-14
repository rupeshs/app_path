import sys
from app_path import get_application_path
import os

print("Is Frozen :", getattr(sys, "frozen", False))
print("Application Path :", get_application_path())
print(os.path.join(get_application_path(), "configs"))
