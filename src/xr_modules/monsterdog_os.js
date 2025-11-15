/**
 * S - MONSTERDOG OS
 * Complete XR operating system interface
 */

class MonsterdogOS {
  constructor() {
    this.active = false;
    this.windows = new Map();
    this.processes = new Map();
    this.desktop = {
      background: '#000000',
      grid: true,
      icons: []
    };
    this.startTime = Date.now();
  }
  
  initialize() {
    console.log('🖥 MONSTERDOG OS initializing...');
    this.active = true;
    this.createDefaultWindows();
    this.createDesktopIcons();
    console.log('✴︎ MONSTERDOG OS ACTIVE');
    return { success: true, status: 'ACTIVE' };
  }
  
  createDefaultWindows() {
    this.spawnWindow('metrics', {
      title: 'Métriques',
      position: { x: -0.4, y: 1.4, z: -1 },
      size: { width: 0.6, height: 0.4 },
      content: 'Entropy: 0\nGradient: 0\nVacuum: 0'
    });
    
    this.spawnWindow('console', {
      title: 'Console',
      position: { x: 0, y: 1.0, z: -1 },
      size: { width: 0.6, height: 0.4 },
      content: 'MONSTERDOG OS v248.0.0\nSystem Ready'
    });
    
    this.spawnWindow('modules', {
      title: 'Modules',
      position: { x: 0.4, y: 1.4, z: -1 },
      size: { width: 0.6, height: 0.4 },
      content: 'Active Modules: 0'
    });
    
    this.spawnWindow('nexus', {
      title: 'Nexus',
      position: { x: 0, y: 1.8, z: -1 },
      size: { width: 0.8, height: 0.5 },
      content: 'NEXUS Hub Status: ONLINE'
    });
  }
  
  createDesktopIcons() {
    this.desktop.icons = [
      { id: 'metrics', label: 'Metrics', position: { x: -1, y: 0.5, z: -2 } },
      { id: 'vision', label: 'Vision', position: { x: -0.5, y: 0.5, z: -2 } },
      { id: 'particles', label: 'Particles', position: { x: 0, y: 0.5, z: -2 } },
      { id: 'portals', label: 'Portals', position: { x: 0.5, y: 0.5, z: -2 } },
      { id: 'settings', label: 'Settings', position: { x: 1, y: 0.5, z: -2 } }
    ];
  }
  
  spawnWindow(id, config) {
    const window = {
      id: id,
      title: config.title || 'Window',
      position: config.position || { x: 0, y: 1.4, z: -1 },
      size: config.size || { width: 0.6, height: 0.4 },
      content: config.content || '',
      visible: true,
      opacity: 0.85,
      color: '#111'
    };
    
    this.windows.set(id, window);
    
    return {
      success: true,
      windowId: id,
      window: window
    };
  }
  
  updateWindow(id, updates) {
    const window = this.windows.get(id);
    
    if (!window) {
      return { success: false, error: 'WINDOW_NOT_FOUND' };
    }
    
    Object.assign(window, updates);
    
    return {
      success: true,
      windowId: id,
      window: window
    };
  }
  
  closeWindow(id) {
    const deleted = this.windows.delete(id);
    
    return {
      success: deleted,
      windowId: id
    };
  }
  
  updateMetrics(metrics) {
    const content = `Entropy: ${metrics.entropy.toFixed(3)}\nGradient: ${metrics.gradient.toFixed(3)}\nVacuum: ${metrics.vacuum_index.toFixed(3)}\nCoherence: ${metrics.coherence.toFixed(3)}`;
    
    return this.updateWindow('metrics', { content: content });
  }
  
  launchApp(appId) {
    const process = {
      id: `proc_${Date.now()}`,
      appId: appId,
      startTime: Date.now(),
      status: 'RUNNING'
    };
    
    this.processes.set(process.id, process);
    
    return {
      success: true,
      processId: process.id,
      appId: appId
    };
  }
  
  killProcess(processId) {
    const deleted = this.processes.delete(processId);
    
    return {
      success: deleted,
      processId: processId
    };
  }
  
  getSystemInfo() {
    const uptime = Math.floor((Date.now() - this.startTime) / 1000);
    
    return {
      success: true,
      active: this.active,
      uptime: uptime,
      windows: this.windows.size,
      processes: this.processes.size,
      version: '248.0.0-vΩΩ'
    };
  }
  
  getWindows() {
    return {
      success: true,
      windows: Array.from(this.windows.values()),
      count: this.windows.size
    };
  }
  
  getProcesses() {
    return {
      success: true,
      processes: Array.from(this.processes.values()),
      count: this.processes.size
    };
  }
  
  getDesktop() {
    return {
      success: true,
      desktop: this.desktop
    };
  }
}

module.exports = MonsterdogOS;
