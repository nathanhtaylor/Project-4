FROM python:3.7
WORKDIR /usr/src/app
CMD [“sh”, “-c”, “git clone https://github.com/nathanhtaylor/Project-4.git && cd ./Project-4 && pip install -r requirements.txt && python server.py”]
