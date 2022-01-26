# model-deployment
Model deployment for inference using Flask, gunicorn, nginx and docker.

# Model
Twitter-roBERTa-base for Sentiment Analysis was the model of choice for this deployment execise. Sentiment analysis is an interesting yet challenging NLP task. The model is of reasonable size (about 480 MB) which is not too small to be considered trivial and not too large to demand powerful infrastructure thereby being ideal for a model deployment execise.

# What's included?
**Part2_app** --> This folder contains a Flask inference service written in python that accepts input text from client in port **7050**. Note that port here is hardcoded. Choice of WSGI is gunicorn with 10 workers. Timeout of each worker is disabled (by setting to 0) to avoid timeout during download of model and its dependencies.  

**nginx** --> This folder contains configuration of nginx server.  

**client_code** --> Contains client applications for quering the server. More details included below.  

# How to run?
Build the docker-compose file by running run_docker.sh or " docker-compose up --build -d " command
Once it is built and is up and running, allow for some time for it to download the model and dependencies.

# How to query?
Once the containers are up and running, you can query the model in one of the following ways,
1. python3 client.py <text here>   ||   python3 client.py I love hamburger and fries  
2. python3 multiThreadClient.oy <threadCount> ||   python3 multiThreadClient.py 150  
3. You can also use python notebook to query the server using multiTreadedClient code included in it.  

# Testing...
Testing was carried out in my laptop with the following configuration,
  Core i7 Processor - 16 GB RAM - GTX 960M GPU - Windows 10
