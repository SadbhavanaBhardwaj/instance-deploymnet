KEY_PATH = "/home/sadbhavana/sadbhavana_key1.pem"
 
region_name = "ap-south-1"
 
 
commands = ['sudo apt-get update', 'sudo apt-get install --yes apt-transport-https ca-certificates curl gnupg-agent software-properties-common',
               'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -', 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"',
               'sudo apt-get update && sudo apt-get install --yes docker-ce docker-ce-cli containerd.io',\
               'docker -v', 'sudo docker run -d --name mynginx1 -p 80:80 nginx']