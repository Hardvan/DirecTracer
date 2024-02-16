# Directory Structure

Format:

```md
📂 Directory
  - File
```

- 📂 **DirecTracer (Current Directory)**
  - [.gitignore](./.gitignore)
  - [directory_structure.md](./directory_structure.md)
  - [directory_structure.txt](./directory_structure.txt)
  - [LICENSE.txt](./LICENSE.txt)
  - [README.md](./README.md)
  - [requirements.txt](./requirements.txt)
  - [run.py](./run.py)
  - [run_output.md](./run_output.md)
  - [run_output.txt](./run_output.txt)
  - [setup.py](./setup.py)
- 📂 **app**
  - [README.md](app/README.md)
  - [__init__.py](app/__init__.py)
  - 📂 **DirecTracer**
    - [__init__.py](app/DirecTracer/__init__.py)
    - 📂 **src**
      - [DirectTracer.py](app/DirecTracer/src/DirectTracer.py)
      - [__init__.py](app/DirecTracer/src/__init__.py)
    - 📂 **test**
      - [generate_sample_structure.py](app/DirecTracer/test/generate_sample_structure.py)
      - [__init__.py](app/DirecTracer/test/__init__.py)
  - 📂 **DirecTracer.egg-info**
    - [dependency_links.txt](app/DirecTracer.egg-info/dependency_links.txt)
    - [PKG-INFO](app/DirecTracer.egg-info/PKG-INFO)
    - [SOURCES.txt](app/DirecTracer.egg-info/SOURCES.txt)
    - [top_level.txt](app/DirecTracer.egg-info/top_level.txt)
- 📂 **build**
  - 📂 **bdist.win-amd64**
  - 📂 **lib**
    - 📂 **DirecTracer**
      - [__init__.py](build/lib/DirecTracer/__init__.py)
      - 📂 **src**
        - [DirectTracer.py](build/lib/DirecTracer/src/DirectTracer.py)
        - [__init__.py](build/lib/DirecTracer/src/__init__.py)
      - 📂 **test**
        - [generate_sample_structure.py](build/lib/DirecTracer/test/generate_sample_structure.py)
        - [__init__.py](build/lib/DirecTracer/test/__init__.py)
- 📂 **demo**
  - [Demo_Video.mp4](demo/Demo_Video.mp4)
  - [thumbnail.png](demo/thumbnail.png)
  - [thumbnail2.png](demo/thumbnail2.png)
- 📂 **dist**
  - [DirecTracer-1.0.0-py3-none-any.whl](dist/DirecTracer-1.0.0-py3-none-any.whl)
  - [DirecTracer-1.0.0.tar.gz](dist/DirecTracer-1.0.0.tar.gz)
- 📂 **SampleDirectory**
  - 📂 **FolderA**
    - [File1.txt](SampleDirectory/FolderA/File1.txt)
    - [File2.txt](SampleDirectory/FolderA/File2.txt)
    - [File3.txt](SampleDirectory/FolderA/File3.txt)
    - 📂 **Subfolder1**
    - 📂 **Subfolder2**
    - 📂 **Subfolder3**
  - 📂 **FolderB**
    - [File1.txt](SampleDirectory/FolderB/File1.txt)
    - [File2.txt](SampleDirectory/FolderB/File2.txt)
    - [File3.txt](SampleDirectory/FolderB/File3.txt)
    - 📂 **Subfolder1**
    - 📂 **Subfolder2**
    - 📂 **Subfolder3**
  - 📂 **FolderC**
    - [File1.txt](SampleDirectory/FolderC/File1.txt)
    - [File2.txt](SampleDirectory/FolderC/File2.txt)
    - [File3.txt](SampleDirectory/FolderC/File3.txt)
    - 📂 **Subfolder1**
    - 📂 **Subfolder2**
    - 📂 **Subfolder3**
