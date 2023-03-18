FROM python:3
COPY ./package.env /python/package.env
RUN pip install --no-cache-dir -r /python/package.env
COPY . /srv/
WORKDIR /srv/
CMD ["python", "./dreamsai_email/main.py"]
