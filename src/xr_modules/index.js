/**
 * XR Modules - Advanced WebXR Features
 * Complete implementation of F through S modules
 */

const Mesh3DRealtime = require('./mesh_3d_realtime');
const ExogeneAI = require('./exogene_ai');
const XRInteraction = require('./xr_interaction');
const HolographicUI = require('./holographic_ui');
const DualReality = require('./dual_reality');
const OmniSight = require('./omnisight');
const ExogeneLive = require('./exogene_live');
const PortalsXR = require('./portals_xr');
const ConstantEvolution = require('./constant_evolution');
const RealtimeReprojection = require('./realtime_reprojection');
const ParticleSystem = require('./particle_system');
const SceneBuilder = require('./scene_builder');
const MonsterdogOS = require('./monsterdog_os');

class XRModules {
  constructor() {
    // Initialize all modules
    this.mesh3D = new Mesh3DRealtime();                    // J - Full 3D Mesh
    this.exogeneAI = new ExogeneAI();                      // K - AI Classifier
    this.interaction = new XRInteraction();                 // L - Interaction System
    this.holographicUI = new HolographicUI();              // M - Holographic UI
    this.dualReality = new DualReality();                  // N - Dual Reality
    this.omniSight = new OmniSight();                      // G - OMNISIGHT
    this.exogeneLive = new ExogeneLive();                  // H - EXOGENE LIVE
    this.portals = new PortalsXR();                        // I - Portals
    this.evolution = new ConstantEvolution();               // O - Constant Evolution
    this.reprojection = new RealtimeReprojection();        // P - Realtime Reprojection
    this.particles = new ParticleSystem();                  // Q - Particle System
    this.sceneBuilder = new SceneBuilder();                // R - Scene Builder
    this.monsterdogOS = new MonsterdogOS();                // S - MONSTERDOG OS
    
    this.initialized = false;
  }
  
  initialize() {
    console.log('');
    console.log('═══════════════════════════════════════════════════');
    console.log('🔱 XR MODULES INITIALIZATION - vΩΩ FULLTRUTL 🔱');
    console.log('═══════════════════════════════════════════════════');
    
    // Initialize all modules
    this.mesh3D.initialize();
    this.exogeneAI.initialize();
    this.interaction.initialize();
    this.holographicUI.initialize();
    this.dualReality.initialize();
    this.omniSight.initialize();
    this.exogeneLive.initialize();
    this.portals.initialize();
    this.evolution.initialize();
    this.reprojection.initialize();
    this.particles.initialize();
    this.sceneBuilder.initialize();
    this.monsterdogOS.initialize();
    
    this.initialized = true;
    
    console.log('✴︎ ALL XR MODULES OPERATIONAL ✴︎');
    console.log('═══════════════════════════════════════════════════');
    console.log('');
    
    return { success: true, status: 'ALL_MODULES_ACTIVE' };
  }
  
  getStatus() {
    return {
      success: true,
      initialized: this.initialized,
      modules: {
        mesh3D: this.mesh3D.getMeshData ? true : false,
        exogeneAI: this.exogeneAI.active,
        interaction: this.interaction.active,
        holographicUI: this.holographicUI.active,
        dualReality: this.dualReality.active,
        omniSight: this.omniSight.active,
        exogeneLive: this.exogeneLive.active,
        portals: this.portals.active,
        evolution: this.evolution.active,
        reprojection: this.reprojection.active,
        particles: this.particles.active,
        sceneBuilder: this.sceneBuilder.active,
        monsterdogOS: this.monsterdogOS.active
      }
    };
  }
  
  // Convenience method to get all module instances
  getAllModules() {
    return {
      mesh3D: this.mesh3D,
      exogeneAI: this.exogeneAI,
      interaction: this.interaction,
      holographicUI: this.holographicUI,
      dualReality: this.dualReality,
      omniSight: this.omniSight,
      exogeneLive: this.exogeneLive,
      portals: this.portals,
      evolution: this.evolution,
      reprojection: this.reprojection,
      particles: this.particles,
      sceneBuilder: this.sceneBuilder,
      monsterdogOS: this.monsterdogOS
    };
  }
}

module.exports = XRModules;
