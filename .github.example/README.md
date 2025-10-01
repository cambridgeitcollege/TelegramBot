# GitHub Actions Configuration for Telegram Bot

This directory contains GitHub Actions workflows for automating various tasks in the Telegram Bot project.

## Workflows Overview

### 1. CI/CD Pipeline (`ci.yml`)
**Purpose**: Continuous Integration and Continuous Deployment

**Triggers**:
- Push to `main` and `develop` branches
- Pull requests to `main` branch

**Jobs**:
- **Test Job**: 
  - Runs on multiple Python versions (3.8, 3.9, 3.10, 3.11)
  - Installs dependencies and runs code quality checks
  - Performs syntax validation
  - Caches pip dependencies for faster builds

- **Build Job**: 
  - Creates deployment package
  - Uploads build artifacts
  - Only runs on `main` branch after successful tests

### 2. Scheduled Message Sender (`scheduled-message.yml`)
**Purpose**: Automated message sending to Telegram

**Triggers**:
- Scheduled daily at 9:00 AM UTC
- Manual workflow dispatch with custom message input

**Features**:
- Uses repository secrets for secure API key storage
- Supports custom messages via workflow dispatch
- Logs execution details
- Creates environment file dynamically

### 3. Code Quality Check (`code-quality.yml`)
**Purpose**: Automated code quality analysis

**Triggers**:
- Push to `main` and `develop` branches
- Pull requests to `main` branch

**Tools Used**:
- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Style guide enforcement
- **Bandit**: Security vulnerability scanning
- **Safety**: Dependency security checks
- **MyPy**: Static type checking
- **Pylint**: Code analysis

### 4. Auto Release (`release.yml`)
**Purpose**: Automated GitHub releases

**Triggers**:
- Git tags starting with 'v' (e.g., v1.0.0, v2.1.3)

**Features**:
- Creates GitHub releases automatically
- Generates release notes
- Packages project files into zip archive
- Uploads release assets

## Setup Instructions

### 1. Repository Secrets
Add these secrets in GitHub repository settings:

```
Settings → Secrets and variables → Actions → New repository secret
```

Required secrets:
- `BOTAPIKEY`: Your Telegram bot API token
- `CHATID`: Your Telegram chat or channel ID

### 2. Workflow Permissions
Ensure your repository has the following permissions:

```
Settings → Actions → General → Workflow permissions
```

Select: "Read and write permissions"

### 3. Branch Protection (Optional)
For production repositories, set up branch protection:

```
Settings → Branches → Add rule
```

Recommended rules for `main` branch:
- Require status checks to pass before merging
- Require up-to-date branches before merging
- Include administrators

## Usage Examples

### Manual Message Sending
1. Go to "Actions" tab in your repository
2. Select "Scheduled Message Sender"
3. Click "Run workflow"
4. Enter custom message (optional)
5. Click "Run workflow" button

### Creating a Release
```bash
# Create and push a new tag
git tag v1.0.0
git push origin v1.0.0

# This will trigger the auto-release workflow
```

### Monitoring Workflows
- View workflow runs in the "Actions" tab
- Check logs for debugging
- Download artifacts from successful builds

## Customization

### Changing Schedule
Edit the cron expression in `scheduled-message.yml`:

```yaml
schedule:
  - cron: '0 9 * * *'  # Daily at 9:00 AM UTC
```

### Adding New Quality Checks
Add new tools in `code-quality.yml`:

```yaml
- name: Run New Tool
  run: |
    pip install new-tool
    new-tool check .
```

### Modifying Python Versions
Update the matrix in `ci.yml`:

```yaml
strategy:
  matrix:
    python-version: [3.8, 3.9, '3.10', '3.11', '3.12']
```

## Best Practices

1. **Security**:
   - Never hardcode secrets in workflow files
   - Use repository secrets for sensitive data
   - Regularly rotate API keys

2. **Performance**:
   - Use caching for dependencies
   - Run jobs in parallel when possible
   - Limit artifact retention days

3. **Reliability**:
   - Add error handling in scripts
   - Use specific action versions (not @main)
   - Test workflows in feature branches

4. **Maintenance**:
   - Keep dependencies updated
   - Review workflow runs regularly
   - Document any custom modifications

## Troubleshooting

### Common Issues

1. **Secret Access Denied**:
   - Check secret names match exactly
   - Verify repository has correct permissions

2. **Python Version Issues**:
   - Ensure all versions in matrix are supported
   - Check dependency compatibility

3. **Workflow Not Triggering**:
   - Verify trigger conditions
   - Check branch names and paths

4. **Build Failures**:
   - Review logs for specific errors
   - Check dependency versions
   - Validate Python syntax

### Getting Help

- Check workflow run logs for detailed error messages
- Review GitHub Actions documentation
- Search GitHub Community forums
- Create issues in the repository for project-specific problems