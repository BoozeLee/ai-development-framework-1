#!/bin/bash

# AIOS Menu Launcher
# A comprehensive launcher for AIOS (AGI Research)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
BASE_DIR="/home/booze/ai-development"
ENV_PATH="$BASE_DIR/environments/aios-env"
MENU_SCRIPT="$BASE_DIR/aios_menu.py"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${CYAN}================================${NC}"
    echo -e "${CYAN}    🚀 AIOS Menu Launcher 🚀    ${NC}"
    echo -e "${CYAN}================================${NC}"
}

# Check if we're in the right directory
check_environment() {
    if [[ ! -d "$BASE_DIR" ]]; then
        print_error "AIOS base directory not found: $BASE_DIR"
        exit 1
    fi

    if [[ ! -d "$ENV_PATH" ]]; then
        print_error "AIOS virtual environment not found: $ENV_PATH"
        print_warning "Please run the installation script first"
        exit 1
    fi

    if [[ ! -f "$MENU_SCRIPT" ]]; then
        print_error "AIOS menu script not found: $MENU_SCRIPT"
        exit 1
    fi
}

# Activate virtual environment
activate_env() {
    print_status "Activating AIOS virtual environment..."

    if [[ -f "$ENV_PATH/bin/activate" ]]; then
        source "$ENV_PATH/bin/activate"
        print_status "Environment activated successfully"
    else
        print_error "Environment activation script not found"
        exit 1
    fi
}

# Check Python availability
check_python() {
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 is not installed or not in PATH"
        exit 1
    fi

    print_status "Python3 found: $(python3 --version)"
}

# Main launcher function
launch_menu() {
    print_header
    print_status "Starting AIOS Comprehensive Menu..."

    # Check environment
    check_environment
    check_python

    # Activate environment
    activate_env

    # Launch the menu
    print_status "Launching AIOS menu..."
    echo ""

    # Run the menu with proper environment
    cd "$BASE_DIR"
    python3 "$MENU_SCRIPT"
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        echo "AIOS Menu Launcher"
        echo ""
        echo "Usage: $0 [OPTION]"
        echo ""
        echo "Options:"
        echo "  --help, -h     Show this help message"
        echo "  --test         Test AIOS installation"
        echo "  --debug        Run in debug mode"
        echo "  --version      Show version information"
        echo ""
        echo "Examples:"
        echo "  $0              # Launch the main menu"
        echo "  $0 --test       # Test AIOS installation"
        echo "  $0 --debug      # Run with debug output"
        ;;
    --test)
        print_header
        print_status "Testing AIOS installation..."

        check_environment
        activate_env

        # Run a quick test
        python3 -c "
import aios
print('✅ AIOS imported successfully')
obj = aios.Object('TestAgent')
print(f'✅ Object created: {obj}')
state = aios.State(['idle', 'working', 'done'])
print(f'✅ State created: {state}')
print('🎉 AIOS test passed!')
"
        ;;
    --debug)
        print_header
        print_status "Running in debug mode..."

        set -x  # Enable debug output
        check_environment
        activate_env
        python3 "$MENU_SCRIPT"
        ;;
    --version)
        echo "AIOS Menu Launcher v1.0.0"
        echo "AIOS (AGI Research) - Advanced AI Agent Operating System"
        ;;
    "")
        launch_menu
        ;;
    *)
        print_error "Unknown option: $1"
        echo "Use --help for usage information"
        exit 1
        ;;
esac
