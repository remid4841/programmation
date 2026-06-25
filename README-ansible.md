# TP — CI/CD avec Ansible

> **YNOV M2 — Promo 25/26**
> Par **Fadi AZZOUZ**

---

## Étape 2 — Pipeline Ansible (`.github/workflows/ansible.yml`)

Le fichier `ansible.yml` est partiellement complété. Votre mission est de remplir les blocs marqués `TODO`.

Le pipeline Ansible utilise un conteneur Docker comme **managed node** (la machine cible d'Ansible). Le runner GitHub Actions joue le rôle du **control node**.

---

### Tâches à implémenter

#### 1. Générer une paire de clés SSH

Le runner doit pouvoir se connecter au conteneur via SSH sans mot de passe. Générez une paire de clés RSA-4096 et copiez la clé publique dans `ansible/authorized_keys` pour qu'elle soit intégrée à l'image Docker.

> **Indice :** cherchez la commande `ssh-keygen` et ses options (`-t`, `-b`, `-f`, `-N`).

---

#### 2. Construire l'image Docker du managed node

Construisez l'image Docker à partir du répertoire `./ansible`.

```yaml
# - name: Build managed node image
#   run: .....
```

---

#### 3. Démarrer le conteneur managed node

Démarrez le conteneur en arrière-plan, en exposant le port SSH `2222` sur l'hôte.

```yaml
# - name: Start managed node container
#   run: |
#     docker run .....
```

---

#### 4. Ansible Lint

Ajoutez un step qui lance `ansible-lint` sur le playbook `deploy.yml` et écrit le résultat dans un fichier de rapport.

```yaml
# - name: Ansible Lint
#   id: lint
#   run: ansible-lint .....
#   working-directory: ./ansible
#   continue-on-error: true
```

---

#### 5. Checkov — Scan de sécurité Ansible

Ajoutez un scan Checkov pour Ansible. Utilisez **la même logique** que pour le scan Terraform dans l'étape 1 (même action `bridgecrewio/checkov-action@v12`, même structure) en adaptant le répertoire et le framework (`ansible`).

---

#### 6. Exécuter le playbook Ansible

Ajoutez un step qui lance `ansible-playbook` contre le managed node via l'inventaire `hosts_docker`.

```yaml
# - name: Run Ansible Playbook
#   run: |
#     ansible-playbook deploy.yml \
#       -i hosts_docker \
#       .....
#   working-directory: ./ansible
```

> **Indice :** vous devrez passer la clé privée SSH en paramètre.

---

#### 7. Vérifier que Nginx répond via HTTP

Après l'exécution du playbook, ajoutez un step qui vérifie que Nginx sert bien du trafic HTTP depuis le runner, pas seulement que le processus tourne.

```yaml
# - name: Verify Nginx serves HTTP traffic
#   run: curl .....
```

> **Indice :** `curl` peut retourner un code d'erreur si le serveur ne répond pas correctement. Regardez les options pour n'afficher que le code HTTP.

---

#### Bonus — Rapport final

Ajoutez un step `Publish Report` qui écrit les résultats d'`ansible-lint` et de Checkov dans `$GITHUB_STEP_SUMMARY`.

---

## Structure du dépôt

```
.
├── .github/
│   └── workflows/
│       └── ansible.yml     # Pipeline Étape 2
├── ansible/
│   ├── deploy.yml          # Playbook Ansible
│   ├── hosts_docker        # Inventaire (managed node Docker)
│   ├── Dockerfile          # Image du managed node
│   └── ...
└── ...
```
