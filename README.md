# bitget_with_tradingview
aws서버에
/var/www/html에 GetAlert.php 업로드

/var/AutoBinance_dev에
main_seannie.py, bitget 폴더 업로드



----------------AWS서버 초기 필요 명령어 모음----------------
//확인 여부를 묻지 않고 업데이트를 설치
sudo yum update -y

//lamp-mariadb10.2-php7.2 및 php7.2 Amazon Linux Extras 리포지토리를 설치하여 Amazon Linux 2용 LAMP MariaDB 및 PHP 패키지의 최신 버전
sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2

//다음 명령을 사용하여 Amazon Linux 버전을 볼 수 있다
cat /etc/system-release

//yum install 명령을 사용하여 여러 소프트웨어 패키지와 모든 관련 종속 프로그램을 동시에 설치
sudo yum install -y httpd mariadb-server

//다음 명령을 사용하여 이러한 패키지의 현재 버전 확인
yum info [package_name]

//Apache 웹 서버를 시작
sudo systemctl start httpd

//systemctl 명령을 사용하여 Apache 웹 서버가 매번 시스템이 부팅할 때마다 시작
sudo systemctl enable httpd

//다음 명령을 실행하여 httpd가 실행되고 있는지 확인
sudo systemctl is-enabled httpd

//사용자(이 경우는 ec2-user)를 apache 그룹에 추가
sudo usermod -a -G apache ec2-user

//로그아웃하고 다시 로그인한 다음, 새 그룹을 선택하고 멤버십 확인
exit
groups

///var/www 및 그 콘텐츠의 그룹 소유권을 apache 그룹으로 변경
sudo chown -R ec2-user:apache /var/www

//그룹 쓰기 권한을 추가하여 나중에 하위 디렉터리에 대한 그룹 ID를 설정하려면 /var/www와 그 하위 디렉터리의 디렉터리 권한을 변경
sudo chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;

//그룹 쓰기 권한을 추가하려면 /var/www 및 그 하위 디렉터리의 파일 권한을 반복하여 변경
find /var/www -type f -exec sudo chmod 0664 {} \;

python3 --version

-- sudo 권한으로 autobot 폴더 생성
sudo mkdir /var/autobot

sudo chown -R ec2-user /var/autobot

sudo chmod 2775 /var/autobot

find /var/autobot -type d -exec sudo chmod 2775 {} \;

//이거필수
sudo -u apache python3 /var/autobot/main_seannie.py

-- 텔레그램 봇
sudo pip3 install python-telegram-bot --upgrade

sudo pip3 install pandas

sudo pip3 install pickle-mixin
