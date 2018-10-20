## Git commands

`git branch -d branch_name` delete branch name

`git config --global color.ui auto` to get colored diff output

`git checkout` temporarily resets the code in working directory to the commit

`git checkout -b new_branchname` creating a new branch and switching to it

`git checkout master` if HEAD is in deattached state, run this 

`git checkout --track origin/<branch_name>` git checkout for remote branches

`git config list` lists all the global configuration

`git diff` shows changes made in unstaged files

`git diff --staged` shows changes in staged files with files in repository 

`git diff commit_old commit_new` diff between two commits

`git log` shows full change history, press 'q' to quit

`git log -p [file/directory]` shows full change history for file/directory 

`git log -n n` shows top 'n' commits, (e.g if n = 1, shows the most recent commit)

`git log --graph --oneline master branch_name` to see the visual representation of commit history

`git reset --soft HEAD~1`, if the changes have not been pushed to remote then it undo the most recent commit to staging area.

`git reset --hard` resets all the uncommited changes to last commit (can't be recovered)

`git reflog` all the commits that have been checkout recently

`git remote` displays all the remote URL

`git remote -v` displays the URL, -v means verbose

`git remote add remote_name url_link` to add a URL to the remote name

`git show commit_id` show difference with the parent  

`git merge from_branch` to merge changes from *from_branch* to *to_branch(master)*

`git push remote_name branch_name` this will send the files not present in the remote repository

`git push --force origin <branch name>` this will *overwrite* the remote repo.

### Notes
+ `HEAD` means current commit
+ `BRANCH` is a label for a commit, deleting a branch will delete the label not the commit history of the branch.
+ `MASTER`, the default branch name in Git. As you initially make commits you're given a master branch that points to the last commit you made. Every time you commit, it moves forward automatically.
+ `UPSTREAM`, the name usually given to the location of original repository. (`git pull UPSTREAM master` to sync your clone to the original repo)
+ `ORIGIN`, usually the name of url of your forked repository
+ Fast-forward merges, criteria - the branch moving 'into' is an ancestor branch of 'from' branch. In this case, renaming the label will be enough rather than creating a new commit.

### Errors and warnings

+ Should not be doing an octopus, octopus is a strategy of combining multiple versions of code together. This message appears at inappropriate combinations.
+ You are in 'detached head state', you can detach from HEAD if you move to previous versions. 

## Resources
* [Git initial setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
* [Visualize git branching](https://learngitbranching.js.org/?NODEMO)
* [Git with Bitbucket](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)
* [Syncing your fork](https://help.github.com/articles/syncing-a-fork/#platform-windows)
* [Delete a commit](https://www.clock.co.uk/insight/deleting-a-git-commit)
* [When to merge v/s when to rebase](https://www.derekgourlay.com/blog/git-when-to-merge-vs-when-to-rebase/)
* [Understanding git theory](https://www.sbf5.com/~cduan/technical/git/)
* [How do I force git pull](https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files)
* [Difference between different diff commands](https://stackoverflow.com/questions/3686452/what-are-the-differences-between-these-git-diff-commands)


[Go to top](#git-commands)
