Project 1 Rubric Questions
---

Name: Elizabeth Wright
---

Setup:
---
1. Setup for repositories: To setup a repository, use "git init --bare newrepo2". Check that the repository is a repository by checking that it has branches, hooks, etc. using ls -lah. I then cloned this repository by using "git clone ubuntu@52.3.67.147:/home/ubuntu/newrepo2". I then check the repository was successfully cloned by using "ls -lah" and checking the repository has a ".git" folder.
2. Users, folders, permissions:
 - Users: I set up a user using "git config --global user.name "Elizabeth"". Omit "--global" if the identity is only for the one repository. 
 - Folders: There is a difference in the folders that are in a remote repository and a cloned repository. The remote repository holds folders involved in making the repository work how it is expected to, such as the "branches" directory which is involved in the editing/commiting process cloned repositories use. Cloned repositories hold a .git folder, which is what is used to store information about your repository over time. 
 - Permissions: Permissions of each file and folder in the remote repository can be used by using "ls -lah". Read, write, and execute permissions for the user, group, and others can be seen, respectively. In the new remote repository specifically, defualt permissions for directories are for the user and group to be able to read, write, and execute; while others can only read and execute, which is why users of the repository can write and commit changes, instead of just anybody being able to edit the repository.
3. SSH key directions: cd to your ssh folder, vim authorized_keys, and add the public key to be authorized (could also use the public key that is already in the folder). I can then make my user I made has this key. This will allow the user I made to use the repository in an authorized way without putting a risk to their own system by using a private key.

Usage guide:
---
4. Clone usage and description: I used git clone to clone the repository I created. Clone is used to create a copy of the repository a which creates a foler, a copy of files that existed, and creates a connection back to the remote.
5. Init usage and description: I used init to create a new repository. Init is used to initialize an empty/new repository.
6. Add usage and description: I used add to track a test file I created. Add is used to add files to be tracked by the repository (if they are new).
7. Commit usage and description: I used commit to commit the change I made, aka the file I created, to the repository. Commits are snapshots of changes in the repository. A message has to be tied to each commit about what has changed.
8. Push usage and description: I used push to sync the changes I made on my terminal to the remote. Push is used to sync the local terminal to the remote.

Proof:
---
9. Screenshot(s) turned in via Pilot.
10. Screenshot(s) turned in via Pilot.
