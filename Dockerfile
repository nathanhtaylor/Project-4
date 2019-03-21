FROM python:3.7
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN git clone http://github.com/nathanhtaylor/Project-4
WORKDIR /usr/src/app/Project-4
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
