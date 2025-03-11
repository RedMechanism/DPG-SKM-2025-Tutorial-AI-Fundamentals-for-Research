#!/usr/bin/env python3
import importlib

# Dictionary mapping package display names to the module names used for import
packages = {
    "numpy": "numpy",
    "torch": "torch",
    "seaborn": "seaborn",
    "matplotlib": "matplotlib",
    "notebook": "notebook",
    "h5py": "h5py",
    "scikit-image": "skimage",        # Module name is 'skimage'
    "scikit-learn": "sklearn",          # Module name is 'sklearn'
    "scikit-optimize": "skopt",         # Module name is 'skopt'
    "ipywidgets": "ipywidgets",
    "ipykernel": "ipykernel",
}

missing_packages = 0

print("Checking installations for required packages...\n")
for pkg_display, module_name in packages.items():
    try:
        importlib.import_module(module_name)
        print(f"[SUCCESS] {pkg_display}")
    except ModuleNotFoundError:
        print(f"[FAILED] {pkg_display} !package is missing")
        missing_packages += 1

print("\n--- Summary ---")
if missing_packages == 0:
    print("All requirements are installed!")
else:
    print(f"{missing_packages} package{'s are' if missing_packages != 1 else ' is'} missing. Please install all missing packages.")
