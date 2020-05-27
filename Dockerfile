FROM python:3
ENV PYTHONUNBUFFERED 1

ADD ./.docker/wait-for-it.sh .

ADD ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --extra-index-url https://pip.expandshare.com/b00332a492824ae434ccf91112b6b1db

RUN mkdir /code
ADD ./src /code
WORKDIR /code
CMD python manage.py collectstatic --no-input && python manage.py migrate && gunicorn -b :8000 myproj.wsgi