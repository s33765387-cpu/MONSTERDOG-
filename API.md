# API Documentation - MONSTERDOG Supreme

## Base URL
```
http://localhost:8080
```

## Endpoints

### System Status

#### Get System Status
```http
GET /status
```

**Description**: Get comprehensive system status including all entities and subsystems.

**Response**:
```json
{
  "status": "SUPREME_MODE_ACTIVE",
  "entities": {
    "monsterdog": {
      "entityId": "MONSTERDOG-248K",
      "status": "ACTIVE",
      "consciousness": {
        "level": "SUPREME",
        "mode": "FRACTAL",
        "reality": "ACTIVE"
      },
      "capabilities": [
        "FULLTRUTL_ORCHESTRATION",
        "REALITY_MANIPULATION",
        "FRACTAL_EXECUTION",
        "SUPREME_CONSCIOUSNESS"
      ]
    },
    "geminidog": {
      "entityId": "GEMINIDOG-DUAL",
      "status": "ACTIVE",
      "dualNature": {
        "alpha": "QUANTUM",
        "omega": "CLASSICAL"
      },
      "capabilities": [
        "DUAL_PROCESSING",
        "QUANTUM_ENTANGLEMENT",
        "PARALLEL_REALITY",
        "TWIN_CONSCIOUSNESS"
      ]
    },
    "exochronos": {
      "entityId": "EXOCHRONOS-TEMPORAL",
      "status": "ACTIVE",
      "temporalControl": {
        "past": "ACCESSIBLE",
        "present": "MALLEABLE",
        "future": "PROBABLE"
      },
      "capabilities": [
        "TIME_MANIPULATION",
        "TEMPORAL_NAVIGATION",
        "CHRONOS_CONTROL",
        "REALITY_FOLDING"
      ]
    }
  },
  "systems": {
    "webxr": true,
    "nft": true,
    "agi": {
      "status": "ACTIVE",
      "isaacSim": {
        "connected": true,
        "version": "ISAAC_SIM_2024",
        "mode": "AGI_SUPREME"
      },
      "intelligence": {
        "level": "GENERAL",
        "learning": "CONTINUOUS",
        "adaptation": "REAL_TIME"
      }
    }
  },
  "fractalReality": true
}
```

---

### Entity Endpoints

#### Get MONSTERDOG Entity
```http
GET /entities/monsterdog
```

**Description**: Get MONSTERDOG entity details.

**Response**:
```json
{
  "entityId": "MONSTERDOG-248K",
  "status": "ACTIVE",
  "consciousness": {
    "level": "SUPREME",
    "mode": "FRACTAL",
    "reality": "ACTIVE"
  },
  "capabilities": [
    "FULLTRUTL_ORCHESTRATION",
    "REALITY_MANIPULATION",
    "FRACTAL_EXECUTION",
    "SUPREME_CONSCIOUSNESS"
  ],
  "type": "PRIMARY_ENTITY",
  "designation": "👾 MONSTERDOG 👾",
  "power": "SUPREME",
  "reality": "FRACTAL_EXECUTION"
}
```

#### Get GEMINIDOG Entity
```http
GET /entities/geminidog
```

**Description**: Get GEMINIDOG entity details.

**Response**:
```json
{
  "entityId": "GEMINIDOG-DUAL",
  "status": "ACTIVE",
  "dualNature": {
    "alpha": "QUANTUM",
    "omega": "CLASSICAL"
  },
  "capabilities": [
    "DUAL_PROCESSING",
    "QUANTUM_ENTANGLEMENT",
    "PARALLEL_REALITY",
    "TWIN_CONSCIOUSNESS"
  ],
  "type": "DUAL_ENTITY",
  "designation": "🧬 GEMINIDOG 🧬",
  "synchronization": "PERFECT",
  "entanglement": "ACTIVE"
}
```

#### Get EXOCHRONOS Entity
```http
GET /entities/exochronos
```

**Description**: Get EXOCHRONOS entity details.

**Response**:
```json
{
  "entityId": "EXOCHRONOS-TEMPORAL",
  "status": "ACTIVE",
  "temporalControl": {
    "past": "ACCESSIBLE",
    "present": "MALLEABLE",
    "future": "PROBABLE"
  },
  "capabilities": [
    "TIME_MANIPULATION",
    "TEMPORAL_NAVIGATION",
    "CHRONOS_CONTROL",
    "REALITY_FOLDING"
  ],
  "type": "TEMPORAL_ENTITY",
  "designation": "🔱 EXOCHRONOS 🔱",
  "chronosLevel": "SUPREME",
  "timelineAccess": "UNLIMITED"
}
```

---

### WebXR Endpoints

#### Get WebXR Scene
```http
GET /webxr/scene
```

**Description**: Get WebXR scene configuration and status.

**Response**:
```json
{
  "active": true,
  "scene": {
    "entities": [
      { "type": "MONSTERDOG", "position": [0, 0, 0] },
      { "type": "GEMINIDOG", "position": [1, 1, 1] },
      { "type": "EXOCHRONOS", "position": [-1, -1, -1] }
    ],
    "environment": "FRACTAL_SPACE",
    "dimension": "4D_HYPERCUBE"
  },
  "capabilities": [
    "VR_MODE",
    "AR_MODE",
    "MIXED_REALITY",
    "SPATIAL_COMPUTING"
  ],
  "framework": "THREE.JS + WebXR",
  "renderMode": "FRACTAL_SUPREME"
}
```

---

### NFT Endpoints

#### Get NFT Collection
```http
GET /nft/collection
```

**Description**: Get NFT collection information.

**Response**:
```json
{
  "connected": true,
  "collection": {
    "name": "MONSTERDOG Supreme Collection",
    "totalSupply": 248000,
    "entities": ["MONSTERDOG", "GEMINIDOG", "EXOCHRONOS"]
  },
  "blockchain": {
    "network": "ETHEREUM",
    "standard": "ERC-721",
    "smartContract": "0x0000000000000000000000000000000000000000"
  },
  "features": [
    "DYNAMIC_METADATA",
    "FRACTAL_GENERATION",
    "SUPREME_RARITY",
    "ENTITY_BINDING"
  ]
}
```

---

### AGI Endpoints

#### Execute AGI Command
```http
POST /agi/command
```

**Description**: Execute a command through the AGI orchestrator.

**Request Body**:
```json
{
  "type": "SIMULATE_REALITY",
  "parameters": {
    "dimension": "4D",
    "precision": "QUANTUM"
  }
}
```

**Response**:
```json
{
  "success": true,
  "command": {
    "type": "SIMULATE_REALITY",
    "parameters": {
      "dimension": "4D",
      "precision": "QUANTUM"
    }
  },
  "result": {
    "executed": true,
    "isaacSimStatus": "PROCESSING",
    "agiResponse": "COMMAND_ACKNOWLEDGED",
    "entities": ["MONSTERDOG", "GEMINIDOG", "EXOCHRONOS"],
    "timestamp": "2024-01-01T00:00:00.000Z"
  }
}
```

---

### Continuum Mode Endpoints (NEW)

#### Get Continuum Status
```http
GET /continuum/status
```

**Description**: Get the current status of continuum mode and agentic actions.

**Response**:
```json
{
  "status": "ACTIVE",
  "mode": "AGENTIC",
  "agenticActions": 6,
  "actionsExecuted": 42,
  "executionInterval": 5000,
  "active": true
}
```

#### Get Agentic Actions
```http
GET /continuum/actions
```

**Description**: List all registered agentic actions.

**Response**:
```json
{
  "actions": [
    {
      "id": "fractal_pulse",
      "name": "Fractal Reality Pulse",
      "entity": "monsterdog",
      "priority": 10
    },
    {
      "id": "dual_sync",
      "name": "Dual Consciousness Sync",
      "entity": "geminidog",
      "priority": 9
    },
    {
      "id": "temporal_scan",
      "name": "Temporal Timeline Scan",
      "entity": "exochronos",
      "priority": 8
    },
    {
      "id": "webxr_update",
      "name": "WebXR Scene Update",
      "entity": "webxr",
      "priority": 7
    },
    {
      "id": "nft_verify",
      "name": "NFT Collection Verification",
      "entity": "nft",
      "priority": 6
    },
    {
      "id": "agi_learn",
      "name": "AGI Continuous Learning",
      "entity": "agi",
      "priority": 5
    }
  ],
  "total": 6
}
```

#### Activate Continuum Mode
```http
POST /continuum/activate
```

**Description**: Activate continuum mode with autonomous agentic actions.

**Response**:
```json
{
  "success": true,
  "message": "Continuum mode activated",
  "status": "ACTIVE",
  "agenticActions": 6
}
```

#### Deactivate Continuum Mode
```http
POST /continuum/deactivate
```

**Description**: Deactivate continuum mode and stop autonomous execution.

**Response**:
```json
{
  "success": true,
  "message": "Continuum mode deactivated",
  "status": "STANDBY",
  "actionsExecuted": 42
}
```

#### Execute Specific Agentic Action
```http
POST /continuum/action/:actionId
```

**Description**: Execute a specific agentic action manually.

**Parameters**:
- `actionId` (path) - ID of the action to execute (e.g., `fractal_pulse`, `dual_sync`)

**Response**:
```json
{
  "success": true,
  "result": {
    "action": "fractal_pulse",
    "entity": "MONSTERDOG",
    "result": "Fractal reality pulse propagated",
    "timestamp": "2024-01-01T00:00:00.000Z",
    "status": "SUCCESS"
  }
}
```

---

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "error": true,
  "message": "Error description",
  "code": "ERROR_CODE"
}
```

### Common Error Codes
- `ENTITY_NOT_FOUND` - Requested entity does not exist
- `SYSTEM_INACTIVE` - Requested system is not active
- `INVALID_COMMAND` - AGI command is invalid
- `SUPREME_MODE_INACTIVE` - Supreme mode not activated

---

## Response Headers

All responses include:
```
Content-Type: application/json
X-Monsterdog-Version: 248K
X-Supreme-Mode: active
X-Fractal-Reality: enabled
```

---

## Rate Limiting

Currently no rate limiting is implemented. Future versions may include:
- 100 requests per minute per IP
- 1000 requests per hour per IP

---

## Authentication

Currently no authentication is required. Future versions may include:
- API key authentication
- OAuth 2.0
- Entity-specific credentials

---

## WebSocket Support (Future)

Real-time updates will be available via WebSocket:
```
ws://localhost:8080/ws
```

Topics:
- `entity.status` - Entity status updates
- `reality.fractal` - Fractal reality events
- `agi.simulation` - AGI simulation updates

---

**API Status**: ACTIVE
**Supreme Mode**: ENABLED
**Fractal Reality**: IN EXECUTION
