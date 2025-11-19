# CWE-22 — Path Traversal (Improper Limitation of a Pathname to a Restricted Directory)

Cette vulnérabilité survient lorsqu'une application construit des chemins de fichiers à partir d'entrées utilisateur **sans valider ni normaliser le chemin**, ce qui permet d'accéder à des fichiers en dehors du répertoire prévu.

**Référence MITRE :** [CWE-22](https://cwe.mitre.org/data/definitions/22.html)
