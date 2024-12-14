import sys
from app_path import get_application_path
import os

print("Is Frozen :", getattr(sys, "frozen", False))
application_path = get_application_path()
print("Application Path :", application_path)
print("Configs Directory :", os.path.join(application_path, "configs"))
