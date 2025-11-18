@echo off
REM ================================================================
REM n8n Startup Script for Windows
REM ================================================================
REM This script starts n8n with recommended environment variables
REM Customize the settings below for your installation
REM ================================================================

REM Set n8n port (default: 5678)
SET N8N_PORT=5678

REM Enable basic authentication (REQUIRED for network access)
SET N8N_BASIC_AUTH_ACTIVE=true
SET N8N_BASIC_AUTH_USER=admin
SET N8N_BASIC_AUTH_PASSWORD=change_this_password

REM Set timezone (adjust for your location)
REM Common values: America/New_York, America/Los_Angeles, Europe/London, Asia/Singapore
SET GENERIC_TIMEZONE=America/New_York

REM Set encryption key (IMPORTANT: Backup this key!)
REM Generate with: openssl rand -base64 32
REM Or use a password manager to generate 32 random characters
SET N8N_ENCRYPTION_KEY=your_32_character_encryption_key_here

REM Optional: Enable webhook tunnel for testing (development only)
REM Uncomment the line below to enable:
REM SET N8N_TUNNEL_MODE=true

REM Optional: Set custom data directory
REM Default: C:\Users\YourUsername\.n8n
REM SET N8N_USER_FOLDER=C:\n8n\data

REM Optional: Database settings
REM Default: SQLite (file-based)
REM For PostgreSQL, uncomment and configure:
REM SET DB_TYPE=postgresdb
REM SET DB_POSTGRESDB_HOST=localhost
REM SET DB_POSTGRESDB_PORT=5432
REM SET DB_POSTGRESDB_DATABASE=n8n
REM SET DB_POSTGRESDB_USER=n8n
REM SET DB_POSTGRESDB_PASSWORD=your_db_password

REM Optional: Execution data pruning (recommended for production)
REM Automatically delete old execution logs
SET EXECUTIONS_DATA_PRUNE=true
SET EXECUTIONS_DATA_MAX_AGE=168

REM Optional: Binary data storage mode
REM Options: default (database), filesystem
SET N8N_DEFAULT_BINARY_DATA_MODE=filesystem

REM Display startup message
echo ================================================================
echo Starting n8n Workflow Automation
echo ================================================================
echo.
echo Configuration:
echo   Port: %N8N_PORT%
echo   Timezone: %GENERIC_TIMEZONE%
echo   Basic Auth: %N8N_BASIC_AUTH_ACTIVE%
echo.
echo Access n8n at: http://localhost:%N8N_PORT%
echo.
echo Press Ctrl+C to stop n8n
echo ================================================================
echo.

REM Start n8n
REM Uses PATH to find n8n (works with npm global install, nvm, or custom locations)
n8n

REM If n8n exits, pause so you can see any error messages
pause
