FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV PATH ${ANDROID_HOME}/tools:$ANDROID_HOME/platform-tools:$PATH
ENV PROJECT_WORKSPACE /root/workspace

VOLUME ${PROJECT_WORKSPACE}
WORKDIR ${PROJECT_WORKSPACE}

RUN    apt update \
    && apt install -y libc6-dev-i386 lib32z1 unzip wget default-jdk-headless expect \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN    wget https://services.gradle.org/distributions/gradle-3.5-bin.zip \
    && mkdir /opt/gradle \
    && unzip -d /opt/gradle gradle-3.5-bin.zip \
    && rm gradle-3.5-bin.zip

ENV PATH ${PATH}:/opt/gradle/gradle-3.5/bin

RUN    wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -O tools.zip \
    && unzip tools.zip -d $ANDROID_HOME \
    && rm tools.zip

RUN /usr/bin/expect -c \
    "spawn $ANDROID_HOME/tools/bin/sdkmanager \"platforms;android-25\" \"build-tools;25.0.2\"; set timeout -1; expect \"Accept? (y/N): \"; send \"y\r\n\"; expect done;"

RUN mkdir -p /root/workspace

CMD ["gradle", "assemble"]
