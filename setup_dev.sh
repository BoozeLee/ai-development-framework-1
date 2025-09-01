#!/bin/bash
"""
Development Setup Script for AI Development Framework

This script sets up the complete development environment including:
- Virtual environment
- Dependencies installation
- Pre-commit hooks
- Testing framework
- Code quality tools
"""

set -e  # Exit on any error

echo "🚀 Setting up AI Development Framework Development Environment"
echo "================================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python 3.11+ is available
check_python() {
    print_status "Checking Python version..."
    if command -v python3.11 &> /dev/null; then
        PYTHON_CMD="python3.11"
        print_success "Python 3.11 found"
    elif command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
        if [[ "$PYTHON_VERSION" > "3.10" ]]; then
            PYTHON_CMD="python3"
            print_success "Python $PYTHON_VERSION found"
        else
            print_error "Python 3.11+ required, found $PYTHON_VERSION"
            exit 1
        fi
    else
        print_error "Python 3.11+ not found"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."
    if [ ! -d "venv" ]; then
        $PYTHON_CMD -m venv venv
        print_success "Virtual environment created"
    else
        print_warning "Virtual environment already exists"
    fi
}

# Activate virtual environment
activate_venv() {
    print_status "Activating virtual environment..."
    source venv/bin/activate
    print_success "Virtual environment activated"
}

# Install dependencies
install_dependencies() {
    print_status "Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    print_success "Dependencies installed"
}

# Install development tools
install_dev_tools() {
    print_status "Installing development tools..."
    pip install pre-commit pytest-cov bandit safety
    print_success "Development tools installed"
}

# Set up pre-commit hooks
setup_pre_commit() {
    print_status "Setting up pre-commit hooks..."
    pre-commit install
    print_success "Pre-commit hooks installed"
}

# Run initial tests
run_tests() {
    print_status "Running initial tests..."
    python -m pytest tests/ -v
    print_success "Tests completed"
}

# Create development configuration
create_dev_config() {
    print_status "Creating development configuration..."
    
    # Create .env file if it doesn't exist
    if [ ! -f ".env" ]; then
        cat > .env << EOF
# Development Environment Configuration
DEBUG=True
LOG_LEVEL=DEBUG
ENVIRONMENT=development

# API Keys (add your actual keys here)
OPENAI_API_KEY=your_openai_api_key_here
AWS_ACCESS_KEY_ID=your_aws_access_key_here
AWS_SECRET_ACCESS_KEY=your_aws_secret_key_here

# Database Configuration
DUCKDB_PATH=./data/local.db
ATHENA_REGION=us-east-1
ATHENA_S3_BUCKET=your-athena-bucket

# Application Settings
MAX_CONCURRENT_WORKFLOWS=3
TIMEOUT_SECONDS=300
RETRY_ATTEMPTS=3
EOF
        print_success "Development .env file created"
    else
        print_warning ".env file already exists"
    fi
}

# Create data directory
create_data_dir() {
    print_status "Creating data directory..."
    mkdir -p data
    print_success "Data directory created"
}

# Display setup summary
show_summary() {
    echo ""
    echo "🎉 Development Environment Setup Complete!"
    echo "=========================================="
    echo ""
    echo "Next steps:"
    echo "1. Activate the virtual environment: source venv/bin/activate"
    echo "2. Update .env file with your API keys"
    echo "3. Run tests: python -m pytest tests/ -v"
    echo "4. Start development: python advanced_ai_orchestrator.py"
    echo ""
    echo "Available commands:"
    echo "- python -m pytest tests/          # Run tests"
    echo "- pre-commit run --all-files      # Run code quality checks"
    echo "- black .                         # Format code"
    echo "- flake8 .                        # Lint code"
    echo "- mypy .                          # Type checking"
    echo ""
}

# Main execution
main() {
    check_python
    create_venv
    activate_venv
    install_dependencies
    install_dev_tools
    setup_pre_commit
    create_dev_config
    create_data_dir
    run_tests
    show_summary
}

# Run main function
main "$@"
