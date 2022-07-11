FROM python:3.10
ADD src /usr/src/app/src
ADD setup.py /usr/src/app
ADD setup.cfg /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN python setup.py install
CMD ["jtv"]
