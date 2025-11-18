# Sample Scripts and Configuration Files

This directory contains ready-to-use scripts and configuration files for n8n on Windows.

## 📁 Contents

### Windows Batch Scripts

#### `start-n8n.bat`
**Purpose**: Start n8n with recommended environment variables

**Features**:
- Pre-configured environment variables
- Basic authentication enabled
- Timezone configuration
- Encryption key setup
- Optional PostgreSQL configuration
- Execution data pruning

**Usage**:
1. Copy to a convenient location (e.g., `C:\n8n\start-n8n.bat`)
2. Edit the file and customize:
   - `N8N_BASIC_AUTH_PASSWORD` - Set a strong password
   - `GENERIC_TIMEZONE` - Set your timezone
   - `N8N_ENCRYPTION_KEY` - Generate and set a 32-character key
3. Double-click to start n8n, or run from PowerShell

**Customization**:
```batch
# Generate encryption key with PowerShell:
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | % {[char]$_})

# Or use OpenSSL:
openssl rand -base64 32
```

---

#### `backup-n8n.bat`
**Purpose**: Create complete backup of n8n installation

**Features**:
- Backs up `.n8n` data directory
- Exports environment variables
- Documents installation details
- Creates restoration instructions
- Optional ZIP compression

**Usage**:
1. Copy to a convenient location
2. Run the script (double-click or from command prompt)
3. Backups are saved to `C:\n8n-backups\` by default
4. Store backups securely (external drive, cloud storage)

**What Gets Backed Up**:
- SQLite database (all workflows and executions)
- Credentials (encrypted)
- Encryption key (**CRITICAL!**)
- Configuration files
- Environment variables

**Restoration**:
1. Install n8n (same method as before)
2. Stop n8n
3. Copy `.n8n` folder from backup to `%USERPROFILE%\.n8n`
4. Restore environment variables
5. Start n8n

---

### Docker Configuration

#### `docker-compose.yml`
**Purpose**: Production-ready Docker Compose configuration

**Features**:
- n8n container with persistent volumes
- Basic authentication pre-configured
- Execution data pruning enabled
- Health checks included
- Optional PostgreSQL database (commented out)
- Resource limits (optional)
- Restart policy configured

**Usage**:
1. Copy to a directory (e.g., `C:\n8n-docker\`)
2. Edit environment variables:
   - `N8N_BASIC_AUTH_PASSWORD`
   - `N8N_ENCRYPTION_KEY`
   - `GENERIC_TIMEZONE`
3. Open PowerShell in that directory
4. Run: `docker compose up -d`
5. Access at: http://localhost:5678

**Common Commands**:
```powershell
# Start services
docker compose up -d

# Stop services
docker compose stop

# View logs
docker compose logs -f n8n

# Restart services
docker compose restart

# Update n8n
docker compose pull && docker compose up -d

# Remove everything (keeps data)
docker compose down

# Remove everything including data
docker compose down -v
```

**PostgreSQL Setup**:
1. Uncomment the `postgres` service section
2. Uncomment PostgreSQL environment variables in n8n service
3. Set a strong password for `POSTGRES_PASSWORD`
4. Run: `docker compose up -d`

---

### WSL2 Configuration

#### `.wslconfig`
**Purpose**: Optimize WSL2 resource usage for Docker Desktop

**Features**:
- Memory limit configuration
- CPU core allocation
- Swap space configuration
- Localhost forwarding
- Performance tuning

**Usage**:
1. Copy to: `%USERPROFILE%\.wslconfig`
   - Example: `C:\Users\YourName\.wslconfig`
2. Edit values based on your system RAM
3. Open PowerShell as Administrator
4. Run: `wsl --shutdown`
5. Restart Docker Desktop

**Recommended Settings by System RAM**:

| Total RAM | memory | processors | swap |
|-----------|--------|------------|------|
| 8 GB      | 3GB    | 2          | 1GB  |
| 16 GB     | 6GB    | 4          | 2GB  |
| 32 GB     | 12GB   | 4-8        | 4GB  |
| 64 GB     | 24GB   | 8-16       | 8GB  |

**Performance Impact**:
- **Before**: WSL2 can use 8-16GB RAM on a 16GB system (50-100%)
- **After**: WSL2 limited to configured amount (e.g., 6GB = 37.5%)
- **Battery Life**: Reduced CPU cores = better battery life on laptops

---

## 🔧 Quick Start Guides

### For npm Installation

1. **Start n8n with custom settings**:
   ```powershell
   # Use start-n8n.bat after customizing
   .\start-n8n.bat
   ```

2. **Create regular backups**:
   ```powershell
   # Run weekly or before updates
   .\backup-n8n.bat
   ```

### For Docker Installation

1. **Set up Docker Compose**:
   ```powershell
   # Copy docker-compose.yml to C:\n8n-docker\
   cd C:\n8n-docker
   docker compose up -d
   ```

2. **Optimize WSL2**:
   ```powershell
   # Copy .wslconfig to %USERPROFILE%
   copy .wslconfig %USERPROFILE%
   wsl --shutdown
   # Restart Docker Desktop
   ```

---

## 🔐 Security Recommendations

### Environment Variables
- **Never** commit passwords or encryption keys to version control
- **Always** use a password manager to generate strong passwords
- **Backup** your encryption key separately from your data

### Passwords
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, symbols
- Unique (don't reuse from other services)

### Encryption Keys
- Generate cryptographically random keys
- 32 characters minimum
- Backup in multiple secure locations
- **Critical**: Without this key, credentials cannot be recovered

### Firewall
- Keep Windows Firewall enabled
- Only allow n8n port (5678) from trusted networks
- Use basic authentication for all network-accessible installations

---

## 📝 Customization Tips

### start-n8n.bat

**Change port**:
```batch
SET N8N_PORT=8080
```

**Add webhook URL**:
```batch
SET WEBHOOK_URL=https://yourdomain.com/
```

**Use custom data directory**:
```batch
SET N8N_USER_FOLDER=D:\n8n-data
```

### docker-compose.yml

**Change port mapping**:
```yaml
ports:
  - "8080:5678"  # Access on port 8080
```

**Add resource limits**:
```yaml
deploy:
  resources:
    limits:
      cpus: '2.0'
      memory: 2G
```

**Mount local files**:
```yaml
volumes:
  - n8n_data:/home/node/.n8n
  - ./my-files:/files  # Add this line
```

### .wslconfig

**Laptop battery saving**:
```ini
memory=3GB
processors=2
swap=1GB
```

**Desktop performance**:
```ini
memory=8GB
processors=8
swap=4GB
```

---

## 🆘 Troubleshooting

### Script won't run
- **Right-click** → **Edit** to view the script
- Check for syntax errors (missing quotes, typos)
- Run from PowerShell with: `.\script-name.bat`
- Check execution policy: `Get-ExecutionPolicy`

### Docker Compose errors
- Verify Docker Desktop is running
- Check for typos in YAML file (indentation matters!)
- Ensure no conflicting containers: `docker ps -a`
- Check logs: `docker compose logs`

### WSL2 not applying changes
- Ensure file is at `%USERPROFILE%\.wslconfig` exactly
- Run `wsl --shutdown` and wait 10 seconds
- Restart Docker Desktop completely
- Verify with: `wsl --status`

### Backup script fails
- Check disk space: `dir C:\`
- Verify n8n data directory exists: `dir %USERPROFILE%\.n8n`
- Run as Administrator if permission errors occur

---

## 📚 Additional Resources

- [n8n Environment Variables Documentation](https://docs.n8n.io/hosting/configuration/environment-variables/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [WSL2 Configuration Documentation](https://docs.microsoft.com/en-us/windows/wsl/wsl-config)
- [Windows Batch Scripting Guide](https://ss64.com/nt/)

---

## 📞 Support

For issues with these scripts:
1. Check the troubleshooting section above
2. Review the course notebooks (especially Modules 02, 03, 06-10)
3. Consult n8n community forum: https://community.n8n.io/

---

**Last Updated**: 2025
**Tested On**: Windows 10 (Build 19041+), Windows 11
**Compatible With**: n8n 1.0+
