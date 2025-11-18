@echo off
REM ================================================================
REM n8n Backup Script for Windows
REM ================================================================
REM This script creates a complete backup of your n8n installation
REM including workflows, credentials, and configuration
REM ================================================================

SETLOCAL EnableDelayedExpansion

REM ================================================================
REM Configuration
REM ================================================================

REM Backup destination directory
SET BACKUP_DIR=C:\n8n-backups

REM n8n data directory (default location)
SET N8N_DATA_DIR=%USERPROFILE%\.n8n

REM Date format for backup folder name
SET BACKUP_DATE=%DATE:~-4,4%%DATE:~-10,2%%DATE:~-7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
SET BACKUP_DATE=%BACKUP_DATE: =0%

REM Full backup path
SET FULL_BACKUP_PATH=%BACKUP_DIR%\n8n-backup-%BACKUP_DATE%

REM ================================================================
REM Backup Process
REM ================================================================

echo ================================================================
echo n8n Backup Utility
echo ================================================================
echo.
echo Backup will be saved to: %FULL_BACKUP_PATH%
echo.

REM Create backup directory if it doesn't exist
if not exist "%BACKUP_DIR%" (
    echo Creating backup directory...
    mkdir "%BACKUP_DIR%"
)

REM Create timestamped backup folder
echo Creating backup folder...
mkdir "%FULL_BACKUP_PATH%"

REM ================================================================
REM Backup n8n Data Directory
REM ================================================================
echo.
echo [1/4] Backing up n8n data directory...

if exist "%N8N_DATA_DIR%" (
    xcopy "%N8N_DATA_DIR%" "%FULL_BACKUP_PATH%\.n8n\" /E /I /H /Y
    echo   ✓ Data directory backed up
) else (
    echo   ✗ Warning: n8n data directory not found at %N8N_DATA_DIR%
)

REM ================================================================
REM Export Environment Variables
REM ================================================================
echo.
echo [2/4] Exporting environment variables...

SET ENV_FILE=%FULL_BACKUP_PATH%\environment-variables.txt

echo # n8n Environment Variables Backup > "%ENV_FILE%"
echo # Created: %DATE% %TIME% >> "%ENV_FILE%"
echo. >> "%ENV_FILE%"

REM List important n8n environment variables
echo N8N_PORT=%N8N_PORT% >> "%ENV_FILE%"
echo N8N_BASIC_AUTH_ACTIVE=%N8N_BASIC_AUTH_ACTIVE% >> "%ENV_FILE%"
echo N8N_BASIC_AUTH_USER=%N8N_BASIC_AUTH_USER% >> "%ENV_FILE%"
echo GENERIC_TIMEZONE=%GENERIC_TIMEZONE% >> "%ENV_FILE%"
echo N8N_ENCRYPTION_KEY=%N8N_ENCRYPTION_KEY% >> "%ENV_FILE%"
echo N8N_USER_FOLDER=%N8N_USER_FOLDER% >> "%ENV_FILE%"
echo DB_TYPE=%DB_TYPE% >> "%ENV_FILE%"

echo   ✓ Environment variables exported

REM ================================================================
REM Document Installation Method
REM ================================================================
echo.
echo [3/4] Documenting installation details...

SET INFO_FILE=%FULL_BACKUP_PATH%\installation-info.txt

echo # n8n Installation Information > "%INFO_FILE%"
echo # Created: %DATE% %TIME% >> "%INFO_FILE%"
echo. >> "%INFO_FILE%"

REM Check if n8n is installed via npm
where n8n >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Installation Method: npm >> "%INFO_FILE%"
    for /f "tokens=*" %%i in ('n8n --version 2^>nul') do echo n8n Version: %%i >> "%INFO_FILE%"
    for /f "tokens=*" %%i in ('node --version 2^>nul') do echo Node.js Version: %%i >> "%INFO_FILE%"
    for /f "tokens=*" %%i in ('npm --version 2^>nul') do echo npm Version: %%i >> "%INFO_FILE%"
) else (
    echo Installation Method: Docker or not found >> "%INFO_FILE%"
)

echo Windows Version: %OS% >> "%INFO_FILE%"
echo Computer Name: %COMPUTERNAME% >> "%INFO_FILE%"
echo Username: %USERNAME% >> "%INFO_FILE%"

echo   ✓ Installation details documented

REM ================================================================
REM Create Backup Manifest
REM ================================================================
echo.
echo [4/4] Creating backup manifest...

SET MANIFEST_FILE=%FULL_BACKUP_PATH%\BACKUP-MANIFEST.txt

echo ================================================================ > "%MANIFEST_FILE%"
echo n8n BACKUP MANIFEST >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo Backup Date: %DATE% %TIME% >> "%MANIFEST_FILE%"
echo Backup Location: %FULL_BACKUP_PATH% >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"
echo CONTENTS >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo [✓] .n8n\                      - Complete n8n data directory >> "%MANIFEST_FILE%"
echo     - database.sqlite          - SQLite database with workflows >> "%MANIFEST_FILE%"
echo     - config                   - Configuration file >> "%MANIFEST_FILE%"
echo     - credentials.json         - Encrypted credentials >> "%MANIFEST_FILE%"
echo     - .n8n-encryption-key      - Encryption key (CRITICAL!) >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo [✓] environment-variables.txt - Environment variable settings >> "%MANIFEST_FILE%"
echo [✓] installation-info.txt     - Installation details >> "%MANIFEST_FILE%"
echo [✓] BACKUP-MANIFEST.txt       - This file >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"
echo RESTORATION INSTRUCTIONS >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo 1. Install n8n (same method as original installation) >> "%MANIFEST_FILE%"
echo 2. Stop n8n if it's running >> "%MANIFEST_FILE%"
echo 3. Copy .n8n folder to: %USERPROFILE%\.n8n >> "%MANIFEST_FILE%"
echo 4. Restore environment variables from environment-variables.txt >> "%MANIFEST_FILE%"
echo 5. Start n8n and verify workflows are restored >> "%MANIFEST_FILE%"
echo. >> "%MANIFEST_FILE%"
echo IMPORTANT: The encryption key must match exactly! >> "%MANIFEST_FILE%"
echo ================================================================ >> "%MANIFEST_FILE%"

echo   ✓ Backup manifest created

REM ================================================================
REM Backup Complete
REM ================================================================
echo.
echo ================================================================
echo Backup Complete!
echo ================================================================
echo.
echo Backup saved to: %FULL_BACKUP_PATH%
echo.
echo Files backed up:
echo   - n8n data directory (.n8n folder)
echo   - Environment variables
echo   - Installation information
echo   - Backup manifest
echo.
echo IMPORTANT: Store this backup in a safe location!
echo   - Copy to external drive
echo   - Upload to cloud storage (encrypted)
echo   - Keep encryption key secure
echo.

REM ================================================================
REM Optional: Create ZIP Archive
REM ================================================================
echo Do you want to create a ZIP archive of this backup? (Y/N)
set /p CREATE_ZIP=

if /i "%CREATE_ZIP%"=="Y" (
    echo.
    echo Creating ZIP archive...

    REM Check if PowerShell is available (for compression)
    where powershell >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        powershell Compress-Archive -Path "%FULL_BACKUP_PATH%" -DestinationPath "%BACKUP_DIR%\n8n-backup-%BACKUP_DATE%.zip"
        echo   ✓ ZIP archive created: %BACKUP_DIR%\n8n-backup-%BACKUP_DATE%.zip
    ) else (
        echo   ✗ PowerShell not found - cannot create ZIP archive
        echo   ℹ Manual compression recommended
    )
)

echo.
echo Press any key to exit...
pause >nul

ENDLOCAL
