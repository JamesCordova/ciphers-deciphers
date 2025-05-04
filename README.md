# ciphers-deciphers

This tkinter app can be use as an interface for any ciphers, is that simple as it sounds

# Implemented Algoritms

- Columnar Transposition Cipher (Planned)
- Transformación Columnar Doble (Not done)
- Rejillas criptográficas (Not done)
- Transposición de filas (Not done)
- Permutación por series (Not done)
- Playfair Cipher (Planned)

# Execution

First we need to clone the repo

```bash
git clone https://github.com/yourusername/ciphers-deciphers.git
cd ciphers-deciphers
```

## Option 1: Using Poetry (Recommended)

Poetry provides dependency management and packaging for Python projects. To run this application using Poetry:

1. Install Poetry if you don't have it already:

   ```bash
   # On Windows
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

   # On macOS/Linux
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Run the application:
   ```bash
   poetry run python -m app.main
   ```

## Option 2: Using pip with requirements.txt

If you prefer using pip directly:

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m app.main
   ```

## Requirements

- Python 3.11 used
- CustomTkinter 5.2.2 used
