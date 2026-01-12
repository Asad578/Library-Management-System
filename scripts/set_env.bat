@echo off
REM Quick script to set Django environment on Windows
REM Usage: scripts\set_env.bat [dev|staging|production]

set ENV=%1
if "%ENV%"=="" set ENV=dev

if not "%ENV%"=="dev" if not "%ENV%"=="staging" if not "%ENV%"=="production" (
    echo Error: Environment must be 'dev', 'staging', or 'production'
    exit /b 1
)

set DJANGO_ENV=%ENV%
echo Django environment set to: %ENV%
