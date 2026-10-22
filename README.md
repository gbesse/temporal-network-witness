# temporal-network-witness

## Français

Trouver et rejouer un cycle de contraintes temporelles impossible.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m temporal_network_witness examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Réseau temporel simple par Bellman-Ford. Chaque contrainte signifie t[to] − t[from] ≤ max. Une impossibilité contient un cycle orienté dont la somme négative se vérifie indépendamment ; une possibilité contient un horaire complet. Contrairement à mission-intent-repair, aucun choix de tâches ni optimisation de ressources.

### Limites

Temps entiers dans une unité unique déclarée par l’appelant ; 100 nœuds et 1 000 contraintes maximum. Algorithme classique, sans supériorité SOTA ni validation de vol.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find and replay an impossible temporal-constraint cycle.

Synthetic data; no network access or secret required.

```sh
python -m temporal_network_witness examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Bellman-Ford simple temporal network. Each constraint means t[to] − t[from] ≤ max. Infeasibility contains a directed cycle with independently checkable negative sum; feasibility contains a full schedule. Unlike mission-intent-repair, this does not select tasks or optimize resources.

### Limits

Integer times in one caller-declared unit; at most 100 nodes and 1,000 constraints. Classical algorithm, no SOTA superiority or flight validation.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar y reproducir un ciclo imposible de restricciones temporales.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m temporal_network_witness examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Red temporal simple con Bellman-Ford. Cada restricción significa t[to] − t[from] ≤ max. La imposibilidad incluye un ciclo dirigido con suma negativa verificable; la viabilidad incluye un horario completo. A diferencia de mission-intent-repair, no selecciona tareas ni optimiza recursos.

### Límites

Tiempos enteros en una unidad declarada; máximo 100 nodos y 1.000 restricciones. Algoritmo clásico, sin superioridad SOTA ni validación de vuelo.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/plexil-group/plexil
- https://doi.org/10.1016/0004-3702(91)90006-6
