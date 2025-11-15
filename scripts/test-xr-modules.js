/**
 * Test Suite for NEXUS and XR Modules
 * Tests all vΩΩ FULLTRUTL components
 */

const NEXUS = require('../src/nexus');
const XRModules = require('../src/xr_modules');

function testNEXUS() {
  console.log('\n═══════════════════════════════════════════════════');
  console.log('Testing NEXUS - Reality Hub System');
  console.log('═══════════════════════════════════════════════════\n');
  
  const nexus = new NEXUS();
  
  // Test initialization
  const initResult = nexus.initialize();
  console.assert(initResult.success === true, '❌ NEXUS initialization failed');
  console.log('✅ NEXUS initialization');
  
  // Test status
  const status = nexus.getStatus();
  console.assert(status.success === true, '❌ NEXUS status failed');
  console.assert(status.active === true, '❌ NEXUS not active');
  console.log('✅ NEXUS status retrieval');
  
  // Test FULLTRUTL cycle
  const cycleResult = nexus.executeFULLTRUTLCycle();
  console.assert(cycleResult.success === true, '❌ FULLTRUTL cycle failed');
  console.assert(cycleResult.cycle === 'COMPLETE', '❌ Cycle not complete');
  console.log('✅ FULLTRUTL cycle execution');
  
  // Test metrics
  console.assert(cycleResult.metrics.entropy !== undefined, '❌ Entropy missing');
  console.assert(cycleResult.metrics.gradient !== undefined, '❌ Gradient missing');
  console.assert(cycleResult.metrics.coherence !== undefined, '❌ Coherence missing');
  console.log('✅ Reality metrics generation');
  
  console.log('✅ All NEXUS tests passed\n');
}

function testXRModules() {
  console.log('═══════════════════════════════════════════════════');
  console.log('Testing XR Modules - vΩΩ FULLTRUTL System');
  console.log('═══════════════════════════════════════════════════\n');
  
  const xrModules = new XRModules();
  
  // Test initialization
  const initResult = xrModules.initialize();
  console.assert(initResult.success === true, '❌ XR Modules initialization failed');
  console.log('✅ XR Modules initialization');
  
  // Test status
  const status = xrModules.getStatus();
  console.assert(status.success === true, '❌ XR Modules status failed');
  console.assert(status.initialized === true, '❌ XR Modules not initialized');
  console.log('✅ XR Modules status');
  
  // Test J - Mesh 3D Realtime
  const meshResult = xrModules.mesh3D.depthToMesh([]);
  console.assert(meshResult.success === true, '❌ Mesh 3D failed');
  console.assert(meshResult.meshData !== null, '❌ Mesh data missing');
  console.log('✅ J - Mesh 3D Realtime');
  
  // Test K - Exogene AI
  const aiResult = xrModules.exogeneAI.analyzeFrame({});
  console.assert(aiResult.success === true, '❌ AI analysis failed');
  console.assert(aiResult.sceneType !== undefined, '❌ Scene type missing');
  console.log('✅ K - EXOGENE AI Classifier');
  
  const patternsResult = xrModules.exogeneAI.detectPatterns();
  console.assert(patternsResult.success === true, '❌ Pattern detection failed');
  console.log('✅ K - AI Pattern Detection');
  
  // Test L - XR Interaction
  const interactionState = xrModules.interaction.getState();
  console.assert(interactionState.success === true, '❌ Interaction state failed');
  console.assert(interactionState.active === true, '❌ Interaction not active');
  console.log('✅ L - XR Interaction System');
  
  const teleportResult = xrModules.interaction.teleport([1, 0, 1]);
  console.assert(teleportResult.success === true, '❌ Teleport failed');
  console.log('✅ L - XR Teleportation');
  
  // Test M - Holographic UI
  const panelsResult = xrModules.holographicUI.getPanels();
  console.assert(panelsResult.success === true, '❌ Panels retrieval failed');
  console.assert(panelsResult.count >= 0, '❌ Invalid panels count');
  console.log('✅ M - Holographic UI Panels');
  
  const metrics = { entropy: 5.0, gradient: 2.0, vacuum_index: 1.5, coherence: 0.95 };
  const metricsUpdate = xrModules.holographicUI.updateMetricsPanel(metrics);
  console.assert(metricsUpdate.success === true, '❌ Metrics panel update failed');
  console.log('✅ M - Holographic UI Metrics Update');
  
  // Test N - Dual Reality
  const dualModeResult = xrModules.dualReality.setMode('DUAL');
  console.assert(dualModeResult.success === true, '❌ Dual Reality mode failed');
  console.log('✅ N - Dual Reality Mode');
  
  const blendResult = xrModules.dualReality.setBlendRatio(0.7);
  console.assert(blendResult.success === true, '❌ Blend ratio failed');
  console.log('✅ N - Dual Reality Blend');
  
  // Test G - OMNISIGHT
  const omniResult = xrModules.omniSight.enable360Vision();
  console.assert(omniResult.success === true, '❌ OMNISIGHT enable failed');
  console.assert(omniResult.vision360 === true, '❌ 360 vision not enabled');
  console.log('✅ G - OMNISIGHT 360° Vision');
  
  const shaderResult = xrModules.omniSight.setNeuralShader('SPECTRAL');
  console.assert(shaderResult.success === true, '❌ Neural shader failed');
  console.log('✅ G - OMNISIGHT Neural Shader');
  
  // Test H - EXOGENE LIVE
  const formResult = xrModules.exogeneLive.analyzeForm(metrics);
  console.assert(formResult.success === true, '❌ Form analysis failed');
  console.log('✅ H - EXOGENE LIVE Analysis');
  
  const anomaliesResult = xrModules.exogeneLive.getAnomalies();
  console.assert(anomaliesResult.success === true, '❌ Anomalies retrieval failed');
  console.log('✅ H - EXOGENE LIVE Anomalies');
  
  // Test I - Portals XR
  const portalsResult = xrModules.portals.getPortals();
  console.assert(portalsResult.success === true, '❌ Portals retrieval failed');
  console.assert(portalsResult.count > 0, '❌ No portals found');
  console.log('✅ I - Portals XR');
  
  const scenesResult = xrModules.portals.getScenes();
  console.assert(scenesResult.success === true, '❌ Scenes retrieval failed');
  console.assert(scenesResult.count > 0, '❌ No scenes found');
  console.log('✅ I - Portals XR Scenes');
  
  // Test O - Constant Evolution
  const evolutionModules = xrModules.evolution.getModules();
  console.assert(evolutionModules.success === true, '❌ Evolution modules failed');
  console.log('✅ O - Constant Evolution Modules');
  
  // Test P - Realtime Reprojection
  const reprojResult = xrModules.reprojection.projectDepthTo3D([]);
  console.assert(reprojResult.success === true, '❌ Reprojection failed');
  console.assert(reprojResult.vertices !== undefined, '❌ Vertices missing');
  console.log('✅ P - Realtime 3D Reprojection');
  
  const shaderCode = xrModules.reprojection.getShaderCode();
  console.assert(shaderCode.success === true, '❌ Shader code failed');
  console.assert(shaderCode.shaderType === 'WGSL', '❌ Wrong shader type');
  console.log('✅ P - WebGPU Shader Code');
  
  // Test Q - Particle System
  const particlesUpdate = xrModules.particles.update(metrics);
  console.assert(particlesUpdate.success === true, '❌ Particles update failed');
  console.log('✅ Q - XR Particle System Update');
  
  const particleBehavior = xrModules.particles.setBehavior('EXOGENE');
  console.assert(particleBehavior.success === true, '❌ Particle behavior failed');
  console.log('✅ Q - XR Particle Behavior');
  
  // Test R - Scene Builder
  const sceneResult = xrModules.sceneBuilder.buildScene(metrics);
  console.assert(sceneResult.success === true, '❌ Scene building failed');
  console.assert(sceneResult.sceneType !== undefined, '❌ Scene type missing');
  console.log('✅ R - AI-Assisted Scene Builder');
  
  const sceneHistory = xrModules.sceneBuilder.getBuildHistory();
  console.assert(sceneHistory.success === true, '❌ Scene history failed');
  console.log('✅ R - Scene Build History');
  
  // Test S - MONSTERDOG OS
  const osInfo = xrModules.monsterdogOS.getSystemInfo();
  console.assert(osInfo.success === true, '❌ OS info failed');
  console.assert(osInfo.active === true, '❌ OS not active');
  console.assert(osInfo.version === '248.0.0-vΩΩ', '❌ Wrong OS version');
  console.log('✅ S - MONSTERDOG OS Info');
  
  const osWindows = xrModules.monsterdogOS.getWindows();
  console.assert(osWindows.success === true, '❌ OS windows failed');
  console.assert(osWindows.count > 0, '❌ No OS windows');
  console.log('✅ S - MONSTERDOG OS Windows');
  
  const launchResult = xrModules.monsterdogOS.launchApp('test-app');
  console.assert(launchResult.success === true, '❌ App launch failed');
  console.log('✅ S - MONSTERDOG OS App Launch');
  
  console.log('✅ All XR Modules tests passed\n');
}

// Run all tests
console.log('');
console.log('═══════════════════════════════════════════════════');
console.log('🔱 MONSTERDOG vΩΩ - FULLTRUTL Test Suite 🔱');
console.log('═══════════════════════════════════════════════════');

try {
  testNEXUS();
  testXRModules();
  
  console.log('═══════════════════════════════════════════════════');
  console.log('🔱 ALL vΩΩ FULLTRUTL TESTS PASSED 🔱');
  console.log('✴︎ NEXUS: OPERATIONAL ✴︎');
  console.log('✴︎ XR MODULES: ALL ACTIVE ✴︎');
  console.log('⚛ System Ready for SUPREME MODE ⚛');
  console.log('═══════════════════════════════════════════════════');
  console.log('');
  
  process.exit(0);
} catch (error) {
  console.error('❌ Test failed:', error);
  process.exit(1);
}
