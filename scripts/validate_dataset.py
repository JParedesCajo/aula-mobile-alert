from pathlib import Path

DATASET_DIR = Path("data/dataset")

image_extensions = {".jpg", ".jpeg", ".png"}

def validate_dataset():
    if not DATASET_DIR.exists():
        print(f"Error: La carpeta {DATASET_DIR} no existe.")
        return

    for split in ["train", "val", "test"]:
        image_dir = DATASET_DIR / "images" / split
        label_dir = DATASET_DIR / "labels" / split

        if not image_dir.exists():
            print(f"Error: La carpeta {image_dir} no existe.")
            continue
            
        if not label_dir.exists():
            print(f"Error: La carpeta {label_dir} no existe.")
            continue

        all_image_files = [
            f for f in image_dir.iterdir()
            if f.is_file() and f.name != "README.md"
        ]
        
        images = [f for f in all_image_files if f.suffix.lower() in image_extensions]
        invalid_images = [f for f in all_image_files if f.suffix.lower() not in image_extensions]
        
        labels = list(label_dir.glob("*.txt"))

        print(f"\n[{split}]")
        print(f"Imágenes: {len(images)}")
        print(f"Etiquetas: {len(labels)}")
        
        if invalid_images:
            print(f"  - Advertencia: {len(invalid_images)} archivos con extensión inválida.")
        
        image_stems = {img.stem for img in images}
        label_stems = {lbl.stem for lbl in labels}
        
        images_without_label = image_stems - label_stems
        if images_without_label:
            print(f"  - Advertencia: {len(images_without_label)} imágenes sin etiqueta.")
            
        labels_without_image = label_stems - image_stems
        if labels_without_image:
            print(f"  - Advertencia: {len(labels_without_image)} etiquetas sin imagen correspondiente.")
            
        empty_labels = 0
        invalid_classes = 0
        invalid_coords = 0
        
        for label_path in labels:
            if label_path.stat().st_size == 0:
                empty_labels += 1
                continue
                
            with open(label_path, 'r') as f:
                lines = f.readlines()
                if not lines:
                    empty_labels += 1
                    continue
                    
                for line in lines:
                    parts = line.strip().split()
                    if not parts:
                        continue
                    if len(parts) != 5:
                        invalid_coords += 1
                        continue
                        
                    cls = parts[0]
                    if cls not in ['0', '1']:
                        invalid_classes += 1
                        
                    try:
                        x, y, w, h = map(float, parts[1:5])
                        if not (0.0 <= x <= 1.0 and 0.0 <= y <= 1.0 and 0.0 <= w <= 1.0 and 0.0 <= h <= 1.0):
                            invalid_coords += 1
                    except ValueError:
                        invalid_coords += 1
                        
        if empty_labels > 0:
            print(f"  - Error: {empty_labels} etiquetas vacías.")
        if invalid_classes > 0:
            print(f"  - Error: {invalid_classes} anotaciones con clases diferentes de 0 y 1.")
        if invalid_coords > 0:
            print(f"  - Error: {invalid_coords} anotaciones con valores fuera de rango o formato incorrecto.")

if __name__ == "__main__":
    validate_dataset()
