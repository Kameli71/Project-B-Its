FROM python:3.9-slim-bullseye AS build

WORKDIR /api
COPY ./requirements.txt .
RUN pip install --disable-pip-version-check --target ./packages -r requirements.txt

COPY . .
RUN mkdir /logs && touch /logs/access.log /logs/error.log

FROM gcr.io/distroless/python3-debian11

ENV PYTHONPATH=/api/packages
WORKDIR /api
COPY --from=build /api /api
COPY --from=build /logs /logs

ENTRYPOINT ["python", "-m", "gunicorn", "-w 4", "--access-logfile", "/logs/access.log", "--error-logfile", "/logs/error.log", "-b :5051", "app:app"] 
# CMD "-m gunicorn -w 4 --access-logfile /logs/access.log --error-logfile /logs/error.log -b :5051 app:app" 
# CMD ["-m", "gunicorn",  "-w 4",  "-b :5051",  "app:app"] 
# CMD ["ls -la"]