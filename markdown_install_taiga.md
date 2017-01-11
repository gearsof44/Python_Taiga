<p align="center" >
# Guide d'installation d'un environnement de développement Taiga sous Debian 8
</p>

### I- Installation Dépendances :

```bash
sudo apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev
sudo apt-get install -y libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev
sudo apt-get install -y automake libtool libffi-dev curl git tmux gettext
```

### II- Installation de postgresql :

```bash
echo "deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main" | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install postgresql-9.5 postgresql-contrib-9.5
sudo apt-get install postgresql-doc-9.5 postgresql-server-dev-9.5
```

### III- Paramétrage postgresql :


* A faire depuis la machine host :
```bash
  sudo -u postgres psql -c "CREATE ROLE taiga LOGIN PASSWORD 'changeme';"
  sudo -u postgres createdb taiga -O taiga
  echo 'local all taiga peer' | sudo -u postgres tee -a /etc/postgresql/9.5/main/pg_hba.conf > /dev/null
  sudo service postgresql restart
```

### IV- Installation et paramétrage de Python :

```bash
sudo apt-get install libpq-dev
sudo apt-get install libssl-dev
sudo apt-get install openssl
sudo apt-get install libbz2-dev
wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
tar zxvf Python-3.5.0.tgz
cd Python-3.5.0
./configure
make
sudo make install
sudo apt-get install -y python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper
sudo apt-get install libxml2-dev libxslt-dev
exec bash
```

### V- Téléchargement du code backend :

```bash
cd ~
git clone https://github.com/taigaio/taiga-back.git taiga-back
cd ~/taiga-back
git checkout stable
```

### VI- Téléchargement des dépendances liées à python

```bash
sudo pip install -U setuptools
mkvirtualenv -p /usr/local/bin/python3.5 taiga
pip install -U setuptools
sudo pip install ujson
sudo pip install setuptools wheel --upgrade
sudo pip install setuptools wheel pip  --upgrade
pip install -r requirements-devel.txt
```

### VII- Ajustement Django :

```bash
cd settings/
cp local.py.example local.py
nano local.py
```
Rajouter :
```bash
from .common import *
cd ..
```

### VIII- Remplir la base de donnée avec un projet/utilisateurs de base :

*	Config connection taiga :
  ```bash
  cd /etc/postgresql/9.5/main/
	sudo nano pg_hba.conf
  ```
	* ajouter comme ci-dessous la ligne :
      ```bash
			"# Database administrative login by Unix domain socket"
			local   all             postgres                                peer
			local   all             taiga                                   md5
      ```
```bash
sudo service postgresql restart
cd /home/monuser/taiga-back/
workon taiga
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py loaddata initial_role
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py sample_data
```

### IX- Lancer la partie back-end

```bash
sudo reboot
sudo service postgresql start
cd ~/taiga-back/
workon taiga
python manage.py runserver 0.0.0.0:8000/
```

### X- Installation de Ruby et Gems

```bash
sudo apt-get install -y ruby
gem install --user-install sass scss-lint
export PATH=~/.gem/ruby/2.3.0/bin:$PATH
exec bash -l
```

### XI- Installation de NodeJS , Gulp ET Bower

```bash
sudo apt-get install -y nodejs npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
echo "deb http://ftp.us.debian.org/debian wheezy-backports main" | 	sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install nodejs
sudo update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100
curl https://www.npmjs.com/install.sh | sudo sh
sudo npm install -g gulp bower
cd ~
git clone https://github.com/taigaio/taiga-front.git taiga-front
cd taiga-front
git checkout stable
npm install
bower install
npm cache clean -f
npm install -g n
sudo n stable
npm rebuild node-sass
sudo gem install scss_lint
npm install gulp-scss-lint --save-dev
```

### XII- Lancer le code côté front

```bash
cd ~/taiga-front
cd ~/taiga-front/dist/
cp conf.example.json conf.json
cd ..
gulp
```

### Après un relancement de la machine host pour que l’appli puisse être lancée :

* Ouvrir 2 consoles :
	* Console 1 :
		*	cd taiga-back
		*	sudo service postgresql start
		*	workon taiga
		*	python manage.py runserver 0.0.0.0:8000
	* Console 2 :
		*	cd taiga-front
		*	gulp
