# Git Commands

Here are some useful Git commands

## Configure Git

```
git config --global user.name "Your name"
git config --global user.email <Your email>
```

## Working Locally

Create a new local repo

`git init`

Check current status of the repository and changes

`git status`

Add all changed files to staging area, which will be tracked by Git for any changes

` git add .`

Commit current changes to the local repo

```
git commit
git commit -m "Some Message"
```

Checking previous commits, messages, and their hash number

`git log`

Visit certain version of code with hash number

`git checkout <hash number>`

Reset the repo to a certain version with hash number

`git reset --hard <hash number>`

Revert a certain commit

`git revert <hash number>`

## Working with a Remote Repo

Synchronize remote repo to local device

`git clone <url>`

Send information to the remote repo

`git push`

Get information from remote repo
`git pull`

## Working with a Group

Create a new branch for a new feature

`git checkout -b <branch name>`

Constantly use `git pull`
