FROM python:3.7

RUN pip install --ignore-installed dvc==0.82.6 \
                                   joblib==0.14.1 \
                                   jupyter==1.0.0 \
                                   jupyterlab==1.2.6 \
                                   matplotlib==3.1.2 \
                                   numpy==1.18.1 \
                                   pandas==1.0.0 \
                                   pyyaml==5.3 \
                                   scikit-learn==0.22.1 \
                                   scipy==1.4.1 \
                                   tqdm==4.42.0

RUN apt-get update && \
    apt-get install -y apt-transport-https sudo unzip wget && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y nodejs && \
    jupyter labextension install @jupyterlab/toc


RUN useradd -m user -u 1000 && \
    echo 'user:user' | chpasswd user

ARG GIT_CONFIG_USER_NAME
ARG GIT_CONFIG_EMAIL

WORKDIR /home/dvc-2-iris-demo

RUN echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user && \
    chown -R user /home

USER user

RUN git config --global user.name $GIT_CONFIG_USER_NAME && \
    git config --global user.email $GIT_CONFIG_EMAIL

CMD jupyter lab --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token=''

