# YNOV TP 2 — Ansible Deployment

Déploiement automatisé d'une application Angular (Olympic Games) avec Nginx via Ansible.

---

## Prérequis

- [Docker](https://www.docker.com/) et Docker Compose installés
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/) installé sur votre machine locale
- `sshpass` installé (`brew install hudochenkov/sshpass/sshpass` sur macOS)

---

## Démarrage de la machine cible

Le fichier `docker-compose.yml` lance un conteneur Ubuntu accessible en SSH sur le port **2222**.  
C'est cette machine qui recevra le déploiement via Ansible.

```bash
docker compose up -d --build
```

Vérifier que le conteneur tourne :

```bash
docker compose ps
```

---

## Inventaire Ansible

Le fichier `hosts_docker` pointe déjà vers le conteneur :

```ini
[all]
127.0.0.1 ansible_ssh_user=ynov ansible_ssh_port=2222
```

Mot de passe SSH du user `ynov` : **ynov**

---

## Ce qu'il faut implémenter dans `deploy.yml`

Le playbook `deploy.yml` contient une structure vide avec des commentaires.  
Voici la liste des tâches à compléter **dans l'ordre** :

### Tasks

1. **Installer Nginx** — via le module `apt` (mettre à jour le cache)
2. **Créer le répertoire de l'application** — `/var/www/html/olympic-games-starter` avec les bons droits
3. **Copier les fichiers Angular** — depuis `app/olympic-games-starter/` vers le répertoire créé
4. **Copier la configuration Nginx** — depuis `nginx/app.conf` vers `/etc/nginx/sites-available/app.conf`
5. **Activer le site Nginx** — créer un lien symbolique dans `sites-enabled/`
6. **Désactiver le site Nginx par défaut** — supprimer le lien `sites-enabled/default`
7. **Démarrer et activer Nginx** — s'assurer que le service est lancé et activé au démarrage

### Handler

8. **Redémarrer Nginx** — handler déclenché automatiquement par les tâches de configuration (notify)

---

## Lancer le playbook

```bash
ansible-playbook -i hosts_docker deploy.yml --ask-pass --ask-become-pass
```

> Les deux mots de passe demandés sont `ynov`.

---

## Vérification

Une fois le playbook exécuté, l'application est accessible sur :

```
http://localhost:80
```

---

## Arrêter le conteneur

```bash
docker compose down
```
