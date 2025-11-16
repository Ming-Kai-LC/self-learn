# Project Name

Brief description of what this project does.

## Project Structure

```
project/
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── config/           # Configuration files
└── scripts/          # Utility scripts
```

## Tech Stack

- **Language**: [Python/JavaScript/etc.]
- **Framework**: [Flask/React/etc.]
- **Database**: [PostgreSQL/MongoDB/etc.]
- **Testing**: [pytest/Jest/etc.]
- **Build Tool**: [npm/webpack/etc.]

## Development Setup

### Prerequisites
- [Tool 1] version X.X
- [Tool 2] version X.X

### Installation
```bash
# Clone the repository
git clone [repo-url]

# Install dependencies
[installation command]

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations/setup
[setup commands]
```

### Running Locally
```bash
# Development server
[dev command]

# Run tests
[test command]

# Build
[build command]
```

## Coding Standards

### Python
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for all public functions/classes

### JavaScript/TypeScript
- Use ESLint configuration
- Prefer const over let
- Use async/await over promises
- Write JSDoc comments for public APIs

### General
- Write meaningful commit messages
- Add tests for new features
- Update documentation
- Run linter before committing

## Architecture Overview

### Key Components
1. **Component 1**: Description and responsibility
2. **Component 2**: Description and responsibility
3. **Component 3**: Description and responsibility

### Data Flow
[Explain how data flows through the system]

### Authentication
[Explain authentication mechanism]

### Error Handling
[Explain error handling strategy]

## Common Tasks

### Adding a New Feature
1. Create feature branch: `git checkout -b feature/feature-name`
2. Implement feature with tests
3. Run test suite: `[test command]`
4. Create pull request
5. Address review feedback
6. Merge after approval

### Fixing a Bug
1. Create branch: `git checkout -b fix/bug-description`
2. Write failing test demonstrating bug
3. Fix the bug
4. Verify test passes
5. Create pull request

### Running Tests
```bash
# All tests
[test command]

# Specific file
[test file command]

# With coverage
[coverage command]
```

### Database Migrations
```bash
# Create migration
[migration create command]

# Run migrations
[migration run command]

# Rollback
[migration rollback command]
```

## Troubleshooting

### Common Issues

**Issue: [Common problem]**
Solution: [How to fix it]

**Issue: [Another common problem]**
Solution: [How to fix it]

## Git Workflow

1. Create feature branch from `main`
2. Make changes with clear commits
3. Push branch and create PR
4. Request review from team
5. Address feedback
6. Squash merge to `main`

### Branch Naming
- Features: `feature/description`
- Fixes: `fix/description`
- Chores: `chore/description`
- Hotfixes: `hotfix/description`

### Commit Messages
```
type(scope): brief description

Detailed explanation (if needed)

Closes #123
```

Types: feat, fix, docs, style, refactor, test, chore

## Testing Strategy

- Unit tests for business logic
- Integration tests for API endpoints
- E2E tests for critical user flows
- Aim for 80%+ code coverage
- Mock external dependencies

## Deployment

### Environments
- **Development**: Auto-deploy from `develop` branch
- **Staging**: Auto-deploy from `staging` branch
- **Production**: Manual deploy from `main` branch

### Deployment Process
1. Merge PR to appropriate branch
2. CI/CD pipeline runs tests
3. Build passes → auto deploy (dev/staging)
4. Production requires manual approval

## Resources

- [Link to API documentation]
- [Link to design system]
- [Link to team wiki]
- [Link to project board]

## Contact

- Tech Lead: [Name/Email]
- Team Channel: [Slack/Teams channel]
- Repository: [GitHub/GitLab URL]

## Notes for Claude Code

- **Main language**: [Language]
- **Testing command**: `[command]`
- **Lint command**: `[command]`
- **Critical files**: Don't modify without asking: [list files]
- **Auto-format**: Use [formatter] for [file types]
- **Branch protection**: Never force-push to `main`

### Preferred Patterns
- Use [pattern] for [use case]
- Avoid [anti-pattern]
- Follow [architectural principle]

### Common Commands
```bash
# Start dev server
[command]

# Run tests
[command]

# Build production
[command]

# Database operations
[command]
```
