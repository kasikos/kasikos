# KasiKos

### Requirements
- Python 3.6+
- Pip3
- Virtual Environment (Recommend: ```virtualenvwrapper```)
- Node
- Docker
- Docker-compose

## Installation
### 1. Clone the project
```
git clone https://github.com/zwelisha/kasikos.git
```

### 2. Create and Activate Virtual Environment
```
mkvirtualenv kasikos-dev

workon kasikos-dev
```

### 3. Install all required modules
First make sure you ```cd``` into ```kasikos``` directory, then run the following command:
```
pip3 install -r requirements.txt
```

### 4. Install all JavaScript modules
```
npm i
```

## Testing your installation

### First compile React
- For development
```
npm run dev
```

- For production
```
npm run build
```

### Migrate tables
Run the following command if it is the first time you clone this project:
```
python3 manage.py migrate
```

### Then run django local server
```
python3 manage.py runserver
```

### Making migrations
If ever for some reason you need to recreate migration run:
```
python3 manage.py makemigrations
```