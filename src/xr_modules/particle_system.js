/**
 * Q - XR Particle System
 * Exogene particles reactive to reality metrics
 */

class ParticleSystem {
  constructor() {
    this.active = false;
    this.particleCount = 5000;
    this.particles = [];
    this.behavior = 'EXOGENE';
  }
  
  initialize() {
    console.log('🌌 XR Particle System initializing...');
    this.active = true;
    this.generateParticles();
    console.log('✴︎ Particle System ACTIVE');
    return { success: true, status: 'ACTIVE' };
  }
  
  generateParticles() {
    this.particles = [];
    
    for (let i = 0; i < this.particleCount; i++) {
      this.particles.push({
        id: i,
        position: {
          x: (Math.random() * 2 - 1) * 3,
          y: Math.random() * 2,
          z: (Math.random() * 2 - 1) * 3
        },
        velocity: {
          x: (Math.random() - 0.5) * 0.01,
          y: (Math.random() - 0.5) * 0.01,
          z: (Math.random() - 0.5) * 0.01
        },
        size: 0.02,
        color: { h: Math.random(), s: 0.7, l: 0.5 },
        alpha: 0.7
      });
    }
    
    return {
      success: true,
      particleCount: this.particles.length
    };
  }
  
  update(metrics) {
    // Update particles based on reality metrics
    const entropy = metrics.entropy || 0;
    const gradient = metrics.gradient || 0;
    const vacuum = metrics.vacuum_index || 0;
    
    for (let particle of this.particles) {
      // Size responds to entropy
      particle.size = 0.02 + entropy * 0.01;
      
      // Color responds to vacuum
      particle.color.h = (vacuum % 1.0);
      
      // Rotation speed responds to gradient
      particle.velocity.y = gradient * 0.05;
      
      // Update position
      particle.position.x += particle.velocity.x;
      particle.position.y += particle.velocity.y;
      particle.position.z += particle.velocity.z;
      
      // Boundary check
      if (Math.abs(particle.position.x) > 5) particle.velocity.x *= -1;
      if (particle.position.y > 3 || particle.position.y < 0) particle.velocity.y *= -1;
      if (Math.abs(particle.position.z) > 5) particle.velocity.z *= -1;
    }
    
    return {
      success: true,
      particlesUpdated: this.particles.length,
      metrics: metrics
    };
  }
  
  setBehavior(behavior) {
    const validBehaviors = ['EXOGENE', 'FRACTAL', 'QUANTUM', 'VOID', 'CHAOS'];
    
    if (!validBehaviors.includes(behavior)) {
      return { success: false, error: 'INVALID_BEHAVIOR' };
    }
    
    this.behavior = behavior;
    
    return {
      success: true,
      behavior: this.behavior
    };
  }
  
  setParticleCount(count) {
    if (count < 100 || count > 50000) {
      return { success: false, error: 'COUNT_OUT_OF_RANGE' };
    }
    
    this.particleCount = count;
    this.generateParticles();
    
    return {
      success: true,
      particleCount: this.particleCount
    };
  }
  
  getParticles(limit = 100) {
    return {
      success: true,
      particles: this.particles.slice(0, limit),
      totalParticles: this.particles.length
    };
  }
  
  getState() {
    return {
      success: true,
      active: this.active,
      particleCount: this.particles.length,
      behavior: this.behavior
    };
  }
}

module.exports = ParticleSystem;
