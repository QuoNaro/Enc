from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.auth.routes import router as auth_routes
from apps.pm.routes import router as pm_routes
from contextlib import asynccontextmanager
from settings import AppSettings
from db import Base,engine
import os

class FolderError(Exception):
    """
    Custom exception class for folder-related errors.
    """
    pass

def init_vault(folder_path : str = AppSettings().vault_folder_path ) -> None:
    """
    Creates a folder at the specified path.

    Parameters:
        folder_path (str): The full path where the folder should be created.

    Returns:
        bool: True if the folder was successfully created.

    Raises:
        FolderError: If the folder already exists or another error occurs during folder creation.
    """
    try:
        # Check if the folder already exists at the specified path
        if not os.path.exists(folder_path):
            # Create the folder
            os.makedirs(folder_path)
            return True  # Indicate success
        else:
            # Raise an error if the folder already exists
            raise FolderError(f"Folder already exists at: {folder_path}")
    except FolderError as fe:
        # Re-raise folder-specific errors
        raise fe
    except Exception as e:
        # Re-raise other unexpected errors
        raise Exception(f"An error occurred while creating the folder: {e}")



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    try :
        init_vault()
    except FolderError:
        pass
    
    # Таблицы созданы
    yield
    
    
app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


# Подключение маршрутов
app.include_router(auth_routes)
app.include_router(pm_routes)








        
