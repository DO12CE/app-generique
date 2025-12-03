
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);


INSERT INTO items (name, description) VALUES
    ('Tâche 1: Conteneuriser API', 'Créer le Dockerfile multiétapes pour l API'),
    ('Tâche 2: Conteneuriser Front', 'Créer le Dockerfile multiétapes pour le Front')
ON CONFLICT (id) DO NOTHING;