FROM        ubuntu:16.04

# some code from https://github.com/tambetm/gym-mincraft/blob/master/docker/Dockerfile
MAINTAINER  Reinforcement Learning KR <zzing0907@naver.com>

# update and install basic
RUN         apt-get update && apt-get upgrade -y
COPY        keyboard /etc/default
RUN         apt-get install wget unzip \
              build-essential python3-dev \
              python3-pip xvfb xsdcxx \
              xpra libgl1-mesa-dev -y

# install Malmo dependencies
RUN         apt-get install libboost-all-dev \
              libpython3.5-dev openjdk-8-jdk \
              libxerces-c3.1 ffmpeg python3-tk \
              python3-pil.imagetk -y

# download Malmo
WORKDIR     /root/
RUN         wget https://github.com/Microsoft/malmo/releases/download/0.34.0/Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip
RUN         unzip Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip
RUN         mv Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5 Malmo
RUN         rm Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip

# export path
ENV         MALMO_XSD_PATH /root/Malmo/Schemas

# build Malmo and start Malmo Client
RUN         mkdir ~/.gradle && echo 'org.gradle.daemon=true\n' > ~/.gradle/gradle.properties
WORKDIR     /root/Malmo/Minecraft
RUN         ./gradlew setupDecompWorkspace
RUN         ./gradlew build
COPY        run.sh /root/
RUN         chmod +x /root/run.sh

# if you want to use other port change this
ENV         PORT 10000
EXPOSE      $PORT

ENTRYPOINT  /root/run.sh /root/Malmo/Minecraft/launchClient.sh -port $PORT
