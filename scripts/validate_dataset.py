import os
import glob
from pathlib import Path

def validate_dataset():
    data_dir = Path('data')
    
    print("=== Validación del Dataset ===")
    
    # Contar archivos por subdirectorio
    for subdir in ['raw', 'processed', 'annotations']:
        path = data_dir / subdir
        if not path.exists():
            print(f"Error: El directorio {path} no existe.")
            continue
            
        files = list(path.glob('**/*'))
        files = [f for f in files if f.is_file() and not f.name.endswith('README.md')]
        
        print(f"Directorio '{subdir}':")
        print(f"  - Archivos encontrados: {len(files)}")
        
        if files:
            extensions = set([f.suffix.lower() for f in files])
            print(f"  - Extensiones: {', '.join(extensions)}")
            
    print("===============================")

if __name__ == '__main__':
    validate_dataset()
