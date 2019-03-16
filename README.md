# Instructions for setup

#### Before beginning:
1. Make sure Docker and Git are installed
2. Make sure you are logged in to Docker and GitHub
2. Pick a directory to work out of, e.g. C:\Users\YourName\Project_4

#### Setting up
1. Clone nathanhtaylor/Project-4 to your directory:
`$ git clone git://github.com/nathanhtaylor/project-4.git` (or use the GitHub app)

2. `cd` into .\Project-4:
`$ cd .\Project-4\`

3. Build our Docker image:
`$ docker build --tag=server .`

4. Run the Docker image:
`$ docker run --rm -it -p 5000:5000 server`

This will send the contents of server.py to `http://localhost:5000` and then delete the container once you Ctrl+C to stop.

#### Making changes
To work on files that are being used by Flask, the docker image must be rebuilt to reflect changes by repeating steps 3 and 4.

The `Dockerfile` and `requirements.txt` files are what Docker uses to build the image. If your code needs a specific library (for example `import re`)
then you can add them to the `requirements.txt`.

Post all questions and requests in Slack and I will help however I can.
