---
description: Deploy application to production with safety checks
allowed-tools: [Bash(git:*), Bash(npm:*), Bash(docker:*)]
argument-hint: [environment]
model: sonnet
---

# Deployment Checklist

You are deploying to the **$ARGUMENTS** environment.

## Pre-deployment Checks

Before deploying, verify:

1. **Git Status**
   Current status: !`git status --short`

2. **Current Branch**
   Branch: !`git branch --show-current`

3. **Tests Passing**
   Run the test suite to ensure all tests pass.

4. **No Uncommitted Changes**
   Ensure all changes are committed.

5. **Up to Date with Remote**
   Check: !`git fetch && git status`

## Deployment Steps

1. **Verify environment**: Confirm you want to deploy to **$ARGUMENTS**
2. **Run tests**: Execute full test suite
3. **Build application**: Create production build
4. **Deploy**: Push to deployment platform
5. **Verify deployment**: Check health endpoints
6. **Monitor**: Watch logs for errors

## Safety Checks

- ⚠️ Deploying to production requires explicit confirmation
- ⚠️ All tests must pass
- ⚠️ No uncommitted changes allowed
- ⚠️ Must be on correct branch

## After Deployment

1. Check application health
2. Monitor error rates
3. Verify key functionality
4. Update deployment log
5. Notify team

Would you like to proceed with deployment to **$ARGUMENTS**?
