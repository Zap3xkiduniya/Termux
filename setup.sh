#!/data/data/com.termux/files/usr/bin/bash
#===============================================================================
# Installer for Number Lookup Tool (Termux)
# 
# Usage: bash install.sh
# 
# This script:
#   1. Updates Termux packages
#   2. Installs Python (if not already installed)
#   3. Installs Python dependencies from requirements.txt
#===============================================================================

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║     Installing Number Lookup Tool...      ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════╝${NC}"
echo ""

# Step 1: Update Termux packages
echo -e "${YELLOW}[1/3] Updating Termux packages...${NC}"
pkg update -y
echo -e "${GREEN}[✓] Packages updated${NC}"
echo ""

# Step 2: Install Python
echo -e "${YELLOW}[2/3] Installing Python...${NC}"
pkg install python -y
echo -e "${GREEN}[✓] Python installed${NC}"
echo ""

# Step 3: Install Python dependencies
echo -e "${YELLOW}[3/3] Installing Python dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}[✓] Dependencies installed${NC}"
echo ""

# Done
echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║       Installation Complete!              ║${NC}"
echo -e "${GREEN}║                                           ║${NC}"
echo -e "${GREEN}║       Run: python main.py                 ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════╝${NC}"
echo ""