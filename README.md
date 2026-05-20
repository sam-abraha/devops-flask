<h1>DevOps</h1>

<p>
A beginner-friendly DevOps project that demonstrates a full CI/CD pipeline using Flask, Docker, and GitHub Actions.
The application automatically runs tests, builds a Docker image, and can be deployed to a server.
</p>

<h2>Overview</h2>

<p>
This project is a simple REST API built with Flask. It is not focused on business logic, but on demonstrating real-world DevOps workflows such as automation, containerization, and continuous integration.
</p>

<h2>Application Features</h2>

<ul>
    <li><strong>Health Check API:</strong> Check if the service is running.</li>
    <li><strong>Simple REST API:</strong> Lightweight Flask endpoints.</li>
    <li><strong>Automated Tests:</strong> Pytest integration for CI validation.</li>
    <li><strong>Docker Support:</strong> Runs consistently in any environment.</li>
    <li><strong>CI Pipeline:</strong> Automated testing with GitHub Actions.</li>
    <li><strong>CD Ready:</strong> Can be extended to automatic deployment.</li>
</ul>

<h2>API Endpoints</h2>

<ul>
    <li><strong>GET /</strong> → Returns a status message</li>
    <li><strong>GET /health</strong> → Returns service health status</li>
</ul>

<h2>Technical Stack</h2>

<h3>Backend</h3>

<ul>
    <li><strong>Language:</strong> Python 3.11</li>
    <li><strong>Framework:</strong> Flask</li>
</ul>

<h3>Testing</h3>

<ul>
    <li><strong>Framework:</strong> Pytest</li>
</ul>

<h3>DevOps / Infrastructure</h3>

<ul>
    <li><strong>Containerization:</strong> Docker</li>
    <li><strong>CI/CD:</strong> GitHub Actions</li>
    <li><strong>Version Control:</strong> Git & GitHub</li>
</ul>

<h2>CI/CD Pipeline</h2>

<p>
Every push to the <strong>main branch</strong> triggers an automated pipeline:
</p>

<ul>
    <li>Install dependencies</li>
    <li>Run automated tests</li>
    <li>Validate application integrity</li>
</ul>

<h2>Project Structure</h2>

<pre>
devops-flask/
│
├── app/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── requirements.txt
├── Dockerfile
└── .github/workflows/ci.yml
</pre>

<h2>How to Run Locally</h2>

<pre>
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run application
python app/app.py
</pre>

<h2>Run with Docker</h2>

<pre>
# Build image
docker build -t devops-app .

# Run container
docker run -p 5000:5000 devops-app
</pre>

<h2>Future Improvements</h2>

<ul>
    <li>Docker image push to Docker Hub</li>
    <li>Automatic deployment to VPS</li>
    <li>Monitoring with Prometheus & Grafana</li>
    <li>HTTPS reverse proxy (Nginx)</li>
</ul>

<h2>Goal of this Project</h2>

<p>
The goal is to understand real-world DevOps workflows:
from writing code → testing → building → deploying automatically.
</p>