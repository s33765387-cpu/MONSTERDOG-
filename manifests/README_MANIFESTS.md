# Manifests for MONSTERDOG agentic actions

Each action has an associated manifest in `manifests/monsterdog/*.json` containing:

- id: numeric identifier
- name: action name (must match runtime)
- category: action category
- description: short human readable summary
- parameters: parameter schema with defaults
- version: semantic version of the manifest
- deploy.artifact: suggested deployment package path

Use `npm run validate:manifests` to verify manifests match the implemented actions.
