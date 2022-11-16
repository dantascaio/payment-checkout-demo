
FROM python:3.9-alpine3.15

# Define build time variables
ARG build_date
ARG vcs_ref
ARG versao=0.0.1
ARG BOM_PATH=/docker/fiap
ARG PROJECT_NAME=payment_checkout_api
ARG PROJECT_PATH=./payment_checkout_api

WORKDIR /usr/src/app

# Define environment variables that can be used in runtime
ENV VERSAO=${versao}

LABEL \
    org.label-schema.maintainer="Caio Dantas <caioaires@gmail.com>" \
    org.label-schema.name="" \
    org.label-schema.license="MIT" \
    org.label-schema.version="$versao" \
    org.label-schema.vcs-ref="$vcs_ref" \
    org.label-schema.build-date="$build_date" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.dockerfile="${BOM_PATH}/Dockerfile"

# Save Bill of Materials to image. Não remova!
COPY README.md LICENSE Dockerfile ${BOM_PATH}/

COPY . .

# Upgrade pip to the most recent version
RUN pip install --no-cache-dir --upgrade pip && \
    # Install the application and all its related packages using the copied Wheel file
    pip install --no-cache-dir -e . 

# Set the working directory for the container
WORKDIR ${PROJECT_PATH}

# Run unit tests
RUN pytest tests

# Expose port 8000 to communicate with outside resources
EXPOSE 8000

# Execute the commands in entrypoint.sh
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]
