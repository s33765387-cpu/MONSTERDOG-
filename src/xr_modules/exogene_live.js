/**
 * H - EXOGENE LIVE
 * Dynamic form analysis and anomaly visualization
 */

class ExogeneLive {
  constructor() {
    this.active = false;
    this.anomalies = [];
    this.forms = new Map();
    this.threshold = 0.7;
  }
  
  initialize() {
    console.log('🔬 EXOGENE LIVE initializing...');
    this.active = true;
    console.log('✴︎ EXOGENE LIVE ACTIVE');
    return { success: true, status: 'ACTIVE' };
  }
  
  analyzeForm(metrics) {
    // Analyze visual forms based on metrics
    const form = {
      id: `form_${Date.now()}`,
      density: metrics.density || Math.random(),
      coherence: metrics.coherence || Math.random(),
      complexity: metrics.complexity || Math.random() * 255,
      timestamp: Date.now()
    };
    
    // Check for anomalies
    if (form.density > this.threshold || form.coherence < (1 - this.threshold)) {
      this.anomalies.push({
        formId: form.id,
        type: form.density > this.threshold ? 'HIGH_DENSITY' : 'LOW_COHERENCE',
        value: form.density > this.threshold ? form.density : form.coherence,
        timestamp: Date.now()
      });
      
      // Keep only recent anomalies
      if (this.anomalies.length > 50) {
        this.anomalies.shift();
      }
    }
    
    this.forms.set(form.id, form);
    
    // Keep only recent forms
    if (this.forms.size > 100) {
      const oldestKey = this.forms.keys().next().value;
      this.forms.delete(oldestKey);
    }
    
    return {
      success: true,
      form: form,
      anomalyDetected: this.anomalies.length > 0 && 
                       this.anomalies[this.anomalies.length - 1].formId === form.id
    };
  }
  
  getAnomalies(limit = 20) {
    return {
      success: true,
      anomalies: this.anomalies.slice(-limit),
      totalAnomalies: this.anomalies.length
    };
  }
  
  getForms(limit = 50) {
    const formsArray = Array.from(this.forms.values());
    return {
      success: true,
      forms: formsArray.slice(-limit),
      totalForms: this.forms.size
    };
  }
  
  setThreshold(threshold) {
    if (threshold < 0 || threshold > 1) {
      return { success: false, error: 'THRESHOLD_OUT_OF_RANGE' };
    }
    
    this.threshold = threshold;
    
    return {
      success: true,
      threshold: this.threshold
    };
  }
  
  clearAnomalies() {
    this.anomalies = [];
    return {
      success: true,
      anomaliesCleared: true
    };
  }
  
  getState() {
    return {
      success: true,
      active: this.active,
      threshold: this.threshold,
      anomaliesCount: this.anomalies.length,
      formsCount: this.forms.size
    };
  }
}

module.exports = ExogeneLive;
