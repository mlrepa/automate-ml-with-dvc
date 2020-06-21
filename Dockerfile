FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y apt-transport-https curl git sudo unzip wget && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs

RUN useradd -m user -u 1000 && \
    echo 'user:user' | chpasswd user && \
    echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user && \
    chown -R user /home

ARG GIT_CONFIG_USER_NAME
ARG GIT_CONFIG_EMAIL

WORKDIR /home/dvc-2-iris-demo

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --ignore-installed -r /tmp/requirements.txt

RUN jupyter labextension install @jupyterlab/toc

USER user

RUN git config --global user.name $GIT_CONFIG_USER_NAME && \
    git config --global user.email $GIT_CONFIG_EMAIL

CMD jupyter lab --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token=''

