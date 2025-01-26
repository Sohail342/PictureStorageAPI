# Picture Storage API

A Django REST Framework (DRF) project for storing and managing pictures using Cloudinary as the cloud-based image storage platform. This API allows authenticated users to upload, retrieve, update, and delete pictures. These API Endpoints are consume by [PictureStorageUI](https://github.com/Sohail342/PictureStorageUI)

## [Cloudinary](https://cloudinary.com/home)
Cloudinary is a cloud-based image and video management platform that provides developers with powerful tools to upload, store, manage, manipulate, and deliver media assets efficiently. It simplifies the process of handling media files by offering a wide range of features, including:

- **Image and Video Upload:** Easily upload media files to the cloud.

- **Optimization:** Automatically optimize images and videos for faster delivery and reduced bandwidth usage.

- **Transformations:** Apply on-the-fly transformations such as resizing, cropping, filters, and more.

- **Storage:** Securely store media files in the cloud with high availability and scalability.

- **CDN Integration:** Deliver media files through a global content delivery network (CDN) for fast loading times.

- **API Support:** Integrate with applications using RESTful APIs and SDKs for various programming languages.

## Features

- **Image Upload**: Upload pictures to Cloudinary.
- **Authentication**: JWT-based authentication for secure access.
- **CORS Support**: Configured to allow requests from specific origins.
- **Docker Support**: Easy setup and deployment using Docker.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **Cloudinary**: A cloud-based image and video management platform.
- **PostgreSQL**: A powerful, open-source relational database system.
- **SQLite**: A lightweight, file-based database for development.
- **JWT Authentication**: Secure token-based authentication.
- **Docker**: Containerization for easy deployment and development.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- PostgreSQL (optional, for production)
- Cloudinary account (for image storage)
- Docker (optional, for Docker setup)

## Setup Instructions

### Option 1: Local Setup

**1. Clone the Repository**

   ```bash
   git clone https://github.com/your-username/picture-storage-api.git
   cd PictureStorageAPI

```

**2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Set Up Environment Variables**

```bash
SECRET_KEY=your-django-secret-key
NAME=your-database-name
USER=your-database-user
PASSWORD=your-database-password
HOST=your-database-host
cloud_name=your-cloudinary-cloud-name
api_key=your-cloudinary-api-key
api_secret=your-cloudinary-api-secret
```

**5. Run Migrations**

```bash
python manage.py migrate
```

**6. Start the Development Server**
```bash
python manage.py runserver
```

### Option 2: Docker Setup

**1. Clone the Repository**

   ```bash
   git clone https://github.com/your-username/picture-storage-api.git
   cd PictureStorageAPI

```

**2. Set Up Environment Variables**

```bash
SECRET_KEY=your-django-secret-key
NAME=your-database-name
USER=your-database-user
PASSWORD=your-database-password
HOST=your-database-host
cloud_name=your-cloudinary-cloud-name
api_key=your-cloudinary-api-key
api_secret=your-cloudinary-api-secret
```
**3. Build Docker Container**

```bash
docker build -t picture-storage-api .
```
**4. Run Docker Container**

```bash
docker run -d -p 8000:8000 --name picture-storage-api picture-storage-api
```
**5. Run Migrations (Inside the Docker Container)**

```bash
docker exec -it picture-storage-api python manage.py migrate
```




## Contact
If you have any questions or feedback, feel free to reach out:
<p align="left">
<a href="https://wa.me/+923431285354" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>


