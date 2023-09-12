# Project-B-Its

## Utilisation
Pour lancer la stack prestashop (appli prestashop et base de données mariadb) :  
- dans le dossier  prestashop, créer les fichiers db.env et presta.env qui contiennent les variables d'environnement ;
- db.env doit contenir ces variables au format ```VAR=valeur``` :  

<table><tr><td>MYSQL_USER</td><td><em>identifiant_de_connexion_db</em></td></tr>
	<tr><td>MYSQL_PASSWORD</td><td><em>mot_de_passe_db</em></td></tr>
	<tr><td>MYSQL_DATABASE</td><td><em>nom_db</em></td></tr>
	<tr><td>MYSQL_ROOT_PASSWORD</td><td><em>mot_de_passe_root</em></td></tr></table>

- presta.env doit contenir ces variables :

<table>
	<tr><td>DB_SERVER</td><td>some-mysql</td></tr>
	<tr><td>DB_NAME</td><td><em>nom_db (doit être identique à celui donné dans db.env)</em></td></tr>
	<tr><td>DB_USER</td><td><em>identifiant_de_connexion_db (doit être identique à celui donné dans db.env)</em></td></tr>
	<tr><td>DB_PASSWD</td><td><em>mot_de_passe_db (doit être identique à celui donné dans db.env)</em></td></tr>
	<tr><td>PS_FOLDER_ADMIN</td><td><em>dossier_administration (ne doit pas être <b>admin</b>)</em></td></tr>
	<tr><td>PS_FOLDER_INSTALL</td><td><em>dossier_install (ne doit pas être <b>install</b>)</em></td></tr>
	<tr><td>PS_INSTALL_AUTO</td><td><em>1 (peut être ignorée ou laissée à 0 si on souhaite faire l'installation manuellement)</em></td></tr>
	<tr><td>PS_DOMAIN</td><td><em>adresse_site_prestashop</em></td></tr>
	<tr><td>ADMIN_MAIL</td><td><em>identifiant_de_connexion_admin_prestashop</em></td></tr>
	<tr><td>ADMIN_PASSWD</td><td><em>mot_de_passe_admin_prestashop</em></td></tr>
</table>

------
## Microservice Gestion API
Ce microservice sert à activer l'API de Prestashop et à récupérer une clef d'autorisation pour les autres microservices, il expose pour ceci deux endpoints :  
* GET ```/ws/is_ws_enabled``` retourne False et active l'API si elle est inactive, et True si l'API est activée.
* GET ```/ws/get_api_key/<service>``` enregistre une clef dans la db Prestashop avec le nom ```<service>``` renseigné et la retourne

## Installation
Le docker-compose.yml intègre ce service, il faut toutefois avoir un fichier .env qui contient les variables suivantes :  
<table>
	<tr><td>PRESTASHOP_DB_USER</td><td>identique à DB_USER et MYSQL_USER</td></tr>
	<tr><td>PRESTASHOP_DB_PASSWD</td><td>identique à DB_PASSWD et MYSQL_PASSWORD</td></tr>
	<tr><td>PRESTASHOP_DB_HOST</td><td>nom du conteneur mariadb</td></tr>
	<tr><td>PRESTASHOP_DB_PORT</td><td>port exposé du conteneur mariadb (par défaut 3306, attention même si on bind un autre port c'est bien le port exposé qui est atteignable)</td></tr>
</table>

A noter, le docker-compose.yml des branches **dev** et **Gestion_API** utilise les variables ```DB_PRESTA, PRESTA_VAR, PRESTA_KEY_MNG``` pour l'intégration via Jenkins, celles-ci font référence à des identifiants stockés dans Jenkins, pour une utilisation autonome il faut les remplacer par le path vers les fichiers d'environnement décrits dans ce README.