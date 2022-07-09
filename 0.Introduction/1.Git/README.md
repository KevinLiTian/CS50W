# Git

[Git](https://git-scm.com/) is a command line tool that will help us with version control in several different ways. Check some useful commands in the _Command.md_ file

- Git allows us to keep track of changes we make to our code by saving snapshots of our code at a given point in time
- Allowing us to easily synchronize code between different people working on the same project by allowing multiple people to pull information from and push information to a repository stored on the web
- Allowing us to make changes to and test out code on a different branch without altering our main code base, and then merging the two together
- Allowing us to revert back to earlier versions of our code if we realize we’ve made a mistake

In the above explanations, we used the word repository, which we haven’t explained yet. A Git repository is a file location where we’ll store all of the files related to a given project. These can either be remote (stored online) or local (stored on your computer)

## Github

Remote repositories have to be stored some places online, the most popular one is [Github](https://github.com/). GitHub is a website that allows us to store Git repositories remotely on the web. Another tool that comes with Github is [Github Desktop](https://desktop.github.com/), which simplifies command line to a GUI which can be understood by developers that aren't familiar with git command line

#### Create Remote Repository

Here's a quick overview of creating a repository on Github. Make sure that you have a GitHub account set up, if not, you can create one [here](https://github.com/)

- Click the + in the top-right corner, and then click “New repository”
- Create a repository name that describes your project
- (Optional) Provide a description for your repository
- Choose whether the repository should be public (visible to anyone on the web) or private (visible just to you and others you specifically grant access)
- (Optional) Decide whether you want to add a README, which is a file describing your new repository

#### Synchronize Local Repository

After creating a remote repository, one will want to synchronize this repository to their local devices and then make changes. The simplest way to do this is through the steps below:

- Make sure you have git command line installed on your computer by typing git into your terminal. If it is not installed, you can download it [here](https://git-scm.com/downloads)
- Click the green “Code” button on your repository’s page, and copy the url that pops down. If you didn’t create a README, this link will appear near the top of the page in the “Quick Setup” section
- In your terminal, run `git clone <repository url>`. This will download the repository to your computer. If you didn’t create a README, you will get the warning: `You appear to have cloned into an empty repository`. This is normal, and there’s no need to worry about it
- Run `ls` or `dir` if on Windows, which is a command that lists all files and folders in your current directory. You should see the name of the repository you’ve just cloned
- You can then use any text editor to make changes to the repository

## 4 Stages

Git specifies the workflow into 4 stages, local directory, staging area, local repository, and remote repository

- **Local Directory**: The changes one make is initially at local directory, untracked by Git
- **Staging Area**: Once one uses the command `git add .`, the changes in the local directory will be staged in the staging area, where the changes are tracked by Git, but not stored in local repo
- **Local Repo**: Once one uses the command `git commit`, the changes will be in the local repo
- **Remote Repo**: Once one uses the command `git push`, the local changes will be sent to and stored on Github

Figure 1

## Conflict

If there are multiple developers working on one project, conflicts are usually going to take place. Conflict happens when two developers changed the same line of code. Once one developer uses the command `git pull` to get information from the remote repo, if some lines of code in the remote repo have changed and they are also changed in the local repo, then there's conflict, which looks like this

```
a = 1
<<<<< HEAD
b = 2
=====
b = 3
>>>>> 56782736387980937883
c = 3
d = 4
e = 5
```

The line between `<<<<< HEAD` and `=====` is what's in local repo and the lline between `=====` and `>>>>> Some Hash Number` is what's on the remote repo. One should modify the file until satisfied and then commit and push the change to fix the conflict

## Branching

A project usually has multiple features that are developing by different people at the same time. If everyone is developing on a straight line so-to speak

Figure 2

The commits will become messy and untrackable if something went wrong since everyone's commits are together on the same line. Branching is introduced to avoid this situation. A branch can be thought as a completely different repo so that one can track one's work clearly. Then after the feature is finished, one will merge the branch back to the original main code base

Figure 3
