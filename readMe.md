
# Learning GitHub Project

This project is designed to help you understand how GitHub and version control systems (VCS) work under the hood. The instructions provided will guide you through running the project using **WSL** (Windows Subsystem for Linux) on a Windows machine. Compatibility with macOS and Linux is not guaranteed, but feel free to try!


## **Requirements**

- **Windows OS**: This project was built on Windows.
- **Bash**: Windows does not come with Bash by default, so you will need to use **WSL (Windows Subsystem for Linux)**.


## **Setup Instructions**

### **Step 1: Install WSL**
1. Open a PowerShell window as Administrator.
2. Run the following command to install WSL:
   ```powershell
   wsl --install
   ```
3. Wait for the installation process to complete. This will:
   - Enable the required features for WSL.
   - Install the latest version of WSL.
   - Install a default Linux distribution (e.g., Ubuntu).

4. Once the installation is complete, restart your computer if prompted.

### **Step 2: Verify WSL Installation**
1. Open a new PowerShell or Command Prompt window.
2. Run the following command to check the installed WSL version:
   ```powershell
   wsl --list --verbose
   ```
   This command will display the list of installed Linux distributions and their WSL versions.

### **Step 3: Set a Default Linux Distribution (Optional)**
1. If you have multiple Linux distributions installed, you can set a default one by running:
   ```powershell
   wsl --set-default <DistributionName>
   ```
   Replace `<DistributionName>` with the name of your preferred distribution (e.g., `Ubuntu`).

### **Step 4: Update WSL (Optional)**
1. To ensure you have the latest version of WSL, run:
   ```powershell
   wsl --update
   
### **How to Run the Code**
1. Navigate to the same directory as the GitHub file.
2. Run the following command to set the PATH environment variable:
   ```bash
   export PATH=$PATH:$(pwd)
   ```
3. Then run:
   ```bash
   run init
   ```