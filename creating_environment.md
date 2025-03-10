# Create and Activate a Python Virtual Environment

Follow these steps to set up the Python environment and install dependencies.

---

## Prerequisites
- **Python 3.6+**: Ensure Python is installed. Verify with:  
  ```bash
  python --version
  ```
- **pip**: Package installer for Python. Usually included with modern Python installations.

---

### macOS / Linux
1. Open **Terminal**.
2. Navigate to your project directory:
   ```bash
   cd path/to/your/project
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the environment:
   ```bash
   source venv/bin/activate
   ```

### Windows (Command Prompt/PowerShell)
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to your project directory:
   ```cmd
   cd path\to\your\project
   ```
3. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```
4. Activate the environment:
   - **Command Prompt**:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **PowerShell** (may require admin permissions):
     ```powershell
     Set-ExecutionPolicy Unrestricted -Scope Process -Force
     .\venv\Scripts\Activate.ps1
     ```

---

## Install Dependencies
Run this command after activating the virtual environment:
```bash
pip install -r requirements.txt
```

---

## Deactivate the Environment
When done, exit the virtual environment:
```bash
deactivate
```

---

## Troubleshooting
- **"python3: command not found" (macOS/Linux)**:  
  Install Python from [python.org](https://www.python.org/downloads/).
- **ModuleNotFoundError: No module named 'venv' (Linux)**:  
  Install the `python3-venv` package:
  ```bash
  sudo apt-get install python3-venv
  ```
- **Permission Issues (Windows)**:  
  Run PowerShell/CMD as **Administrator**.
- **Outdated pip**: Upgrade pip before installing requirements:
  ```bash
  pip install --upgrade pip
  ```

---

**Note**: Replace `path/to/your/project` with your actual project directory path.  
For issues not listed here, consult the [Python venv documentation](https://docs.python.org/3/library/venv.html).