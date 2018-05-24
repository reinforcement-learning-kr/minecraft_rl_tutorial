# malmo window 튜토리얼

1. https://github.com/Microsoft/malmo/releases/download/0.34.0/Malmo-0.34.0-Windows-64bit_withBoost_Python3.6.zip  위 링크로 들어가서 malmo 파일을 다운로드 한 후 원하는 디렉터리에 압축 해제 시킵니다.
2. 디펜던시 설치 : malmo 실행을 위해서는 다음과 같은 것들이 필요합니다.
    *  OS 확인 : 64비트 운영체제 인지 확인합니다.
    * 7-zip :
        * http://7-zip.org/ 에 들어가서 "Download .exe 64-bit x86." 를 설치합니다.
    * FFMPEG :
        * http://ffmpeg.zeranoe.com/builds/ 에 들어가서 64-bit-Static 버전을 다운로드합니다.
        * C:\\ffmpeg 경로에 압축을 해제합니다.
            * bin 폴더가 C:\\ffmpeg\bin 경로여야 합니다!
        * 환경변수를 추가해 줍니다 ( 아래 참조 )
        * cmd창을 실행한 뒤 ffmpeg 명령을 입력해서 잘 동작하는지 확인합니다.
    * CodeSynthesis : http://www.codesynthesis.com/products/xsd/download.xhtml 에 들어가서 Code Synthesis를 설치합니다.
    * Python3 :  https://www.python.org/ 에 들어가서 다운로드 탭에 들어간 후, 3.6.5버전을 설치합니다.
    * JAVA SE Development Kit (JDK) :  http://www.oracle.com/technetwork/java/javase/downloads/index.html
        *  주의사항 : JAVA 8 이하버젼으로 설치하세요 !!
    * MS Visual Studio 2013 Redistrubutable (비쥬얼 스튜디오 IDE 가 아닙니다. 필수적으로 설치해 주세요) : https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package
    * 환경변수 설정 ( 하단 참조 )

3. 환경변수 설정 : 내 컴퓨터 -> 우클릭 -> 속성 -> 고급 -> 환경변수… -> 시스템 변수
    1. FFMPEG Path설정 :
        1. Path항목 찾은 후 편집 클릭
        2. 맨 마지막 문자 ‘;’ 옆에 경로 추가 + ‘;’ 입력
            1. ex) ~; C:\\FFMPEG;
        3. 저장
    2. 설치폴더 Path설정 :
        1. 새로 만들기 클릭
        2. 이름을 ‘MALMO_XSD_PATH’ 로 지정
        3. 경로 추가
        4. 저장

