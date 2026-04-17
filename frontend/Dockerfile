# Image for React 
From node:18 as build

#Working directory
Workdir /app

#ARG: Defining build-time variables
#ENV: Defining build and runtime variables

ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Copy package files
copy package*.json ./
run npm install 

#copy all files
copy . .
run npm run build

from nginx:alpine
copy --from=build /app/build /usr/share/nginx/html

expose 80

cmd ["nginx", "-g", "daemon off;"]

