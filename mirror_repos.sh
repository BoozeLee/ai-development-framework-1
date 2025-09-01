#!/bin/bash
# Repository Mirroring Script
#
# This script automatically mirrors changes between:
# - Personal: https://github.com/BoozeLee/ai-development-framework
# - Organization: https://github.com/Bakery-street-projct/ai-development-framework
#
# Usage:
#   ./mirror_repos.sh [personal|org|both]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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

# Function to push to both repositories
mirror_to_both() {
    print_status "Mirroring to both repositories..."
    
    # Push to personal repository
    print_status "Pushing to personal repository (origin)..."
    git push origin master
    git push origin develop
    
    # Push to organization repository
    print_status "Pushing to organization repository (org)..."
    git push org master
    git push org develop
    
    print_success "Successfully mirrored to both repositories!"
}

# Function to push to personal repository only
mirror_to_personal() {
    print_status "Pushing to personal repository only..."
    git push origin master
    git push origin develop
    print_success "Successfully pushed to personal repository!"
}

# Function to push to organization repository only
mirror_to_org() {
    print_status "Pushing to organization repository only..."
    git push org master
    git push org develop
    print_success "Successfully pushed to organization repository!"
}

# Function to sync from personal to organization
sync_personal_to_org() {
    print_status "Syncing from personal to organization repository..."
    git fetch origin
    git push org origin/master:master
    git push org origin/develop:develop
    print_success "Successfully synced personal to organization!"
}

# Function to sync from organization to personal
sync_org_to_personal() {
    print_status "Syncing from organization to personal repository..."
    git fetch org
    git push origin org/master:master
    git push origin org/develop:develop
    print_success "Successfully synced organization to personal!"
}

# Function to check repository status
check_status() {
    print_status "Checking repository status..."
    
    echo ""
    echo "Personal Repository (origin):"
    echo "  URL: https://github.com/BoozeLee/ai-development-framework"
    echo "  Status: $(git remote show origin | grep 'HEAD branch' | cut -d' ' -f5)"
    
    echo ""
    echo "Organization Repository (org):"
    echo "  URL: https://github.com/Bakery-street-projct/ai-development-framework"
    echo "  Status: $(git remote show org | grep 'HEAD branch' | cut -d' ' -f5)"
    
    echo ""
    echo "Current branch: $(git branch --show-current)"
    echo "Last commit: $(git log -1 --oneline)"
}

# Main execution
case "${1:-both}" in
    "personal")
        mirror_to_personal
        ;;
    "org")
        mirror_to_org
        ;;
    "both")
        mirror_to_both
        ;;
    "sync-personal")
        sync_personal_to_org
        ;;
    "sync-org")
        sync_org_to_personal
        ;;
    "status")
        check_status
        ;;
    *)
        echo "Usage: $0 [personal|org|both|sync-personal|sync-org|status]"
        echo ""
        echo "Commands:"
        echo "  personal      - Push to personal repository only"
        echo "  org          - Push to organization repository only"
        echo "  both         - Push to both repositories (default)"
        echo "  sync-personal - Sync from personal to organization"
        echo "  sync-org     - Sync from organization to personal"
        echo "  status       - Check repository status"
        echo ""
        echo "Examples:"
        echo "  $0 both              # Mirror to both repositories"
        echo "  $0 personal          # Push to personal only"
        echo "  $0 org               # Push to organization only"
        echo "  $0 sync-personal     # Sync personal → organization"
        echo "  $0 status            # Check status"
        ;;
esac
