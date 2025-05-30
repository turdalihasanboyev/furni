# Furni 🛋️

Furni is a Django-based web application for managing and showcasing furniture products. It provides a foundation for building an e-commerce platform with features like product listings, categories, image management, and admin controls.

## 🚀 Features

- Product catalog with images, descriptions, and pricing
- Admin panel for managing products and categories
- Custom apps organized under a modular architecture
- Static files and templates for frontend customization
- Environment configuration using `.env` file
- Django ORM and admin customization

## 🧱 Tech Stack

- Python 3.12.3 +
- Django 5.2
- PostgreSQL (or SQLite by default)
- HTML/CSS (Bootstrap or custom styles)
- Docker (optional)

## 📁 Project Structure

```
furni/
├── apps/                # Django apps like products, users, core
├── config/              # Project settings and URLs
├── templates/           # HTML templates
├── static/              # CSS, JS, and images
├── manage.py
├── .env.example         # Environment variable template
├── requirements.txt     # Project dependencies
```

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/turdalihasanboyev/furni.git
cd furni
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create and configure `.env` file:**

Copy the `.env.example` and update with your own settings.

```bash
cp .env.example .env
```

5. **Run migrations and start the development server:**

```bash
python manage.py migrate
python manage.py runserver
```

## 🧪 Testing

To run tests (if implemented):

```bash
python manage.py test
```

## 🛠️ TODO

- Add user authentication and registration
- Implement shopping cart and checkout system
- Add product search and filters
- Write unit and integration tests
- Improve UI with modern frontend framework

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Made with ❤️ by [Turdali Hasanboyev](https://github.com/turdalihasanboyev)
