FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y curl git sudo && \
    useradd -m user -u 1000 && \
    echo 'user:user' | chpasswd user && \
    echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user && \
    chown -R user /home && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --ignore-installed -r /tmp/requirements.txt

WORKDIR /home/dvc-5-demo-project-iris

USER user

RUN sudo jupyter contrib nbextension install && \
    jupyter nbextension enable toc2/main

ARG GIT_CONFIG_USER_NAME
ARG GIT_CONFIG_EMAIL

RUN git config --global user.name $GIT_CONFIG_USER_NAME && \
    git config --global user.email $GIT_CONFIG_EMAIL

CMD jupyter notebook --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token=''

