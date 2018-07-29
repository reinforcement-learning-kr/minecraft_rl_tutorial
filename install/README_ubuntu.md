# 우분투에서 말모 설치  

먼저 [여기](https://github.com/Microsoft/malmo/releases)서 본인의 환경에 맞는 pre-built버전의 말모를 받아야 합니다. 최신 버전으로 빌드된 말모를 받습니다. 현재 최신 버전은 0.34.0입니다. 여기서는 Ubuntu 16.04, python3.5, 말모 0.34.0 버전을 기본으로 설명하도록 하겠습니다. 

<br>

먼저 말모를 받아줍니자. 아래 bash코드들을 실행하거나 위의 링크에서 해당 버전을 다운로드 받아도 됩니다.  

```bash
$ cd ~
$ wget https://github.com/Microsoft/malmo/releases/download/0.34.0/Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip  
$ unzip Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip  
$ mv Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5 Malmo  
$ rm -f Malmo-0.34.0-Linux-Ubuntu-16.04-64bit_withBoost_Python3.5.zip  
```

<br>

말모를 위해 필요한 디펜던시들을 설치합니다.  

```bash
$ sudo apt-get install libboost-all-dev build-essential python3-dev \
					   libpython3.5 openjdk-8-jdk libxerces-c3.1 \
					   python3-tk python3-pil.imagetk libgl1-mesa-dev \
					   ffmpeg xsdcxx -y  
```

<br>

Malmo 폴더 안에 Schemas라는 폴더를 환경변수로 추가해줘야 합니다. 아래 환경변수를 ~/.bashrc에 추가해 줍니다. vim이나 nano, gedit같은 프로그램으로 ~/.bashrc 파일을 열어 맨 아랫줄에 아래 명령어를 추가해주면 됩니다.   

혹시 Malmo설치 경로가 다른경우 본인의 Malmo설치 경로안의 Schemas폴더를 환경변수로 추가해 줘야 합니다.   

```bash
export MALMO_XSD_PATH=$HOME/Malmo/Schemas #(or path/to/Malmo/Schemas)  
```

<br>

환경변수를 추가해줬으면 ~/.bashrc 파일을 실행해줍니다.  

```bash
$ source ~/.bashrc  
```

<br>

마지막으로 python에 필요한 라이브러리를 받습니다.  

```bash
$ sudo pip3 install pillow future  
```

<br>

이제 launchClient.sh를 실행하면 자동으로 말모 클라이언트가 빌드되고 실행됩니다.  

```bash
$ ./launchClient.sh  
```

화면이 켜지면서 마인크래프트가 실행되면 설치가 완료된 것입니다.  
클라이언트가 켜진 상태로 Python_Examples 폴더에서 run_mission.py를 실행해보고 에러 없이 실행된다면 강화학습을 적용하기만 하면 됩니다.  

<br>

### (Optional) 서버에서 말모 클라이언트 돌리기  

서버에서 돌리기 위해서 먼저 가상 디스플레이를 실행할 수 있도록 해야합니다. 위의 디펜던시에 추가로 아래 패키지를 더 설치합니다.  

```bash
$ sudo apt-get install xvfb xpra  
```

<br>

다른 과정은 위 과정과 같고 클라이언트를 실행할 때 가상 디스플레이에서 실행할 수 있도록 명령을 추가해 줍니다.

```bash
$ xvfb-run -a -e /dev/stdout -s '-screen 0 1400x900x24' ./launchClient.sh
```

<br>

또는 도커파일을 이용해 클라이언트를 도커 컨테이너로 실행할 수도 있습니다. 도커파일을 이용하는 방법은 README_docker.md를 보시면 됩니다.  