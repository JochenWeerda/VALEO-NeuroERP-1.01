from setuptools import setup, find_packages

setup(
    name="valeo-neuroerp",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "sqlalchemy>=2.0.23",
        "alembic>=1.12.1",
        "pydantic>=1.10.13",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "python-dotenv>=1.0.0",
        "pytest>=7.4.3",
        "httpx>=0.25.2",
        "psutil>=5.9.6"
    ],
    python_requires=">=3.8",
) 