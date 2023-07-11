FROM python:latest

ENV HOME=/root
ENV APPDIR /usr/src/app
ENV PYTHONPATH ${PYTHONPATH}:${APPDIR}
WORKDIR ${APPDIR}
RUN pip install poetry
ENV PATH=${HOME}/.poetry/bin:${PATH}

ADD poetry.lock ${APPDIR}/
ADD pyproject.toml ${APPDIR}/
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . ${APPDIR}

ENTRYPOINT ["python", "/usr/src/app/main.py"]
