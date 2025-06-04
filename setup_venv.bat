REM Navigate to the project directory
mkdir torquetalk && cd torquetalk

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install the required packages
pip install -r requirements.txt
