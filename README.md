# Instructions for setup

### Before beginning:
1. Make sure Docker and Git are installed
2. Make sure you are logged in to Docker and GitHub
3. Pick a directory to work out of, e.g. C:\Users\YourName\Project_4

### Running Docker
1. Pull docker image `$ docker pull nathanhtaylor/project-4:v2`
2. Run docker image `$ docker run --rm -p 5000:5000 server`

### Rerunning Docker 
1. List containers `docker ps -a`
2. Find the most recent container that has "0.0.0.0:5000->5000/tcp" next to it and copy its ID, like "a5421a994dbd"
3. Delete the container `docker kill xxxxxxxxxx`
2. Run docker image again `$ docker run --rm -p 5000:5000 server`

### Making changes
**Make sure that code is written inside of server.py so that all paths work together!**

The `Dockerfile` and `requirements.txt` files are what Docker uses to build the image. If your code needs a specific library (for example `import re`)
then you can add them to the `requirements.txt`.

Post all questions and requests in Slack and I will help however I can.
