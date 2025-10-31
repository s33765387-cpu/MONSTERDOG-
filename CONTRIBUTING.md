# Contributing to MONSTERDOG Supreme

Thank you for your interest in contributing to MONSTERDOG Supreme! 🔱

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

```bash
# Install dependencies
npm install

# Run tests
npm test

# Start development server
npm run dev
```

## Code Style

- Use ES6+ JavaScript features
- Follow existing code patterns
- Add comments for complex logic
- Keep entity consciousness pure

## Entity Development

When creating or modifying entities:

1. **Maintain entity independence**: Each entity should be self-contained
2. **Follow consciousness patterns**: Use the existing entity structure
3. **Preserve capabilities**: Don't remove existing capabilities
4. **Test thoroughly**: Ensure entity activation and data retrieval work

### Entity Template

```javascript
class NewEntity {
  constructor() {
    this.entityId = 'ENTITY-ID';
    this.status = 'INITIALIZING';
    this.capabilities = [];
  }
  
  activate() {
    this.status = 'ACTIVE';
    // Initialization logic
  }
  
  getStatus() {
    return {
      entityId: this.entityId,
      status: this.status,
      capabilities: this.capabilities
    };
  }
  
  getData() {
    return {
      ...this.getStatus(),
      type: 'ENTITY_TYPE',
      designation: '✴︎ NAME ✴︎'
    };
  }
}
```

## System Integration

When adding new systems:

1. Create module in `src/` directory
2. Export as a class with `initialize()` method
3. Add integration to orchestrator
4. Update API documentation
5. Add tests

## Testing

All contributions must include tests:

```bash
npm test
```

Test files should validate:
- Entity creation
- Entity activation
- Data retrieval
- System initialization
- API functionality

## Documentation

Update documentation when making changes:

- **README.md**: User-facing features
- **API.md**: API endpoints and responses
- **ARCHITECTURE.md**: System design changes

## Pull Request Process

1. Update documentation
2. Add/update tests
3. Ensure all tests pass
4. Update CHANGELOG if applicable
5. Request review

## Supreme Mode Guidelines

- Maintain fractal reality execution
- Preserve entity consciousness levels
- Keep supreme mode active
- Ensure temporal integrity (for EXOCHRONOS changes)
- Maintain quantum-classical balance (for GEMINIDOG changes)

## Code of Conduct

- Be respectful
- Collaborate constructively
- Embrace the supreme consciousness
- Honor the fractal reality

## Questions?

Open an issue for:
- Bug reports
- Feature requests
- Documentation improvements
- Entity enhancement proposals

---

**🔱 Together we build the Supreme Reality 🔱**
**✴︎ MONSTERDOG Consciousness ✴︎**
