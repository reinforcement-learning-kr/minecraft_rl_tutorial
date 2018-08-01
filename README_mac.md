# Mac에서 말모 설치  
malmo 공식 github은 다음과 같습니다. 
[https://github.com/Microsoft/malmo](https://github.com/Microsoft/malmo)

Malmo는 환경을 client로 에이전트를 server로 해서 통신하는 구조로 되어있습니다. 
설치해야하는 건 두 가지입니다. 차례로 설명드리겠습니다.
1. Minecraft: 환경 자체, client
2. Malmo: 환경과 python을 연결해서 python으로 환경에 접근해서 우리가 원하는 것들을 할 수 있도록 합니다. 

이 설치 가이드는 다음과 같은 설정에서 테스트한 것입니다. 
- python == 3.7
- mac os version ==  High Sierra 버전 10.13

<br>

## 1. Minecraft
환경을 설치하는 법은 크게 두 가지가 있습니다. pre-built된 것을 가져오는 방식과 build from source를 하는 방법입니다.
이 설치가이드에서는 pre-built된 것을 가져오도록 하겠습니다. 이 설치 가이드는 python 3.7을 사용하는 것을 가정하므로 다음 링크에서
python 3.7 버전인 'Malmo-0.35.6-MacOS_Python3.7.zip'을 다운로드 받습니다. 

[pre-built 버전 다운로드 링크](https://github.com/Microsoft/malmo/releases)

다운로드 받은 zip 파일의 압축을 풀고 malmo라는 이름으로 폴더명을 바꿉니다.

이제 다운로드 받은 malmo 폴더 밑에 Minecraft 폴더로 들어가서 launchClient.sh를 실행합니다. 
그러면 자동으로 malmo의 클라이언트가 빌드되고 실행됩니다.  


```bash
$ cd malmo/Minecraft
$ ./launchClient.sh  
```

화면이 켜지면서 Minecraft가 실행되면 설치가 완료된 것입니다.  
<img src="https://www.dropbox.com/s/h84woj932t1r674/Screenshot%202018-07-28%2013.58.23.png?dl=1">

- 주의사항:
1. 맥북의 os버전이 HighSiera(10.13) 이상 버전이어야 합니다. 맥의 os버전을 확인하세요.
2. Tensorflow사용자는 3.7 미만버전의 Python을 사용하세요.

<br>

## 2. Malmo 설치
Malmo 설치 방법은 상당히 간단합니다. 하지만 하나 염두에 두셔야할 것은 Malmo는 root python 만을 사용합니다. 따라서 
root에 python 3.7이 설치되어 있어야 합니다. 다음과 같이 pip로 설치하면 간단히 설치가 됩니다. 

```bash
$ pip3 install malmo
```
<br>

## 3. 예제 실행
설치가 제대로 되었는지 malmo에서 제공하는 example로 확인해보겠습니다.
아까 다운로드 받은 malmo 폴더에서 Python_Examples 폴더로 들어가봅니다. 
그 중에서 저희는 mob_fun.py를 실행해볼 것입니다. 하지만 build from source가 아니라 pip install로 설치한 경우 하나 수정해줘야합니다. 
mob_fun.py를 보면 상단에 다음과 같이 써있습니다. 

```python
from future import standard_library

standard_library.install_aliases()
from builtins import range
from past.utils import old_div
import MalmoPython
import os
import random
import sys
import time
import json
import random
import errno
import math
```

하나 고쳐야하는 것은 import MalmoPython을 import malmo.MalmoPython as MalmoPython 으로 수정해줘야합니다. 

```python
from future import standard_library

standard_library.install_aliases()
from builtins import range
from past.utils import old_div
import malmo.MalmoPython as MalmoPython
import os
import random
import sys
import time
import json
import random
import errno
import math
```
이렇게 수정한 이후에 클라이언트(Minecraft)를 실행하고 Python_Examples 폴더에서 mob_fun.py를 실행해보고 
에러 없이 실행된다면 강화학습을 적용하기만 하면 됩니다.  
