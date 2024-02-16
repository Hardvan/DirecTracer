import DirecTracer
import os

if __name__ == "__main__":

    DirecTracer.save_directory_structure(
        root_dir=os.getcwd(),
        text_output_file="run_output.txt",
        markdown_output_file="run_output.md",
        animation=True
    )
