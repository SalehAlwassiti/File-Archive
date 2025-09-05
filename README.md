# Archiving System
## Overview
The system is a Python-based digital archiving solution developed for the Department of Engineering to transition from paper-based documentation to a fully digital environment. It provides a structured method for storing, retrieving, and managing departmental records, helping to reduce paper usage while improving accessibility and organization. The application is built with a graphical user interface to make file management tasks intuitive for users, and it integrates networking and database support to enable secure and scalable archiving operations.

## Technologies & Libraries
The system is implemented in Python and makes use of the following libraries and modules:

- **CustomTkinter**: for building a modern graphical user interface  
- **SQLite3**: for managing file records and metadata in a lightweight database  
- **Pillow (PIL)**: for handling and displaying image files within the application  
- **Sockets & Threading**: for enabling network communication and multi-user support  
- **Hashlib**: for file integrity verification using cryptographic hashing  
- **OS, Shutil, Datetime**: for file system operations and timestamp handling  
- **Custom File Manager (Thingy module)**: for organizing and managing archive files
