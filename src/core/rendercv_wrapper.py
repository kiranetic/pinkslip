# src/core/rendercv_wrapper.py
import subprocess
import tempfile
import os

def render_pdf_from_yaml(yaml_resume: str, output_path: str):
    subprocess.run(["rendercv", "render", "--dont-generate-markdown", "--dont-generate-html", "--dont-generate-png", yaml_resume, "--pdf-path", output_path], check=True)
    print(f"Resume rendered to {output_path}")
