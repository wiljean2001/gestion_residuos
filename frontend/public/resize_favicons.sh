#!/bin/bash

# Ruta a la imagen original
original="/home/wiljean/Documentos/django-projects/gestion_residuos/frontend/public/favicon.png"

# Dimensiones deseadas
sizes=(60 70 72 76 96 114 120 128 144 150 152 180 310 384)

# Bucle para crear cada versión redimensionada
for size in "${sizes[@]}"; do
    convert "$original" -resize "${size}x${size}" "favicon-${size}x${size}.png"
done

