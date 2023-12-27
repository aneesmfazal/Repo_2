print ("Hello World")


#First we need to initialise the repository
git init
#Wen need to add the repo from the remote e.g gitgub or azuredo to local
git remote add origin <link to repo>
#We need to fetch any changes from the remote and pull them locally
git fetch
#Checkout the main branch
git checkout main
#Here we are adding the file we want to commit
git add <filename>
#This returns the statu of what we are committing
git status
#This commits the changes
git commit -m "message"
#This pushes the change to the remote
git push