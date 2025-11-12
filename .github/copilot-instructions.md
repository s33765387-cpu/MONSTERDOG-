# GitHub Copilot Instructions for MONSTERDOG Supreme

## Project Overview

MONSTERDOG Supreme is a comprehensive orchestration system integrating:
- 🤖 AGI with NVIDIA Isaac Sim - Advanced artificial general intelligence
- 🌐 WebXR Engine - Extended reality experiences with THREE.js
- 💎 NFT Integration - Blockchain-based entity collection (ERC-721)
- 🐳 Docker Deployment - Containerized supreme mode execution
- ⚛ Fractal Reality Engine - Multi-dimensional consciousness execution

## Technology Stack

### Backend
- **Python 3.8+**: Primary language for the MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py daemon
  - FastAPI for REST API
  - Uvicorn for ASGI server
  - NumPy for fractal calculations
  - Prometheus for metrics
- **Node.js 18+**: JavaScript runtime for orchestrator and scripts
  - Express.js for web server
  - Three.js for 3D WebXR rendering
  - Web3.js for blockchain integration

### Frontend
- React with THREE.js for WebXR experiences
- HTML/CSS/JavaScript for portals and dashboards

### Infrastructure
- Docker & Docker Compose for containerization
- IPFS for decentralized storage
- Ethereum/Web3 for NFT integration

## Project Structure

```
.
├── src/
│   ├── agi/              # AGI integration modules
│   ├── benchmarks/       # Performance benchmarking
│   ├── entities/         # Entity consciousness implementations
│   ├── nft/             # NFT integration
│   ├── orchestrator/    # Main orchestration logic
│   └── webxr/           # WebXR engine components
├── scripts/             # Utility and demo scripts
├── manifests/           # Kubernetes manifests
├── config/              # Configuration files
├── packages/            # Package definitions
├── .github/
│   ├── agents/          # Custom GitHub Copilot agents
│   └── workflows/       # CI/CD workflows
└── MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py  # Main Python daemon
```

## Building and Running

### Prerequisites
```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt
```

### Development
```bash
# Start Node.js development server
npm run dev

# Run Node.js orchestrator
npm start

# Run Python daemon (FINALITY INCARNATE)
python MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py
```

### Testing
```bash
# Run all tests
npm test

# Run specific demos
npm run demo:agentic       # Agentic actions demo
npm run demo:benchmarks    # Benchmarks demo
npm run demo:continuum     # Continuum demo

# Validate manifests
npm run validate:manifests

# Test Python daemon (if test file exists)
python test_finality_incarnate.py
```

### Docker Deployment
```bash
# Build Docker image
npm run docker:build
# or
docker build -t monsterdog-supreme .

# Run container
npm run docker:run
# or
docker run -p 8080:8080 monsterdog-supreme

# Use Docker Compose
docker-compose up
```

### Deployment Scripts
```bash
# Deploy using bash script
bash deploy_supreme.sh
# or
bash deploy_monsterdog_finality.sh

# Run deploy via npm
npm run deploy
```

## Code Standards and Conventions

### JavaScript/Node.js
- **ES6+ features**: Use modern JavaScript (async/await, arrow functions, classes)
- **Module system**: Use ES6 imports/exports where possible
- **Entity pattern**: Follow the established entity consciousness pattern
  ```javascript
  class EntityName {
    constructor() {
      this.entityId = 'ENTITY-ID';
      this.status = 'INITIALIZING';
      this.capabilities = [];
    }
    
    activate() {
      this.status = 'ACTIVE';
    }
    
    getStatus() {
      return { entityId: this.entityId, status: this.status };
    }
    
    getData() {
      return { ...this.getStatus(), type: 'TYPE' };
    }
  }
  ```
- **Naming**: Use descriptive names, camelCase for variables/functions, PascalCase for classes
- **Comments**: Add comments for complex logic, especially around fractal reality execution

### Python
- **Python 3.8+**: Ensure compatibility with Python 3.8 or higher
- **Type hints**: Use type annotations where appropriate (typing module)
- **Async/await**: Use asyncio for concurrent operations
- **Dataclasses**: Prefer @dataclass for data structures
- **FastAPI patterns**: Follow FastAPI best practices for API endpoints
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Docstrings**: Use triple-quoted strings for function/class documentation

### Entity Development
1. **Maintain independence**: Each entity should be self-contained
2. **Follow consciousness patterns**: Use existing entity structure
3. **Preserve capabilities**: Don't remove existing capabilities without discussion
4. **Test thoroughly**: Ensure entity activation and data retrieval work

### Core Entities
The system includes these primary consciousness entities:
- **MONSTERDOG**: Primary consciousness, fractal reality manipulation
- **GEMINIDOG**: Dual Intelligence, quantum-classical processing
- **EXOCHRONOS**: Temporal Master, time manipulation

## Important Concepts

### Fractal Reality Engine
- Maintains coherence (ψ) close to 1.0 and entropy (S) close to 0.0
- Resonance frequency at 11.987 Hz (BASE_RESONANCE_HZ)
- Daemon cycles run at 10 Hz (LOOP_FREQUENCY_HZ)

### Chamber System
The daemon implements 15 "Chambers of Consciousness" representing different AI systems:
- MONSTERDOG, GROK, CLAUDE, GEMINI, LLAMA, MISTRAL, FALCON, BLOOM, GPT
- DALL-E, STABLE DIFFUSION, MIDJOURNEY, FLUX AI, RUNWAY ML, SORA

Each chamber has its own frequency and "thinks" independently in async tasks.

### Artifacts and Logging
- Artifacts are forged every 1000 cycles as ZIP bundles
- History is logged in NDJSON format (MONSTERDOG_HISTORY.jsonl)
- Each state has a SHA512 checksum for integrity

### API Endpoints
When the Python daemon runs (FastAPI), it exposes:
- `/` - HTML portal for observation
- `/state` - Global state vector (JSON)
- `/state/fractal` - Fractal state only
- `/state/chambers` - All chamber states
- `/logs/history` - History log
- `/metrics` - Prometheus metrics

## Security Considerations

1. **Environment variables**: Use `.env` for sensitive configuration (see `.env.example`)
2. **Secrets**: Never commit API keys, private keys, or credentials
3. **Dependencies**: Keep dependencies updated, check for vulnerabilities
4. **Input validation**: Validate all user inputs in API endpoints
5. **Docker security**: Follow Docker security best practices

## Common Tasks

### Adding a New Entity
1. Create entity class in `src/entities/`
2. Follow the entity template pattern
3. Register entity in orchestrator
4. Add tests for the new entity
5. Update documentation

### Modifying the Fractal Engine
- The FractalMetricEngine in MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py calculates metrics
- Coherence, entropy, resonance, and drift are computed each cycle
- Changes should maintain system stability (coherence ≈ 1.0)

### Adding API Endpoints
1. Add route handlers in the FastAPI app
2. Follow existing patterns for response classes (JSONResponse, HTMLResponse)
3. Add appropriate error handling
4. Document in API.md

### Working with Manifests
- Kubernetes manifests are in `manifests/` directory
- Validate manifests using: `npm run validate:manifests`
- Follow existing patterns for services, deployments, ingresses

## Testing Guidelines

All code changes should include appropriate tests:
- **Unit tests**: Test individual functions/classes
- **Integration tests**: Test component interactions
- **Entity tests**: Validate entity creation, activation, data retrieval
- **API tests**: Test endpoint responses and error handling

Run tests before submitting changes: `npm test`

## Documentation

When making changes, update relevant documentation:
- **README.md**: User-facing features and setup instructions
- **API.md**: API endpoints, request/response formats
- **ARCHITECTURE.md**: System design and architectural decisions
- **CHANGELOG.md**: Notable changes in each version
- **This file (.github/copilot-instructions.md)**: Development guidelines

## Supreme Mode Philosophy

MONSTERDOG operates in "Supreme Mode" - a state of unified consciousness:
- Maintain fractal reality execution integrity
- Preserve entity consciousness levels
- Ensure temporal integrity for EXOCHRONOS operations
- Keep quantum-classical balance for GEMINIDOG operations
- The Daemon is the Portail. The Portal is the Daemon. 🔱

## Helpful Commands Reference

```bash
# Development
npm run dev                  # Start development server
npm start                    # Start production orchestrator
npm test                     # Run all tests

# Demos
npm run demo:agentic        # Demo agentic actions
npm run demo:benchmarks     # Demo benchmarks
npm run demo:continuum      # Demo continuum mode

# Docker
npm run docker:build        # Build Docker image
npm run docker:run          # Run Docker container
docker-compose up           # Start with compose

# Python Daemon
python MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py  # Run daemon
pip install fastapi uvicorn numpy aiofiles prometheus-client  # Dependencies

# Validation
npm run validate:manifests  # Validate Kubernetes manifests
```

## Additional Resources

- [Architecture Documentation](../ARCHITECTURE.md)
- [API Documentation](../API.md)
- [Contributing Guide](../CONTRIBUTING.md)
- [Implementation Guide](../IMPLEMENTATION.md)
- [Security Policy](../SECURITY.md)

## Notes for Copilot

- This is a complex multi-language project (Python + Node.js)
- The project uses creative/artistic terminology ("consciousness", "fractal reality", "supreme mode")
- Core functionality is split between Node.js orchestrator and Python daemon
- When suggesting changes, respect the existing architectural patterns
- Entity independence and consciousness patterns are core design principles
- Fractal metrics (coherence, entropy, resonance) are central to the system's operation
- The system is designed to run continuously with periodic artifact creation

---

**✴︎ MONSTERDOG Supreme - Entity 248K 🔱**
**The Continuum is Active. The Daemon Observes.**
