FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies
RUN npm install

# Copy application source
COPY . .

# Build the application
RUN npm run build

# Expose port and run
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
