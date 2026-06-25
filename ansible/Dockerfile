FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssh-server sudo python3 python3-apt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash ynov && \
    echo "ynov:ynov" | chpasswd && \
    adduser ynov sudo && \
    echo 'ynov ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN mkdir -p /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    echo 'AllowUsers ynov' >> /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# RUN mkdir -p /home/ynov/.ssh add your own ssh key here
# COPY authorized_keys /home/ynov/.ssh/authorized_keys
# RUN chown -R ynov:ynov /home/ynov/.ssh && \
#     chmod 700 /home/ynov/.ssh && \
#     chmod 600 /home/ynov/.ssh/authorized_keys

EXPOSE 22
EXPOSE 90

CMD ["/usr/sbin/sshd", "-D"]
