# Tells the image to use the latest version of PHP
FROM nginx:1.26-alpine  

# Copies your code to the image
COPY /www/ /usr/share/nginx/html

# Sets that directory as your working directory
WORKDIR /usr/share/nginx/html 