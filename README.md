# README

## Description
Ce projet contient deux scripts Python permettant d'automatiser la navigation sur un site web avec Selenium et d'extraire des liens depuis une page avec BeautifulSoup.

### Fonctionnalités
1. **selenium()** : Automatisation de l'ajout d'un produit au panier sur Zooplus.
2. **scrap_to_page()** : Scraping des titres des pages liées à la documentation MDN.

---

## Prérequis
Avant d'exécuter ce projet, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- Google Chrome
- [Chromedriver](https://sites.google.com/chromium.org/driver/)
- Selenium
- BeautifulSoup
- Requests
- lxml

Installez les dépendances Python avec la commande :
```bash
pip install -r requirements.txt
```

---

## Utilisation

### Exécuter l'automatisation Selenium
La fonction `selenium()` ouvre Google Chrome et effectue les actions suivantes sur **Zooplus** :
- Accepte les cookies.
- Effectue une recherche de "paté pour chat".
- Applique un filtre pour les produits destinés aux chats.
- Trie les résultats par prix décroissant.
- Ajoute deux unités du premier produit au panier.
- Accède à la page du panier.

Exécutez cette fonction en lançant le script Python :
```python
selenium()
```

**⚠️ Attention :** Assurez-vous de modifier le chemin de `chromedriver.exe` dans le code avant d'exécuter le script.

### Exécuter le scraping de pages MDN
La fonction `scrap_to_page()` récupère et affiche les titres des pages liées à **developer.mozilla.org/fr/**.

Exécutez cette fonction en lançant :
```python
scrap_to_page()
```

---

## Notes
- Ce script fonctionne uniquement avec Google Chrome.
- Vérifiez que **Chromedriver** est compatible avec votre version de Chrome.
- L'usage de `time.sleep()` est utilisé pour gérer les délais de chargement des pages, mais une approche plus robuste serait d'utiliser `WebDriverWait` de Selenium.

---

## Auteur
Développé par Bougherara Safi

