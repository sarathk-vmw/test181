FROM python:latest
RUN pip install Flask uwsgi requests redis 
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
USER uwsgi
WORKDIR /app
COPY app /app
COPY cmd.sh /
CMD ["/cmd.sh"]
