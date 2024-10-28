#!/bin/bash

# Function to run Alembic migrations based on type and table
run_migrations() {
    local type=$1
    local table=$2

    # Initialize an empty array to hold the revision numbers
    revisions=()

    # Determine the file pattern based on the type parameter
    if [[ "$type" == "type" ]]; then
        pattern="*_type.py"
    elif [[ "$type" == "table" ]]; then
        pattern="*_table.py"
    else
        echo "Invalid type specified. Use 'type' or 'table'."
        return
    fi

    # Loop through the relevant files
    for file in ./alembic/versions/$pattern; do
        # Extract the part between the first '-' and the first '_'
        revision=${file#*-}   # Remove everything before and including the first '-'
        revision=${revision%%_*}  # Remove everything after and including the first '_'
        
        # Append the revision to the array if it's not empty
        if [[ -n $revision ]]; then
            revisions+=("$revision")
        fi
    done

    # Print the collected revisions
    echo "Collected revisions for $type:"
    for revision in "${revisions[@]}"; do
        echo "$revision"
    done

    # Loop through each revision and run the upgrade command
    for revision in "${revisions[@]}"; do
        alembic upgrade "$revision"
    done
}

run_migrations "type"
run_migrations "table"