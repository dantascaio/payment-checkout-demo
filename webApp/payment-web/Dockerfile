
FROM node:18

# Define build time variables
ARG build_date
ARG vcs_ref
ARG versao=0.0.1
ARG BOM_PATH=/docker/fiap
ARG PROJECT_NAME=user_profile
ARG PROJECT_PATH=./user_profile

WORKDIR /usr/src/app

# Define environment variables that can be used in runtime
ENV VERSAO=${versao}

LABEL \
    org.label-schema.maintainer="Diogo Raul" \
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
RUN npm install

# Expose port 8000 to communicate with outside resources
EXPOSE 4200

# Execute the commands in entrypoint.sh
ENTRYPOINT ["npm", "start"]
