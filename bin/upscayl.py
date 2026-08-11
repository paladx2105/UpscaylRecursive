import os
import subprocess
from pathlib import Path
from typing import Literal

def run_upscayl_batch(
    input_path: str,
    output_path: str,
    binary_path: str,
    model_name: str,
    model_path: str = "",
    model_scale: Literal[1, 2, 3, 4] = 4,
    custom_scale: str = "",
    compress: int = 0,
    gpu_id: str = "auto",
    tta: bool = False,
    output_format: Literal["jpg", "png", "webp"] = "png",
    verbose: bool = False
):
    """
    Durchläuft ein Verzeichnis rekursiv, spiegelt die Ordnerstruktur und
    verarbeitet alle Bilder mit upscayl-bin.exe.
    """
    input_dir = Path(input_path).resolve()
    output_dir = Path(output_path).resolve()
    bin_file = Path(binary_path).resolve()

    if not bin_file.exists():
        raise FileNotFoundError(f"Die Datei 'upscayl-bin.exe' wurde nicht gefunden unter: {bin_file}")

    # Unterstützte Bildformat-Endungen
    valid_extensions = {".jpg", ".jpeg", ".png", ".webp"}

    # Alle Dateien rekursiv durchsuchen
    files = [f for f in input_dir.rglob("*") if f.is_file() and f.suffix.lower() in valid_extensions]
    print(f"Gefundene Bilder: {len(files)}")

    for file_path in files:
        # Relativen Pfad ermitteln und Zielordner/Datei definieren
        relative_path = file_path.relative_to(input_dir)
        target_file = output_dir / relative_path.with_suffix(f".{output_format}")
        
        # Zielordner erstellen, falls nicht vorhanden
        target_file.parent.mkdir(parents=True, exist_ok=True)

        # CLI-Parameter aufbauen
        cmd = [
            str(bin_file),
            "-i", str(file_path),
            "-o", str(target_file),
            "-n", model_name,
            "-f", output_format,
            "-c", str(compress),
            "-g", gpu_id
        ]

        if model_path:
            cmd.extend(["-m", model_path])

        # Skalierung festlegen
        if custom_scale:
            cmd.extend(["-s", custom_scale])
        else:
            cmd.extend(["-s", str(model_scale)])

        # TTA Flag
        if tta:
            cmd.append("-x")

        # Ausführung
        if verbose:
            print(f"Verarbeite: {file_path.name} -> {target_file}")
            print("Befehl:", " ".join(cmd))
        else:
            print(f"Verarbeite: {file_path.name}...")

        try:
            # Aufruf der exe über subprocess
            result = subprocess.run(
                cmd, 
                check=True, 
                stdout=subprocess.PIPE if not verbose else None,
                stderr=subprocess.PIPE if not verbose else None
            )
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Verarbeiten von {file_path.name}: {e}")

    print("\nFertig! Alle Bilder wurden verarbeitet.")


# --- BEISPIEL FÜR DEN AUFRUF IM PYTHON-SKRIPT ---
if __name__ == "__main__":
    run_upscayl_batch(
        input_path=r"C:\Bilder\Input",
        output_path=r"C:\Bilder\Output",
        binary_path=r"C:\Pfad\zu\upscayl-bin.exe",
        model_name="ultrasharp",
        model_path=r"C:\Pfad\zu\models",
        model_scale=4,
        compress=0,
        gpu_id="auto",
        tta=False,
        output_format="png",
        verbose=True
    )