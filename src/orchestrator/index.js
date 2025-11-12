/**
 * MONSTERDOG SUPREME - FULLTRUTL Orchestrator
 * Entity 248K - Fractal Reality Execution Engine
 */

const express = require('express');
const path = require('path');

// Import entity modules
const MonsterdogEntity = require('../entities/monsterdog');
const GeminidogEntity = require('../entities/geminidog');
const ExochronosEntity = require('../entities/exochronos');

// Import core modules
const WebXREngine = require('../webxr');
const NFTIntegration = require('../nft');
const AGIOrchestrator = require('../agi');
const ContinuumMode = require('../continuum');

class FULLTRUTLOrchestrator {
  constructor() {
    this.app = express();
    this.port = process.env.PORT || 8080;
    this.supremeMode = process.env.SUPREME_MODE === 'active';
    this.fractalReality = process.env.FRACTAL_REALITY === 'enabled';
    
    // Initialize entities
    this.entities = {
      monsterdog: new MonsterdogEntity(),
      geminidog: new GeminidogEntity(),
      exochronos: new ExochronosEntity()
    };
    
    // Initialize core systems
    this.webxr = new WebXREngine();
    this.nft = new NFTIntegration();
    this.agi = new AGIOrchestrator();
    this.continuum = new ContinuumMode(this);
    
    this.initialize();
  }
  
  initialize() {
    console.log('🔱 MONSTERDOG SUPREME MODE ACTIVATED 🔱');
    console.log('✴︎ Initializing FULLTRUTL Orchestrator ✴︎');
    console.log(`🛸 Entity Mode: MONSTERDOG + GEMINIDOG + EXOCHRONOS 🛸`);
    console.log(`⚛ Fractal Reality: ${this.fractalReality ? 'ACTIVE' : 'STANDBY'} ⚛`);
    
    // Setup middleware
    this.app.use(express.json());
    this.app.use(express.static('public'));
    
    // Initialize core systems
    this.webxr.initialize();
    this.nft.initialize();
    this.agi.initialize();
    this.continuum.initialize();
    
    // Setup routes
    this.setupRoutes();
    
    // Activate entities
    this.activateEntities();
  }
  
  setupRoutes() {
    // Health check
    this.app.get('/status', (req, res) => {
      res.json({
        status: 'SUPREME_MODE_ACTIVE',
        entities: {
          monsterdog: this.entities.monsterdog.getStatus(),
          geminidog: this.entities.geminidog.getStatus(),
          exochronos: this.entities.exochronos.getStatus()
        },
        systems: {
          webxr: this.webxr.isActive(),
          nft: this.nft.isConnected(),
          agi: this.agi.getStatus(),
          continuum: this.continuum.getStatus()
        },
        fractalReality: this.fractalReality
      });
    });
    
    // Entity endpoints
    this.app.get('/entities/monsterdog', (req, res) => {
      res.json(this.entities.monsterdog.getData());
    });
    
    this.app.get('/entities/geminidog', (req, res) => {
      res.json(this.entities.geminidog.getData());
    });
    
    this.app.get('/entities/exochronos', (req, res) => {
      res.json(this.entities.exochronos.getData());
    });
    
    // WebXR endpoint
    this.app.get('/webxr/scene', (req, res) => {
      res.json(this.webxr.getScene());
    });
    
    // NFT endpoints
    this.app.get('/nft/collection', (req, res) => {
      res.json(this.nft.getCollection());
    });
    
    // AGI endpoints
    this.app.post('/agi/command', (req, res) => {
      const result = this.agi.executeCommand(req.body);
      res.json(result);
    });
    
    // Continuum mode endpoints
    this.app.get('/continuum/status', (req, res) => {
      res.json(this.continuum.getStatus());
    });
    
    this.app.get('/continuum/actions', (req, res) => {
      res.json({
        actions: this.continuum.getActions(),
        total: this.continuum.getActions().length
      });
    });
    
    this.app.post('/continuum/activate', (req, res) => {
      const result = this.continuum.activate();
      res.json(result);
    });
    
    this.app.post('/continuum/deactivate', (req, res) => {
      const result = this.continuum.deactivate();
      res.json(result);
    });
    
    this.app.post('/continuum/action/:actionId', (req, res) => {
      const result = this.continuum.executeAction(req.params.actionId);
      res.json(result);
    });
  }
  
  activateEntities() {
    console.log('👾 Activating MONSTERDOG Entity...');
    this.entities.monsterdog.activate();
    
    console.log('🧬 Activating GEMINIDOG Entity...');
    this.entities.geminidog.activate();
    
    console.log('🔱 Activating EXOCHRONOS Entity...');
    this.entities.exochronos.activate();
    
    console.log('✴︎ All entities activated in SUPREME MODE ✴︎');
  }
  
  start() {
    this.app.listen(this.port, () => {
      console.log('');
      console.log('═══════════════════════════════════════════════════');
      console.log('👾 MONSTERDOG SUPREME - ENTITY 248K 👾');
      console.log('✴︎ FULLTRUTL Orchestrator ACTIVE ✴︎');
      console.log(`🌐 Server running on port ${this.port}`);
      console.log('🔱 Mode: SUPRÊME ENCLENCHÉ 🔱');
      console.log('⚛ Fractal Reality: IN EXECUTION ⚛');
      console.log('═══════════════════════════════════════════════════');
      console.log('');
    });
  }
}

// Start the orchestrator only if this file is run directly
if (require.main === module) {
  const orchestrator = new FULLTRUTLOrchestrator();
  orchestrator.start();
}

module.exports = FULLTRUTLOrchestrator;
