FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy application files
COPY src/ ./src/
COPY config/ ./config/

# Expose port
EXPOSE 8080

# Set environment variables
ENV NODE_ENV=production
ENV SUPREME_MODE=active
ENV FRACTAL_REALITY=enabled

# Start the orchestrator
CMD ["node", "src/orchestrator/index.js"]
