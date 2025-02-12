# Currency Converter Web App

This is a simple web-based currency converter application built with Flask, a lightweight web framework for Python. The application allows users to convert an amount from one currency to another using real-time exchange rates fetched from the ExchangeRate-API.

Access the application through: http://13.236.94.102
Note this application is accessed using http so there will be "not secure" warning.

## Features

- Convert amounts between different currencies.
- Real-time exchange rates using the ExchangeRate-API.
- Responsive and user-friendly interface.
- Styled with modern CSS, animations, and gradients.

## Project Structure

```
Currency Converter/
├── converter.py       # Main Flask application
├── templates/
│   └── index.html     # HTML template
└── static/
    └── style.css      # CSS file for styling
```

## Usage

1. Select the base currency from the dropdown menu.
2. Select the target currency from the dropdown menu.
3. Enter the amount you want to convert.
4. Click the "Convert" button to get the converted amount.

## Deployment

This application is hosted on an **AWS EC2 instance** using **Gunicorn** as the WSGI server and **Nginx** as a reverse proxy to serve the application efficiently.

### Steps to Deploy:

1. **Set Up EC2 Instance:**

   - Launch an Ubuntu EC2 instance on AWS.
   - Connect to the instance via SSH.

2. **Install Required Software:**

   - Install Python, pip, and virtualenv.
   - Install Gunicorn and Nginx.

3. **Clone the Project:**

   ```bash
   git clone <repository-url>
   cd Currency-Converter
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the App with Gunicorn:**

   ```bash
   gunicorn --bind 127.0.0.1:5000 converter:app
   ```

5. **Configure Nginx:**

   - Set up a server block to proxy requests to Gunicorn.
   - Restart Nginx to apply the configuration.

6. **Set Up Supervisor (Optional but Recommended):**

   - Install Supervisor to ensure the app runs continuously even after reboots.
   - Configure Supervisor to manage the Gunicorn process.

7. **Access the App:**
   - Visit `http://<your-ec2-public-ip>` in your browser to use the application.

This setup ensures the application is **reliable**, **scalable**, and **available 24/7** as long as the EC2 instance is running.
