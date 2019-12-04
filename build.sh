#!/bin/bash

git pull

sudo docker build -t 172.23.43.15:5000/tqcloud/tisecret .
sudo docker push 172.23.43.15:5000/tqcloud/tisecret

#sudo docker build -t tisecret .
#sudo docker stop tisecret
#sudo docker run --rm -d -p 8000:8000 --name=tisecret \
#     -v /home/taojiayuan/tomcat-linux/webapps/webroot/WEB-INF/schedule:/workspace/static_root/schedule \
#     -v /home/taojiayuan/workspace/extra_report:/workspace/static_root/extra_report \
#     tisecret

