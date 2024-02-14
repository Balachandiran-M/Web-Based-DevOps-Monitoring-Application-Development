![Your paragraph text](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/38232550-6193-48a1-a2ba-bad0bdf150cf)

  <h2>Step 1: Application Development</h2>

<p>
Initially, I developed this monitoring application using Python, HTML, and CSS, leveraging the Python Flask framework. The application comprises essential functionalities such as signup, login, portfolio management, and monitoring sections.
</p>

<h2>Step 2: Containerization with Docker</h2>

<p>
Subsequently, I containerized the application using Docker for its lightweight nature and portability, allowing it to run seamlessly across various environments.
</p>

<h2>Step 3: Publishing to Docker Hub</h2>

<p>
Following containerization, I published the application to Docker Hub, making it publicly accessible by storing it in a public repository.
</p>

<h2>Step 4: Deployment on Kubernetes (EKS)</h2>

<p>
Afterward, I proceeded to deploy the application on Kubernetes, specifically utilizing an EKS cluster. Kubernetes serves as a powerful container orchestration tool, offering features like auto-scaling, deployment rollback capabilities, and load balancing, ensuring robustness and scalability.
</p>

<h2>Step 5: Automation with Jenkins</h2>

<p>
To streamline the entire process, I automated each stage using Jenkins, orchestrating the following tasks:
</p>

<ol>
  <li><strong>Stage 1:</strong> Fetching the application code from GitHub and initiating the build process.</li>
  <li><strong>Stage 2:</strong> Containerizing the application using Docker, ensuring encapsulation and ease of deployment.</li>
  <li><strong>Stage 3:</strong> Pushing the Dockerized application to Docker Hub, facilitating accessibility and version control.</li>
  <li><strong>Stage 4:</strong> Finally, deploying the application onto the Kubernetes cluster (EKS) to ensure efficient management and scalability of the application.</li>
</ol>
