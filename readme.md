## Content
* _main.py_ : l'API
* _data.py_ : code python pour la connexion a la base de donnée
* _Dockerfile_ : Le docker file pour faire l'image de l'API
* _requirements.txt_ : les requirement pour l'API
## Déploiement de l'application Web FastAPI dans AWS
### Créer une application FastAPI

_main.py_ et _data.py_

### Dockerize l'application Fast API

1. Créer un fichier docker

_Dockerfile_

2. Créer une image Docker

```bash
docker build -t fastapi:latest .
```
### Transférer l'image Docker vers AWS ECR

Tout d'abord, vous devez installer et configurer l'AWS CLI pour transférer les images docker vers AWS ECR

1. Installez l'AWS CLI

Exécutez les deux commandes suivantes pour installer l'AWS CLI

```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"


sudo installer -pkg AWSCLIV2.pkg -target /
```

Vérifiez l'installation en exécutant la commande suivante

```bash
aws --version
```

Pour configurer l'AWS CLI, obtenez __access key ID__ et __Secret Access Key__ à partir de __Identity and Access Management (IAM)__ dans AWS

2. Configurer l'AWS CLI

```bash
aws configureAWS Access Key ID [None]:Your Acces Key ID
AWS Secret Access Key [None]:Your Acess Key
Default region name [None]:Your Region
Default output format [None]:json
```

3. Après avoir configuré l'AWS CLI, connectez-vous à AWS ECR à l'aide de la commande suivante, fournissez les détails __region__ et __account id__.

```bash
aws ecr get-login-password  --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```

4. Créer un référentiel

Vous pouvez créer un référentiel dans l'interface de ligne de commande ou directement dans la console AWS

```bash
aws ecr create-repository --repository-name fast_api_app
```
https://console.aws.amazon.com/ecr/repositories

5. Marquer votre image pour pouvoir la pousser vers ce référentiel

```bash
docker tag api:latest 
aws_account_id.dkr.ecr.region.amazonaws.com/fast_api_app
```
6. Exécutez la commande suivante pour pousser l'image docker vers le référentiel AWS

```bash
docker push 
aws_account_id.dkr.ecr.region.amazonaws.com/fast_api_app
```
### Déployer l'application FastAPI dans EC2

Modifiez les paramètres de sécurité en ajoutant une règle en utilisant TCP personnalisé comme type et portez comme 5000 et cliquez sur examiner et lancer l'instance. Ces configurations sont nécessaires à l'exécution de notre application Web

1. Connectez-vous à l'instance ec2 à l'aide de la commande suivante

```bash
ssh -i yourKey.pem ec2-user@yourEC2DNSIPv4public.compute.amazonaws.com
```
2. Configurez AWS comme vous l'avez fait précédemment

```bash
aws configureAWS Access Key ID [None]:Your Acces Key ID
AWS Secret Access Key [None]:Your Acess Key
Default region name [None]:Your Region
Default output format [None]:json
```

3. Exécutez les commandes suivantes pour ajouter un utilisateur ec2 afin d'exécuter des commandes docker

```bash
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart
```
Quittez l'instance et ssh dans l'instance EC2 à nouveau

4. Connectez-vous au registre Amazon ECR

```bash
aws ecr get-login --region region --no-include-email
```

5. __Copiez la sortie ci-dessus et exécutez-la dans la ligne de commande__. Une fois que vous êtes connecté avec succès à AWS ECR, vous pouvez voir «Connexion réussie» dans la console.

6. Extraire l'image docker d'AWS ECR

```bash
docker pull 
aws_account_id.dkr.ecr.region.amazonaws.com/fast_api_app:latest
```

7. Exécutez le conteneur Docker

```bash
docker run -p 5000:5000 aws_account_id.dkr.ecr.region.amazonaws.com/fast_api_app
```

8. Obtenez l'adresse IP publique IPv4 à partir de la page des détails de l'instance et ajoutez le port 5000 lors de son lancement dans le navigateur

## Épuisement des bases de données Postgres dans AWS

Créer une base de données postgres dans le service AWS RDS