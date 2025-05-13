#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Function to print messages
print_message() {
    echo -e "${GREEN}$1${NC}"
}

# Function to print errors
print_error() {
    echo -e "${RED}$1${NC}"
}

# Check if Docker is running
check_docker() {
    if ! docker info > /dev/null 2>&1; then
        print_error "Docker is not running. Please start Docker first."
        exit 1
    fi
}

case "$1" in
    "build")
        print_message "Building Docker container..."
        docker-compose build
        ;;
    "up")
        check_docker
        print_message "Starting application..."
        docker-compose up
        ;;
    "down")
        check_docker
        print_message "Stopping application..."
        docker-compose down
        ;;
    "restart")
        check_docker
        print_message "Restarting application..."
        docker-compose down
        docker-compose up -d
        ;;
    "logs")
        check_docker
        print_message "Showing logs..."
        docker-compose logs -f
        ;;
    *)
        echo "Usage: $0 {build|up|down|restart|logs}"
        exit 1
        ;;
esac
