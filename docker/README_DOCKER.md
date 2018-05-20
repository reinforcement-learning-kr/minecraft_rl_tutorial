# Docker 가이드    

도커를 이용해서 쉽게 서버에서 display없이 말모 클라이언트를 돌릴 수 있습니다. 현재는 우분투만 가능합니다.   

먼저 도커를 빌드 합니다. Dockerfile이 있는 폴더에서 다음 명령어를 실행하면 Dockerfile이 빌드됩니다.  

```bash
$ docker build -t malmo:0.34.0 .  
```

<br>

빌드가 끝나고 아래 명령어로 Docker 이미지를 확인하면 malmo 이미지가 있는 것을 확능인 할 수 있습니다.  

```bash
$ docker images  
```

<br>

도커가 이미지가 있는게 확인 됬다면 다음 명령어로 말모 클라이언트를 도커 컨테이너로 실행하실 수 있습니다.  

```bash
$ docker run --net=host -e PORT=10000 --name test malmo  
```

<br>

위 명령어에서 --name 옵션은 컨테이너 이름을 설정하는 옵션이고 -e PORT=10000 옵션은 말모 클라이언트의 포트를 설정해 주는 옵션입니다. 클라이언트를 여러 개 실행한다면 네트워크 포트를 바꿔주실 수 있습니다. (설정하지 않으면 자동으로 10000으로 설정됩니다.)

<br>

실행 후에는 다음 명령어로  돌아가고 있는 컨테이너를 확인할 수 있습니다. 꺼진 컨테이너도 확인하려면 -a 옵션을 이용할 수 있습니다.  

```bash
$ docker ps  
```

<br>

이후에 본인 환경에 맞는 말모 에이전트를 실행하면 실행되는 것을 확인 할 수 있습니다.  

<br>

#### Docker 설치    

우분투에서 설치하는 것은 아래 bash 스크립트를 터미널 창에서 실행하면 됩니다. 현재 Dockerfile은 우분투만 가능하나 윈도우나 맥에 도커를 설치하시고 싶으신 경우 [이곳](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)을 참고하세요.  

```bash
$ curl -fsSL https://get.docker.com/ | sudo sh  
```

<br>

docker 설치 후 그룹을 변경해 줘야 sudo 명령어 없이 docker가 실행됩니다.  

```bash
$ sudo usermod -aG docker $USER  
```
