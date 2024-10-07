## Project Intial Setup

```
echo "# MLProjects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/risarora/MLProjects.git
git push -u origin main

```

## Project Setup

- **Create setup.py**
- **add '-e .' to requirements.txt**
- **pip install '-e '**

## git add, commit and push Changes

```
PS D:\Workspaces\MLProjects> git add .
warning: in the working copy of 'MLproject.egg-info/SOURCES.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'MLproject.egg-info/dependency_links.txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'MLproject.egg-info/top_level.txt', LF will be replaced by CRLF the next time Git touches it
PS D:\Workspaces\MLProjects> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   MLproject.egg-info/PKG-INFO
        new file:   MLproject.egg-info/SOURCES.txt
        new file:   MLproject.egg-info/dependency_links.txt
        new file:   MLproject.egg-info/top_level.txt
        modified:   README.md
        modified:   requirements.txt
        new file:   setup.py
        new file:   src/__init__.py

PS D:\Workspaces\MLProjects> git commit -m "setup"
[main 8e95c51] setup
 8 files changed, 47 insertions(+), 1 deletion(-)
 create mode 100644 MLproject.egg-info/PKG-INFO
 create mode 100644 MLproject.egg-info/SOURCES.txt
 create mode 100644 MLproject.egg-info/dependency_links.txt
 create mode 100644 MLproject.egg-info/top_level.txt
 create mode 100644 setup.py
 create mode 100644 src/__init__.py
PS D:\Workspaces\MLProjects> git push -u origin main
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 12 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (12/12), 1.28 KiB | 657.00 KiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/risarora/MLProjects.git
   2eaa9d8..8e95c51  main -> main
branch 'main' set up to track 'origin/main'.
PS D:\Workspaces\MLProjects>

```
