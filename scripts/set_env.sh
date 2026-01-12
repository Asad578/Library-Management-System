#!/bin/bash
# Quick script to set Django environment
# Usage: source scripts/set_env.sh [dev|staging|production]

ENV=${1:-dev}

if [ "$ENV" != "dev" ] && [ "$ENV" != "staging" ] && [ "$ENV" != "production" ]; then
    echo "Error: Environment must be 'dev', 'staging', or 'production'"
    exit 1
fi

export DJANGO_ENV=$ENV
echo "Django environment set to: $ENV"
