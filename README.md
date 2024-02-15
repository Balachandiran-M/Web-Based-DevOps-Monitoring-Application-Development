![Your paragraph text](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/38232550-6193-48a1-a2ba-bad0bdf150cf)

  <h2>Step 1: Application Development</h2>

<p>
Initially, I developed this monitoring application using Python, HTML, and CSS, leveraging the Python Flask framework. The application comprises essential functionalities such as signup, login, portfolio management, and monitoring sections.
  
![Screenshot (208)](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/05ea5214-9b08-436a-81f9-34922b27e0ac)
  
![Screenshot (212)](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/4e9bedd5-5bb5-4de2-8f35-210a72bfb7f7) 

![Screenshot (209)](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/bbd144af-88e2-4889-995b-839eba111991)

![Screenshot (210)](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/d8045666-0aaf-44e7-9c59-5e1b72a6408e)

  
</p>

<h2>Step 2: Containerization with Docker</h2>

<p>
Subsequently, I containerized the application using Docker for its lightweight nature and portability, allowing it to run seamlessly across various environments.
</p>

<h2>Step 3: Publishing to Docker Hub</h2>

<p>
Following containerization, I published the application to Docker Hub, making it publicly accessible by storing it in a public repository.

![Screenshot 2024-02-15 192822](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/2dd13294-a786-4e5a-8b5d-5b9bd9c28353)

  
</p>

<h2>Step 4: Deployment on Kubernetes (EKS)</h2>

<p>
Afterward, I proceeded to deploy the application on Kubernetes, specifically utilizing an EKS cluster. Kubernetes serves as a powerful container orchestration tool, offering features like auto-scaling, deployment rollback capabilities, and load balancing, ensuring robustness and scalability.

![Screenshot 2024-02-15 193044](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/6c6c6683-afea-42e2-8e5d-4c78c5102cf0)

![Screenshot 2024-02-15 193153](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/575d3007-67a9-419a-a9e4-2e4be3deacde)

  
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

![Screenshot 2024-02-15 193931](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/d06d883d-6579-436f-b484-5e93fc6a4fb2)

![Screenshot 2024-02-15 194121](https://github.com/Balachandiran-M/Web-Based-DevOps-Monitoring-Application-Development/assets/152047725/89c1d3a5-9880-4fd2-bfb6-25b06a4271ed)
