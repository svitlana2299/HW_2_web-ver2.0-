FROM python:3.11

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

RUN python --version
RUN pipenv install --system --deploy
RUN pip install pipenv

EXPOSE 5000

ENTRYPOINT ["pipenv", "run", "python", "main.py"]
