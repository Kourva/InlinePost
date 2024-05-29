#!/usr/bin/env bash

# Installer fro InlinePost bot

# Make bash trap to detect Ctrl+C
trap bashtrap INT
bashtrap() {
    echo -e "\n[x] CTRL+C Detected! cancelling installation..."
    exit
}

# Install requirements for InlinePost
function install_requirements {
    # Set requirements file
    RequirementsFile="requirements.txt"
    
    # Check requirements file
    if [ -e $RequirementsFile ]; then
       echo $(pip install -r $RequirementsFile)
       echo ""
       echo -e "[*] Requirements installed!"   
    else 
        echo "[x] Requirements file does not exist!"
    fi
    exit
}

# Install virtual environment for InlinePost
function make_virtualenv {    
    # Make virtual environment
    echo $(virtualenv venv)
    echo ""
    echo -e "[*] Activate using 'source venv/bin/activate'"
    exit
}

# Install bot commands for InlinePost
function install_bot_commands {
    # Set installer file
    CommandInstallerFile="install_commands.py"

    # Check installer file
    if [ -e $CommandInstallerFile ]; then
        # Install bot commands 
        echo $(python $CommandInstallerFile)
        echo ""
        echo -e "[*] Commands installed successfully!"
    else 
        echo "[x] Commands script does not exist!"
    fi
    exit
}

# Main function
function main {
    # Get input from user
    echo "[?] Welcome to InlinePost installer"
    echo "1) Make virtualenv"
    echo "2) Install requirements"
    echo "3) Install bot commands"
    echo -e "Choose an option: \c"
    read operation

    # Select Operation  
    if [ $operation == "1" ]; then
        make_virtualenv
    elif [ $operation == "2" ]; then
        install_requirements
    elif [ $operation == "3" ]; then
        install_bot_commands
    else
        exit
    fi
}

# Run main function
main
