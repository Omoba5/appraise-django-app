#!/bin/bash

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
  echo "PostgreSQL is not installed. Installing now..."

  # Install necessary packages
  sudo apt-get update
  sudo apt-get install -y curl ca-certificates gnupg apt-transport-https

  # Add PostgreSQL official repository
  curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /usr/share/keyrings/postgresql-keyring.gpg

  # Detect Ubuntu version
  UBUNTU_VERSION=$(lsb_release -cs)

  # Add PostgreSQL repo based on the detected version
  echo "deb [signed-by=/usr/share/keyrings/postgresql-keyring.gpg] http://apt.postgresql.org/pub/repos/apt/ ${UBUNTU_VERSION}-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list

  # Update package list and install PostgreSQL
  sudo apt-get update
  sudo apt-get install -y postgresql-16  # Install the latest stable version (16 as of 2024)

  echo "PostgreSQL installation complete."
else
  echo "PostgreSQL is already installed."
fi
