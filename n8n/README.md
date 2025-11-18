# n8n Windows Automation - Complete Learning Path

A comprehensive educational course for setting up, securing, and optimizing n8n workflow automation on Windows systems.

## 📚 Course Overview

This course provides a complete, beginner-to-advanced learning path for running n8n on Windows. Whether you're automating personal workflows on a laptop or deploying production automation for your business, this course covers everything you need to know.

### What You'll Learn

✅ Install n8n on Windows using multiple methods (npm, Docker, WSL2)
✅ Create and manage automated workflows
✅ Secure your installation with authentication and encryption
✅ Optimize performance for laptop or server deployments
✅ Configure automatic startup and maintenance procedures
✅ Make informed decisions about production deployment strategies

### Who This Course Is For

- **Beginners**: No prior knowledge needed - start from scratch
- **Windows Users**: Specifically tailored for Windows 10/11 environments
- **Self-Hosters**: Learn to run n8n locally instead of cloud services
- **Business Users**: Deploy production-ready workflow automation
- **Privacy-Conscious**: Keep your data on your own hardware

## 🎯 Learning Path

### Beginner Track (Modules 00-05)
**Goal**: Get n8n installed and create your first workflows

| Module | Title | Difficulty | Time | Description |
|--------|-------|-----------|------|-------------|
| 00 | Setup and Introduction | ⭐ | 20 min | Understand n8n, check requirements, plan your installation |
| 01 | Installation Methods Comparison | ⭐ | 30 min | Compare npm vs Docker vs WSL2 with decision framework |
| 02 | npm Installation (Windows) | ⭐ | 45 min | Step-by-step Node.js and n8n installation |
| 03 | Docker Desktop Installation | ⭐⭐ | 60 min | Set up Docker with volumes and compose files |
| 04 | Initial Configuration & First Workflow | ⭐ | 45 min | Create account, build first workflows, test webhooks |
| 05 | Understanding Webhooks and Triggers | ⭐⭐ | 50 min | Master different trigger types and webhook security |

### Intermediate Track (Modules 06-08)
**Goal**: Secure your installation and optimize performance

| Module | Title | Difficulty | Time | Description |
|--------|-------|-----------|------|-------------|
| 06 | Security Best Practices | ⭐⭐ | 50 min | Authentication, encryption, firewall configuration |
| 07 | Performance Optimization (Windows) | ⭐⭐⭐ | 60 min | Memory, WSL2, battery life, database optimization |
| 08 | Auto-start Configuration | ⭐⭐ | 45 min | Task Scheduler, NSSM, PM2, Docker policies |

### Advanced Track (Modules 09-10)
**Goal**: Maintain and scale to production

| Module | Title | Difficulty | Time | Description |
|--------|-------|-----------|------|-------------|
| 09 | Updates and Maintenance | ⭐⭐ | 50 min | Backup, update, rollback, and migration procedures |
| 10 | Production Deployment Strategies | ⭐⭐⭐ | 55 min | Laptop vs server, PostgreSQL, reverse proxy, cost analysis |

**Total Course Time**: ~7 hours
**Total Exercises**: 33+ hands-on exercises

## 🚀 Quick Start

### Prerequisites

Before starting the course, ensure you have:

- **Windows 10** (Build 19041+) or **Windows 11**
- **4+ GB RAM** (8+ GB recommended)
- **20+ GB free disk space**
- **Administrator access** to your Windows computer
- **Internet connection** for downloads

### Installation Quick Reference

#### Option 1: npm Installation (Recommended for Beginners)

```powershell
# 1. Download and install Node.js LTS from nodejs.org
# 2. Open PowerShell as Administrator and run:
npm install n8n -g

# 3. Start n8n:
n8n

# 4. Open browser to:
http://localhost:5678
```

#### Option 2: Docker Desktop (Recommended for Production)

```powershell
# 1. Install Docker Desktop from docker.com
# 2. Create volume and run container:
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n --restart unless-stopped docker.n8n.io/n8nio/n8n

# 3. Open browser to:
http://localhost:5678
```

## 📂 Project Structure

```
n8n-windows-automation/
├── notebooks/                    # Educational Jupyter notebooks
│   ├── 00_setup_introduction.ipynb
│   ├── 01_installation_methods_comparison.ipynb
│   ├── 02_npm_installation_windows.ipynb
│   ├── 03_docker_desktop_installation.ipynb
│   ├── 04_initial_configuration_first_workflow.ipynb
│   ├── 05_understanding_webhooks_triggers.ipynb
│   ├── 06_security_best_practices.ipynb
│   ├── 07_performance_optimization_windows.ipynb
│   ├── 08_autostart_configuration.ipynb
│   ├── 09_updates_maintenance.ipynb
│   └── 10_production_deployment_strategies.ipynb
│
├── data/
│   ├── sample/                   # Sample configuration files
│   └── scripts/                  # Helper scripts
│
├── requirements.txt              # Python dependencies for notebooks
└── README.md                     # This file
```

## 🛠️ Setup Instructions for Course Materials

### 1. Clone or Download This Repository

```bash
git clone <repository-url>
cd n8n-windows-automation
```

### 2. Install Python and Jupyter

```powershell
# Install Python 3.8+ from python.org
# Then install requirements:
pip install -r requirements.txt

# Launch Jupyter:
jupyter notebook
```

### 3. Start with Module 00

Navigate to `notebooks/00_setup_introduction.ipynb` and begin your learning journey!

## 📊 Key Features of This Course

### Interactive Learning
- **33+ Hands-On Exercises**: Practice what you learn immediately
- **Python Tools**: Calculators, generators, validators, and analyzers
- **Real-World Examples**: Based on comprehensive n8n documentation
- **Progressive Difficulty**: Easy → Medium → Hard exercises in each module

### Windows-Specific Content
- **PowerShell Commands**: Windows-native administration
- **Batch Scripts**: Easy automation for Windows users
- **Windows Firewall**: Step-by-step security configuration
- **Task Scheduler**: Native Windows auto-start setup
- **WSL2 Optimization**: Memory and performance tuning

### Production-Ready
- **Security Best Practices**: Authentication, encryption, network security
- **Performance Optimization**: Memory, battery, database tuning
- **Maintenance Procedures**: Backup, update, rollback strategies
- **Cost Analysis**: Compare laptop, home server, cloud, and managed options

## 🎓 Learning Outcomes

After completing this course, you will be able to:

✅ **Install**: Set up n8n on Windows using npm or Docker
✅ **Configure**: Apply security, performance, and auto-start settings
✅ **Create**: Build automated workflows with various trigger types
✅ **Secure**: Protect installations with authentication and firewall rules
✅ **Optimize**: Tune memory, battery life, and database performance
✅ **Maintain**: Perform safe updates, backups, and rollbacks
✅ **Deploy**: Make informed production deployment decisions
✅ **Scale**: Migrate from laptop to server when needed

## 📖 Additional Resources

### Official Documentation
- [n8n Documentation](https://docs.n8n.io/)
- [n8n Community Forum](https://community.n8n.io/)
- [n8n GitHub Repository](https://github.com/n8n-io/n8n)

### Windows Resources
- [Windows PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/windows/)
- [WSL2 Documentation](https://docs.microsoft.com/en-us/windows/wsl/)

### Automation Ideas
- [n8n Workflow Templates](https://n8n.io/workflows)
- [Integration Nodes](https://docs.n8n.io/integrations/)

## 🤝 Contributing

Found an error or have suggestions? Contributions are welcome!

1. Open an issue describing the problem or enhancement
2. Submit a pull request with improvements
3. Share your automation workflows with the community

## 📝 License

This educational content is provided for learning purposes. n8n is licensed under the [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

## ⚡ Quick Reference Card

### Essential Commands

| Task | npm Method | Docker Method |
|------|-----------|---------------|
| **Install** | `npm install n8n -g` | `docker pull n8nio/n8n` |
| **Start** | `n8n` | `docker start n8n` |
| **Stop** | `Ctrl+C` | `docker stop n8n` |
| **Update** | `npm install n8n@latest -g` | `docker pull n8nio/n8n:latest` |
| **Check Version** | `n8n --version` | `docker exec n8n n8n --version` |

### Essential Environment Variables

```powershell
# Basic Authentication (REQUIRED for network access)
$env:N8N_BASIC_AUTH_ACTIVE="true"
$env:N8N_BASIC_AUTH_USER="admin"
$env:N8N_BASIC_AUTH_PASSWORD="your_secure_password"

# Timezone
$env:GENERIC_TIMEZONE="America/New_York"

# Custom Port
$env:N8N_PORT="5678"

# Encryption Key (backup this!)
$env:N8N_ENCRYPTION_KEY="your_32_character_random_key_here"
```

### Port Conflicts

If port 5678 is in use:

```powershell
# Find process using port
netstat -ano | findstr :5678

# Change n8n port
$env:N8N_PORT="8080"
```

### Access URLs

- **Local Access**: http://localhost:5678
- **Network Access**: http://YOUR_IP_ADDRESS:5678
- **With Tunnel**: Provided by `n8n start --tunnel`

## 🎯 Course Completion Checklist

Track your progress through the course:

- [ ] Module 00: Verified system requirements
- [ ] Module 01: Decided on installation method
- [ ] Module 02: Installed n8n via npm (or skipped)
- [ ] Module 03: Installed n8n via Docker (or skipped)
- [ ] Module 04: Created first workflow successfully
- [ ] Module 05: Tested webhooks and triggers
- [ ] Module 06: Configured security settings
- [ ] Module 07: Optimized performance
- [ ] Module 08: Set up auto-start
- [ ] Module 09: Tested backup and update procedures
- [ ] Module 10: Planned production deployment

**Congratulations on completing the course!** 🎉

---

## 💡 Need Help?

- **Course Issues**: Open an issue in this repository
- **n8n Questions**: Ask on the [n8n Community Forum](https://community.n8n.io/)
- **Bug Reports**: Report to [n8n GitHub Issues](https://github.com/n8n-io/n8n/issues)

## 🌟 Success Stories

Share your automation success stories! What workflows have you built with n8n on Windows?

---

**Happy Automating!** 🚀

*Last Updated: 2025*
*Course Version: 1.0*
*Compatible with: n8n 1.0+ on Windows 10/11*
