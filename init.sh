#!/bin/bash

# Define the target directory and the tar file
TARGET_DIR="robot"
TAR_FILE="robot.tar"

# 1. Safety Check: Ensure the tar file exists before deleting anything
if [ ! -f "$TAR_FILE" ]; then
    echo "Error: '$TAR_FILE' not found. Aborting to prevent data loss."
    exit 1
fi

# 2. Delete the existing directory if it exists
if [ -d "$TARGET_DIR" ]; then
    echo "Removing existing directory: $TARGET_DIR..."
    rm -rf "$TARGET_DIR"
else
    echo "Directory '$TARGET_DIR' does not exist. Proceeding to extract..."
fi

# 3. Extract the tar file
echo "Extracting $TAR_FILE..."
tar -xf "$TAR_FILE"

# 4. Verify success
if [ $? -eq 0 ]; then
    echo "Success: '$TAR_FILE' has been successfully extracted into place."
else
    echo "Error: Failed to extract '$TAR_FILE'."
    exit 1
fi
