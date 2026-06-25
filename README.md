# TP — CI/CD avec Terraform

> **YNOV M2 — Promo 25/26**
> Par **Fadi AZZOUZ**

---

## Pré-requis

Avant de commencer, effectuez les actions suivantes.

### 1. Créer un dépôt GitHub et pousser ce projet

1. Connectez-vous à [github.com](https://github.com) et créez un **nouveau dépôt public ou privé** (ex. `cicd-tp`).
2. Clonez ce projet localement, puis liez-le à votre dépôt distant et poussez-le :

```bash
git init
git remote add origin https://github.com/<votre-utilisateur>/cicd-tp.git
git add .
git commit -m "initial commit"
git push -u origin main
```

### 2. Créer un compte Infracost et obtenir une clé API

1. Rendez-vous sur [infracost.io](https://www.infracost.io) et créez un compte.
2. Une fois connecté, allez dans **Org Settings** (paramètres de l'organisation).
3. Dans la section **API keys**, générez une clé pour la CLI et copiez-la.

### 3. Ajouter la clé Infracost comme secret GitHub

1. Dans votre dépôt GitHub, allez dans **Settings → Secrets and variables → Actions**.
2. Cliquez sur **New repository secret**.
3. Nommez-le `INFRACOST_API_KEY` et collez la clé copiée à l'étape précédente.

---

## Pipeline Terraform (`.github/workflows/terraform.yml`)

Le fichier `terraform.yml` est partiellement complété. Votre mission est de remplir les blocs marqués `TODO`.

### Tâches à implémenter

#### 1. Terraform Format

Ajoutez un step qui vérifie que les fichiers `.tf` sont correctement formatés.

```yaml
# - name: Terraform Format
#   id: fmt
#   run: terraform fmt .....
#   working-directory: ./terraform
```

> **Indice :** la commande `terraform fmt` accepte un flag pour simplement vérifier le format sans modifier les fichiers.

---

#### 2. Terraform Init

Ajoutez un step qui initialise le répertoire de travail Terraform (télécharge les providers, etc.).

```yaml
# - name: Terraform Init
#   id: init
#   run: terraform init .....
#   working-directory: ./terraform
```

---

#### 3. Terraform Plan

Ajoutez un step qui génère un plan d'exécution Terraform, ainsi qu'un step conditionnel qui fait échouer le job si le plan échoue.

```yaml
# - name: Terraform Plan
#   id: plan
#   run: terraform plan .....
#   working-directory: ./terraform
#   continue-on-error: true
#
# - name: Terraform Plan Status
#   if: steps.plan.outcome == 'failure'
#   run: exit 1
```

---

#### 4. Infracost — Estimation des coûts cloud

Ajoutez le step d'installation du CLI Infracost via l'action officielle. Le step `infracost breakdown` est déjà fourni et s'exécutera une fois l'installation réalisée.

> **Indice :** utilisez l'action `infracost/actions/setup@v3` et passez votre clé avec `api-key: ${{ secrets.INFRACOST_API_KEY }}`.

---

#### 5. Terraform Apply

Ajoutez un step qui déploie l'infrastructure.

```yaml
# - name: Terraform Apply
#   run: terraform apply .....
#   working-directory: ./terraform
```

> **Indice :** regardez le flag qui permet d'éviter la confirmation interactive.

---

#### Bonus — Rapport

Une fois Infracost configuré, publiez le tableau de coûts dans le résumé du job GitHub Actions via `$GITHUB_STEP_SUMMARY`.

---

## Structure du dépôt

```
.
├── .github/
│   └── workflows/
│       └── terraform.yml   # Pipeline CI/CD
├── terraform/
│   ├── main.tf
│   ├── dev.tfvars
│   └── ...
└── python/
    └── ...
```
